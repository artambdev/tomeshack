# Generated by Django 5.1.3 on 2025-01-07 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(default=12345, max_length=16),
            preserve_default=False,
        ),
    ]
