from django.db import models
from mptt.models import MPTTModel
from django.utils.safestring import mark_safe
from django.urls import reverse


class Years(models.Model):
    years = models.CharField(max_length=40)
    create_time = models.TimeField(auto_now=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.years

    class Meta:
        verbose_name = "Video Yillari"
        verbose_name_plural = "Video Yillari"


class Authors(models.Model):
    fullname = models.CharField(max_length=100)
    create_time = models.TimeField(auto_now=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Aftor"
        verbose_name_plural = "Aftor"


class HomeVideos(models.Model):
    STATUS = (
        ('True', 'Yoniq'),
        ('False', 'O`chiq'),

    )
    CONDITION = (
        ('Tavsiya Etiladi', 'Tavsiya Etiladi'),
        ('Mashxur', 'Mashxur'),
        ('Eng yangi', 'Eng yangi'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name="Author")
    years = models.ForeignKey(Years, on_delete=models.CASCADE, related_name="Years")
    status = models.CharField(max_length=50, choices=STATUS)
    condition = models.CharField(max_length=50, choices=CONDITION)
    video = models.FileField(upload_to='video/', null=True)
    image = models.ImageField(upload_to='images/', null=True)
    poster_image = models.ImageField(upload_to='images/poster/', null=True, blank=True)
    create_time = models.TimeField(auto_now=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Home Video"
        verbose_name_plural = 'Home Video'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'self': self.slug})


class CenterVideos(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name="Authors")
    years = models.ForeignKey(Years, on_delete=models.CASCADE, related_name="Year")
    image = models.ImageField(upload_to='images/', null=True)
    poster_image = models.ImageField(upload_to='images/poster/', null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True)
    create_time = models.TimeField(auto_now=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Center Video"
        verbose_name_plural = 'Center Video'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'self': self.slug})


class InterviewVideo(models.Model):
    title = models.CharField(max_length=201)
    slug = models.SlugField(null=False, unique=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/Interview', null=True)
    poster_image = models.ImageField(upload_to='images/poster/Interview', null=True, blank=True)
    video = models.FileField(upload_to='video/Interview', null=True)
    create_time = models.TimeField(auto_now=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Interview Video"
        verbose_name_plural = 'Interview Video'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'self': self.slug})
