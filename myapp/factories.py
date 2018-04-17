import factory
import myapp
from . import models

class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Team

    name = factory.Faker('sentence', nb_words=3, variable_nb_words=True)

class TeamWithPlayersFactory(TeamFactory):
    
    @factory.post_generation
    def players(obj, create, extracted, **kwargs):
        """
        If called like: TeamFactory(players=4) it generates a Team with 4
        players.  If called without `players` argument, it generates a
        random amount of players for this team
        """
        if not create:
            # Build, not create related
            return

        if extracted:
            for n in range(extracted):
                myapp.factories.PlayerFactory(team=obj)
        else:
            import random
            number_of_units = random.randint(1, 10)
            for n in range(number_of_units):
                myapp.factories.PlayerFactory(team=obj)


class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Player

    team = factory.SubFactory(TeamFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


