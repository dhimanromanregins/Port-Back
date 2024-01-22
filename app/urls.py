from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, MentorViewSet,  ProjectViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'mentor', MentorViewSet, basename='mentor')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]