# Generated by Django 3.2.16 on 2023-01-06 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_music_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='image',
            new_name='img',
        ),
    ]