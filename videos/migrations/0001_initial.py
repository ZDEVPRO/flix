# Generated by Django 4.0.1 on 2022-01-15 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('create_time', models.TimeField(auto_now=True)),
                ('create_date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Domlalar',
                'verbose_name_plural': 'Domlalar',
            },
        ),
        migrations.CreateModel(
            name='InterviewVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=201)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(null=True, upload_to='images/Interview')),
                ('poster_image', models.ImageField(blank=True, null=True, upload_to='images/poster/Interview')),
                ('video', models.FileField(null=True, upload_to='video/Interview')),
                ('create_time', models.TimeField(auto_now=True)),
                ('create_date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Interview Video',
                'verbose_name_plural': 'Interview Video',
            },
        ),
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.CharField(max_length=40)),
                ('create_time', models.TimeField(auto_now=True)),
                ('create_date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Video Yillari',
                'verbose_name_plural': 'Video Yillari',
            },
        ),
        migrations.CreateModel(
            name='HomeVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('True', 'Yoniq'), ('False', 'O`chiq')], max_length=50)),
                ('condition', models.CharField(choices=[('Tavsiya Etiladi', 'Tavsiya Etiladi'), ('Mashxur', 'Mashxur'), ('Eng yangi', 'Eng yangi')], max_length=50)),
                ('video', models.FileField(null=True, upload_to='video/')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('poster_image', models.ImageField(blank=True, null=True, upload_to='images/poster/')),
                ('create_time', models.TimeField(auto_now=True)),
                ('create_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Author', to='videos.authors')),
                ('years', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Years', to='videos.years')),
            ],
            options={
                'verbose_name': 'Home Video',
                'verbose_name_plural': 'Home Video',
            },
        ),
        migrations.CreateModel(
            name='CenterVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('poster_image', models.ImageField(blank=True, null=True, upload_to='images/poster/')),
                ('video', models.FileField(null=True, upload_to='video/')),
                ('create_time', models.TimeField(auto_now=True)),
                ('create_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Authors', to='videos.authors')),
                ('years', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Year', to='videos.years')),
            ],
            options={
                'verbose_name': 'Center Video',
                'verbose_name_plural': 'Center Video',
            },
        ),
    ]