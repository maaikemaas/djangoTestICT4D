from django.shortcuts import render, get_object_or_404

from .models import FilmInfo
	
def index(request):
    filmInfo_list = FilmInfo.objects.all()
    context = {'filmInfo_list': filmInfo_list}
    return render(request, 'filmInfo/index.html', context)
	

def duration(request):
    filmInfo_list = FilmInfo.objects.order_by('-duration')
    context = {'filmInfo_list': filmInfo_list}
    return render(request, 'filmInfo/duration.html', context)

	
def release(request):
    filmInfo_list = FilmInfo.objects.order_by('-releaseDate')
    context = {'filmInfo_list': filmInfo_list}
    return render(request, 'filmInfo/release.html', context)	
