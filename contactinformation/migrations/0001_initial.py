# Generated by Django 3.2.9 on 2021-11-13 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('insta_link', models.CharField(max_length=255)),
                ('fb_link', models.CharField(max_length=255)),
                ('twitter_link', models.CharField(max_length=255)),
                ('youtube_link', models.CharField(max_length=255)),
                ('created_date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]