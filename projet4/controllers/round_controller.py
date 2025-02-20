from views.round_view import RoundView
from models.round_model import Round
from models.tournament_model import Tournament
from models.player_model import Player
from controllers.match_controller import MatchController
from datetime import datetime
import random


class RoundController:

    def __init__(self, tournament: Tournament, round_number: int):
        self.round = Round(number=round_number)
        self.view = RoundView(self.round)
        self.tournament = tournament

    def manage_round(self):
        self.view.start_round()
        players = []
        if self.round.number == 1:
            players = self.tournament.playerList.copy()
            random.shuffle(players)
        else:
            # call here pair_players method
            players = self.tournament.playerList
        self.start_matches(players)
        self.round.endDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self.round.model_dump()

    def start_matches(self, players: list):
        for i in range(self.match_count()):
            print(f"Match {i + 1} sur {self.match_count()}")
            player1 = players.pop()
            player2 = players.pop()
            match = self.new_match(player1, player2)
            match.play_match()

    def new_match(self, player1: Player, player2: Player) -> MatchController:
        match_controller = MatchController(self.tournament, player1, player2)
        self.round.matchList.append(match_controller)
        return match_controller

    def pair_players(self):
        # Triez tous les joueurs en fonction de leur nombre total de points dans le tournoi.
        # Associez les joueurs dans l’ordre (le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4
        # Si plusieurs joueurs ont le même nombre de points, vous pouvez les choisir de façon aléatoire.
        # Lors de la génération des paires, évitez de créer des matchs identiques
        # (c’est-à-dire les mêmes joueurs jouant plusieurs fois l’un contre l’autre).
        # Par exemple, si le joueur 1 a déjà joué contre le joueur 2,associez-le plutôt au joueur 3.
        pass

    def match_count(self) -> int:
        return int((len(self.tournament.playerList) + 1) / 2)
