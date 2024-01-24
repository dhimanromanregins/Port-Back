from django.contrib import admin
from .models import Contact, Project_Planner, Mentorship
# Register your models here.

admin.site.register((Contact, Project_Planner, Mentorship))
