# Generated by Django 3.0.2 on 2021-08-29 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0064_watchtvshow_quality_profile_custom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchtvepisode',
            name='quality_profile_custom',
        ),
        migrations.RemoveField(
            model_name='watchtvseason',
            name='quality_profile_custom',
        ),
    ]
