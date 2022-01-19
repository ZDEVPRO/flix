from django.contrib import admin
from videos.models import HomeVideos, Authors, Years, CenterVideos, InterviewVideo


class HomeVideosAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'image_tag']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}


class CenterVideosAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'image_tag']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}


class InterViewAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'create_time', 'create_date']


class YearsAdmin(admin.ModelAdmin):
    list_display = ['years', 'create_time', 'create_date']


admin.site.register(Years, YearsAdmin)
admin.site.register(CenterVideos, CenterVideosAdmin)
admin.site.register(InterviewVideo, InterViewAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(HomeVideos, HomeVideosAdmin)
