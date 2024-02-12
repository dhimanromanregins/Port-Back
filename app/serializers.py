from rest_framework import serializers
from .models import Contact, Mentorship,category,Project_Planner,Projects,DisplayImage, Testmonials

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Planner
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class DisplayImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayImage
        fields = '__all__'

class TestmonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testmonials
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
