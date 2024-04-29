import datetime

import factory
import factory.fuzzy

from family_friendly_api.core.models import Movie
from family_friendly_api.core.models import Watchlist
from family_friendly_api.users.factories import UserFactory


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    tmdb_id = factory.Sequence(lambda n: n)
    title = factory.Faker("sentence", nb_words=4)
    overview = factory.Faker("paragraph", nb_sentences=3)
    release_date = factory.fuzzy.FuzzyDate(start_date=datetime.date(2000, 1, 1))


class WatchlistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Watchlist

    user = factory.SubFactory(UserFactory)
