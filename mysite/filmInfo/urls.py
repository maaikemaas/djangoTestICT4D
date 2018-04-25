from django.urls import path

from . import views

app_name = 'filmInfo'
urlpatterns = [
    path('', views.index, name='index'),
	path('duration/', views.duration, name='duration'),
		path('release/', views.release, name='release'),
]