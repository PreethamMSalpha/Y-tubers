# Generated by Django 3.2.9 on 2021-11-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_url',
            field=models.CharField(default='www.google.com', max_length=255),
            preserve_default=False,
        ),
    ]