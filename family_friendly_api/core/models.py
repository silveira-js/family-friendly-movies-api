from django.db import models

from family_friendly_api.users.models import User


class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Watchlist(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="watchlist",
    )
    movies = models.ManyToManyField(Movie, related_name="watchlists")

    def __str__(self):
        return f"{self.user.username}'s Watchlist"
