# Generated by Django 5.1.3 on 2024-11-26 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_review_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='stars',
        ),
    ]
