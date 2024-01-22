# yourappname/views.py
from rest_framework import viewsets
from .models import Contact, Mentorship,Project_Planner
from .serializers import ContactSerializer, MentorSerializer,ProjectSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all()
    serializer_class = MentorSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project_Planner.objects.all()
    serializer_class = ProjectSerializer


