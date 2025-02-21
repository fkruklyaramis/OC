from models.match_model import Match
from models.player_model import Player
from views.match_view import MatchView


class MatchController:
    def __init__(self, tournament, player1: Player, player2: Player):
        self.tournament = tournament
        self.view = MatchView
        self.match = Match(
            match=([player1, 0], [player2, 0])
        )

    def play_match(self):
        result = self.view.play_match(self.match)
        self.match.match[0][1] = result[0]
        self.match.match[1][1] = result[1]
        return self.match.model_dump()
