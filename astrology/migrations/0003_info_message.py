# Generated by Django 4.0.4 on 2022-05-24 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrology', '0002_info_email_info_name_info_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='message',
            field=models.TextField(max_length=64, null=True),
        ),
    ]