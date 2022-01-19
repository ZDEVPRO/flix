from django.shortcuts import render
from videos.models import HomeVideos, CenterVideos, InterviewVideo
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    video_slider = HomeVideos.objects.all().order_by('-id')[:8]
    context = {
        'video_slider': video_slider,
    }
    return render(request, 'index/base.html', context)


@login_required(login_url='login')
def videos(request):
    return render(request, 'videos/base.html')


@login_required(login_url='login')
def about(request):
    return render(request, 'about/base.html')


@login_required(login_url='login')
def live(request):
    return render(request, 'live/base.html')


@login_required(login_url='login')
def privacy(request):
    return render(request, 'privacy/base.html')


@login_required(login_url='login')
def contact(request):
    return render(request, 'contact/base.html')


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile/base.html')


@login_required(login_url='login')
def video_detail(request, id, slug):
    video = HomeVideos.objects.get(pk=id)
    context = {
        'video': video,
    }
    return render(request, 'video_detail/base.html', context)


@login_required(login_url='login')
def center_detail(request, id, slug):
    center_video = CenterVideos.objects.get(pk=id)
    context = {
        'center_video': center_video,
    }
    return render(request, 'cvideo_detail/base.html', context)


@login_required(login_url='login')
def interview_detail(request, id, slug):
    in_detail = InterviewVideo.objects.get(pk=id)
    context = {
        'in_detail': in_detail,
    }
    return render(request, 'interview_detail/base.html', context)
