# Generated by Django 4.2.5 on 2023-10-09 11:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_rating'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rating',
            new_name='MovieRating',
        ),
    ]
