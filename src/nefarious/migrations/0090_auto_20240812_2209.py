# Generated by Django 3.0.2 on 2024-08-12 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0089_qualityprofile_require_five_point_one'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qualityprofile',
            old_name='profile',
            new_name='quality',
        ),
    ]
