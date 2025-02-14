# Generated by Django 3.2.25 on 2024-11-17 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_alter_book_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='uid',
            field=models.SlugField(default=None, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.SlugField(default=None, max_length=200, null=True)),
                ('content', models.TextField(max_length=200)),
                ('stars', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('hidden', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('review_of', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='products.book')),
            ],
        ),
    ]
