from models.match_model import Match
from typing import Tuple


class MatchController:
    def __init__(self, tournament):
        self.tournament = tournament

    def manage_matches(self, player1: Tuple[str, float], player2: Tuple[str, float]):
        new_match = Match(
            match=([player1], [player2])
        )
        print(f"Match créé avec succès : {new_match}")
        return new_match
