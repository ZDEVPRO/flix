from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),

    path('videos/', views.videos, name='videos'),
    path('about/', views.about, name='about'),
    path('live/', views.live, name='live'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('video/<int:id>/<slug:slug>', views.video_detail, name='video_detail'),
    path('center_detail/<int:id>/<slug:slug>', views.center_detail, name='center_detail'),
    path('interview_detail/<int:id>/<slug:slug>', views.interview_detail, name='interview_detail'),
]
