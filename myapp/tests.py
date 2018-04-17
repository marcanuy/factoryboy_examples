from django.test import TestCase

from myapp.factories import TeamFactory, PlayerFactory, TeamWithPlayersFactory
from myapp.models import Team, Player

class FactoriesTests(TestCase):
    
    def test_create_players_with_same_team(self):
        team = TeamFactory.create()
        player1 = PlayerFactory.create(team=team)
        player2 = PlayerFactory.create(team=team)

        self.assertIsInstance(player1, Player)
        self.assertIsInstance(player2, Player)
        self.assertEqual(player1.team, team)
        self.assertEqual(player2.team, team)

    def test_create_players_with_different_teams(self):

        player1 = PlayerFactory.create()
        player2 = PlayerFactory.create()

        self.assertIsInstance(player1, Player)
        self.assertIsInstance(player2, Player)
        self.assertNotEqual(player1.team, player2.team)

    def test_create_team_with_players(self):
        team = TeamWithPlayersFactory.create()
        
        self.assertIsInstance(team, Team)
        players = team.players.all()
        self.assertTrue(len(players) > 0)
        for player in players:
            self.assertIsInstance(player, Player)
        
