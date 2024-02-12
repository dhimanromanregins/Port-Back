from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, CategoryViewSet,MentorViewSet,  ProjectViewSet, ProjectsViewSet,DisplayImageViewSet, TestmonialsViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'mentor', MentorViewSet, basename='mentor')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'project-display', ProjectsViewSet, basename='Project-display')
router.register(r'testmonials', TestmonialsViewSet, basename='testmonials')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
