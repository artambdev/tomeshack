# Generated by Django 5.1.3 on 2025-01-09 18:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_email', models.EmailField(max_length=254)),
                ('uid', models.SlugField(default=None, max_length=200, null=True)),
                ('name', models.TextField(max_length=30)),
                ('title', models.TextField(max_length=50)),
                ('content', models.TextField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('resolved', models.BooleanField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tickets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicketResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.SlugField(default=None, max_length=200, null=True)),
                ('content', models.TextField(max_length=400)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('responder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_responses', to=settings.AUTH_USER_MODEL)),
                ('response_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='support.ticket')),
            ],
        ),
    ]
