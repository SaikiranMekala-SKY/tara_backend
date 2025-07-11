# Generated by Django 5.0.4 on 2025-06-26 14:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usermanagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=50)),
                ('category_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('yet to be started', 'Yet to be Started'), ('in progress', 'In Progress'), ('completed', 'Completed'), ('sent for approval', 'Sent for Approval'), ('revoked', 'Revoked')], default='in progress', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateField(default=None, null=True)),
                ('priority', models.CharField(choices=[('critical', 'Critical'), ('medium', 'Medium'), ('low', 'Low'), ('high', 'High')], default='low', max_length=20)),
                ('completion_percentage', models.IntegerField(default=0)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_service_tasks', to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_service_tasks', to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_service_tasks', to=settings.AUTH_USER_MODEL)),
                ('service_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_tasks', to='usermanagement.servicerequest')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceSubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='servicetasks.servicetask')),
            ],
        ),
    ]
