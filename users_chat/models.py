from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)


class Rooms(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            token = get_random_string(length=6)  # Change the length as needed
            self.slug = f"{base_slug}-{token}"

            # Ensure the slug is unique
            if Rooms.objects.filter(slug=self.slug).exists():
                count = 1
                while Rooms.objects.filter(slug=self.slug).exists():
                    self.slug = f"{base_slug}-{token}-{count}"
                    count += 1

        super(Rooms, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender_username = models.CharField(max_length=255)
    reciever_username = models.CharField(max_length=25)
    content = models.TextField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    read_message = models.BooleanField(default=False)


    def __str__(self):
        return "Message is :- "+ self.content
