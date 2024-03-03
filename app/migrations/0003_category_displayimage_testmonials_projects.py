# Generated by Django 5.0.2 on 2024-03-03 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mentorship_project_planner_alter_contact_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
                ('category_description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='category/')),
            ],
        ),
        migrations.CreateModel(
            name='DisplayImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='display-images/')),
            ],
        ),
        migrations.CreateModel(
            name='Testmonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='testimonials/')),
                ('description', models.TextField(max_length=1000)),
                ('Mentored_for', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=250)),
                ('project_description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='projects/')),
                ('project_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]