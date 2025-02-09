from models.match_model import Match


class MatchController:
    def __init__(self, tournament):
        self.tournament = tournament

    def manage_matches(self, player1: tuple, player2: tuple):
        new_match = Match(
            match=[player1, player2]
            )
        print(f"Match demarré avec succès : {new_match}")
        return new_match
