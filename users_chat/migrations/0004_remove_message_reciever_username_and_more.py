# Generated by Django 4.2.11 on 2024-03-07 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_chat', '0003_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='reciever_username',
        ),
        migrations.AddField(
            model_name='message',
            name='receiver_username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL, to_field='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
