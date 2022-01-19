# Generated by Django 4.0.1 on 2022-01-19 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_alter_authors_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='centervideos',
            name='description',
            field=models.TextField(default='This is description', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homevideos',
            name='description',
            field=models.TextField(default='This is center description', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interviewvideo',
            name='description',
            field=models.TextField(default='This is interview description', max_length=500),
            preserve_default=False,
        ),
    ]