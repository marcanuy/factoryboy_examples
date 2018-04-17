from django.db import models

class Player(models.Model):
    """
    Model representing a player of a team
    """
    team = models.ForeignKey(
        'team', # class name
        on_delete=models.CASCADE,
        related_name='players'
    )
    first_name = models.CharField(max_length=200, help_text="Player's first name")
    last_name = models.CharField(max_length=200, help_text="Player's last name")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Team(models.Model):
    """ 
    Model representing a text Team.
    """
    name = models.CharField(max_length=200, help_text="Team name")

    def __str__(self):
        return self.name
