import factory

from family_friendly_api.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    name = factory.Faker("name")

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        password = extracted if extracted else "testpass"
        self.set_password(password)
        if create:
            self.save()
