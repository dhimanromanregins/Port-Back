# models.py
from django.db import models
import os

class Chat_Data(models.Model):
    json_file = models.FileField(upload_to="chat/jsonfile/")