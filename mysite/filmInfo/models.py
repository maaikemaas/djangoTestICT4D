import datetime

from django.db import models
from django.utils import timezone

class FilmInfo(models.Model):
    filmTitle = models.CharField(max_length=300)
    duration = models.IntegerField(default=1)
    director = models.CharField(max_length=150)
    releaseDate = models.IntegerField(default=00)
	
    def __str__(self):
        return self.filmTitle
		
     def was_released_before_2000(self):
         return releaseDate < 2000