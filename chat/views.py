from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .chat import get_response
from rest_framework import generics
from .models import Chat_Data
from .serializers import ChatDataSerializer



# Create your views here.

@api_view(['POST'])
def process_data(request):
    if request.method == 'POST':
        data = request.data
        message = data.get('user')
        response = get_response(message)
        response_message = {"answer": response}
        return Response({'assistant': response_message})
    else:
        return Response({'error': 'Only POST requests are allowed.'}, status=405)


# views.py



class JsonUploadAPIView(generics.ListCreateAPIView):
    queryset = Chat_Data.objects.all()
    serializer_class = ChatDataSerializer

    def create(self, request, *args, **kwargs):
        # Check if a file is provided in the request
        if 'json_file' not in request.data:
            return Response({"json_file": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        # Get the file from the request data
        file = request.data['json_file']

        # Check if a file with name 'intents.json' already exists
        existing_instance = Chat_Data.objects.filter(json_file='chat/jsonfile/intents.json').first()
        if existing_instance:
            existing_instance.json_file.delete()  # Delete the existing file

        # Create a new instance with the provided file
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Rename the uploaded file to 'intents.json'
        new_instance = serializer.instance
        new_instance.json_file.name = 'intents.json'
        new_instance.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

