from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.TextField(max_length=1000)


class Mentorship(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    story = models.TextField(max_length=1000)
    membership_type = models.CharField(max_length=100)
    desired_outcome = models.CharField(max_length=100)



class Project_Planner(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    project_type = models.CharField(max_length=250)
    budget = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)