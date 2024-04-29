from django.test import TestCase

from family_friendly_api.core.api.serializers import MovieSerializer
from family_friendly_api.core.api.serializers import WatchlistSerializer
from family_friendly_api.core.factories import MovieFactory
from family_friendly_api.core.factories import WatchlistFactory


class MovieSerializerTest(TestCase):
    def test_movie_serializer(self):
        movie = MovieFactory()
        serializer = MovieSerializer(movie)
        data = serializer.data
        self.assertEqual(data["title"], movie.title)
        self.assertEqual(data["overview"], movie.overview)
        self.assertEqual(data["release_date"], movie.release_date.isoformat())


class WatchlistSerializerTest(TestCase):
    def test_watchlist_serializer(self):
        watchlist = WatchlistFactory()
        serializer = WatchlistSerializer(watchlist)
        data = serializer.data
        self.assertEqual(data["user"], watchlist.user.id)
        self.assertIsInstance(data["movies"], list)
