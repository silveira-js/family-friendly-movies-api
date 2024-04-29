from rest_framework import serializers

from family_friendly_api.core.models import Movie
from family_friendly_api.core.models import Watchlist


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["tmdb_id", "title", "overview", "release_date"]


class WatchlistSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Watchlist
        fields = ["user", "movies"]
