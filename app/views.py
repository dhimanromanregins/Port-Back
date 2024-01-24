# yourappname/views.py
from rest_framework import viewsets
from .models import Contact, Mentorship,Project_Planner,Projects,DisplayImage, Testmonials
from .serializers import ContactSerializer, MentorSerializer,ProjectSerializer,ProjectsSerializer, DisplayImageSerializer, TestmonialsSerializer

class ContactViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class MentorViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Mentorship.objects.all()
    serializer_class = MentorSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Project_Planner.objects.all()
    serializer_class = ProjectSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class DisplayImageViewSet(viewsets.ModelViewSet):
    queryset = DisplayImage.objects.all()
    serializer_class = DisplayImageSerializer


class TestmonialsViewSet(viewsets.ModelViewSet):
    queryset = Testmonials.objects.all()
    serializer_class = TestmonialsSerializer

