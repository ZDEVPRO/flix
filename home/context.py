from videos.models import HomeVideos, Authors, Years, CenterVideos, InterviewVideo


def videos(request):
    videos_slider = HomeVideos.objects.all().order_by('-id')[:10]
    context = {
        'videos_slider': videos_slider,
    }
    return context


def authors(request):
    author = Authors.objects.all().order_by('id')[:100]
    context = {
        'author': author,
    }
    return context


def years(request):
    year = Years.objects.all().order_by('id')[:20]
    context = {
        'year': year,
    }
    return context


def centervideos(request):
    center_video = CenterVideos.objects.all().order_by('-id')[:10000]
    context = {
        'center_video': center_video,
    }
    return context


def intervideo(request):
    in_video = InterviewVideo.objects.all().order_by('-id')[:25]
    context = {
        'in_video': in_video,
    }
    return context
