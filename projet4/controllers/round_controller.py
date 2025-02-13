from views.round_view import RoundView
from models.round_model import Round
from models.tournament_model import Tournament
from controllers.match_controller import MatchController
from typing import Tuple
from datetime import datetime
import random


class RoundController:
    MATCH_NULL_SCORE = 0.5
    MATCH_WIN_SCORE = 1.0
    MATCH_LOOSE_SCORE = 0.0
    SCORE_MAPPING = {
        0: (MATCH_NULL_SCORE, MATCH_NULL_SCORE),
        1: (MATCH_WIN_SCORE, MATCH_LOOSE_SCORE),
        2: (MATCH_LOOSE_SCORE, MATCH_WIN_SCORE)
    }

    def __init__(self, view: RoundView, tournament: Tournament):
        self.view = RoundView()
        self.tournament = tournament

    def manage_rounds(self) -> list:
        rounds = []
        for i in range(1, self.tournament.roundNumber + 1):
            print(f"Round {i} started")
            if i == 1:
                players = self.tournament.playerList.copy()
                random.shuffle(players)
            else:
                players = self.tournament.playerList
            if len(players) >= 2:
                # call here pair_players method
                player1_selected = players[0]
                player2_selected = players[1]
                player1 = (player1_selected['chess_id'], 0.0)
                player2 = (player2_selected['chess_id'], 0.0)

                winner = None
                while winner not in self.SCORE_MAPPING:
                    winner = int(input(f"Player 1 : {player1_selected['first_name']} {player1_selected['last_name']}"
                                       f" VS "
                                       f"Player 2 : {player2_selected['first_name']} {player2_selected['last_name']}"
                                       f"\nWho is the winner ? 0 (if null), 1 or 2 : ").strip())
                    if winner in self.SCORE_MAPPING:
                        player1_score, player2_score = self.SCORE_MAPPING[winner]
                        player1 = (player1_selected['chess_id'], float(player1_score))
                        player2 = (player2_selected['chess_id'], float(player2_score))
                    else:
                        print("invalid input : fill 0 (if null), 1 or 2")

            else:
                print("Not enough players to start a match")
                break
            match = self.new_match(player1, player2)
            round = Round(
                number=i,
                name=f"Round {i}",
                matchList=[match.model_dump()]
                )

            round.endDate = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            rounds.append(round.model_dump())
        print("Rounds finished!")
        return rounds

    def new_match(self, player1: Tuple[str, float], player2: Tuple[str, float]):
        match_controller = MatchController(self.tournament)
        return match_controller.manage_matches(player1, player2)

    def pair_players(self):
        # Triez tous les joueurs en fonction de leur nombre total de points dans le tournoi.
        # Associez les joueurs dans l’ordre (le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4
        # Si plusieurs joueurs ont le même nombre de points, vous pouvez les choisir de façon aléatoire.
        # Lors de la génération des paires, évitez de créer des matchs identiques
        # (c’est-à-dire les mêmes joueurs jouant plusieurs fois l’un contre l’autre).
        # Par exemple, si le joueur 1 a déjà joué contre le joueur 2,associez-le plutôt au joueur 3.
        pass
