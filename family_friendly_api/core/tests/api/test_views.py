from unittest.mock import patch

from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from family_friendly_api.core.factories import UserFactory
from family_friendly_api.core.factories import WatchlistFactory
from family_friendly_api.core.models import Movie


class MovieViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()

    @patch("requests.get")
    def test_family_friendly_movies(self, mock_get):
        # Setup mock
        mock_response = {
            "results": [
                {
                    "tmdb_id": 1,
                    "title": "Test Movie",
                    "overview": "Test overview",
                    "release_date": "2021-01-01",
                },
            ],
            "total_results": 1,
            "total_pages": 1,
            "page": 1,
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("api:movies-family-friendly"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["title"], "Test Movie")


class WatchlistViewSetTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.watchlist = WatchlistFactory(user=self.user)

    @patch("requests.get")
    def test_add_movie_to_watchlist(self, mock_get):
        mock_movie_data = {
            "tmdb_id": 123,
            "title": "Mocked Movie",
            "overview": "Some overview",
            "release_date": "2022-12-12",
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_movie_data

        response = self.client.post(
            reverse(
                "api:watchlists-add-movie",
                kwargs={"pk": self.watchlist.pk, "tmdb_id": 123},
            ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Movie.objects.filter(tmdb_id=123).exists())
        self.assertTrue(Movie.objects.get(tmdb_id=123) in self.watchlist.movies.all())
