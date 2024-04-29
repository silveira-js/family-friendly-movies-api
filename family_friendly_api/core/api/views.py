import requests
from django.conf import settings
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from family_friendly_api.core.models import Movie
from family_friendly_api.core.models import Watchlist

from .pagination import TMDbPagination
from .serializers import MovieSerializer
from .serializers import WatchlistSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False, methods=["get"])
    def family_friendly(self, request):
        page = request.query_params.get("page", 1)
        query_params = {
            "api_key": settings.TMDB_API_KEY,
            "language": "en-US",
            "include_adult": "false",
            "with_genres": "10751",
            "page": page,
        }
        response = requests.get(
            "https://api.themoviedb.org/3/discover/movie",
            params=query_params,
        )
        if response.status_code == 200:
            pagination = TMDbPagination()
            paginated_data = pagination.paginate_queryset(
                response.json(),
                request,
                self,
            )
            if paginated_data is not None:
                return pagination.get_paginated_response(paginated_data)
            return Response(response.json()["results"])
        return Response(
            {"error": "Failed to fetch data from TMDb"}, status=response.status_code
        )


class WatchlistViewSet(viewsets.ModelViewSet):
    serializer_class = WatchlistSerializer

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)

    @action(detail=True, methods=["post"], url_path="add_movie/(?P<tmdb_id>[^/.]+)")
    def add_movie(self, request, tmdb_id, pk=None):
        movie, created = Movie.objects.get_or_create(tmdb_id=tmdb_id)
        if created:
            movie_data = requests.get(
                f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={settings.TMDB_API_KEY}"
            ).json()
            movie.title = movie_data.get("title")
            movie.overview = movie_data.get("overview")
            movie.release_date = movie_data.get("release_date")
            movie.save()
        watchlist = self.get_object()
        watchlist.movies.add(movie)
        return Response({"status": "Movie added to watchlist"})

    @action(detail=True, methods=["post"], url_path="remove_movie/(?P<tmdb_id>[^/.]+)")
    def remove_movie(self, request, tmdb_id, pk=None):
        movie = Movie.objects.get(tmdb_id=tmdb_id)
        watchlist = self.get_object()
        watchlist.movies.remove(movie)
        return Response({"status": "Movie removed from watchlist"})
