from django.contrib import admin

from .models import Movie
from .models import Watchlist

admin.site.register(Movie)
admin.site.register(Watchlist)
