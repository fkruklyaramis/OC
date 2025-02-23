from views.round_view import RoundView
from models.round_model import Round
from models.tournament_model import Tournament
from models.player_model import Player
from controllers.match_controller import MatchController
from datetime import datetime
import random


class RoundController:

    def __init__(self, tournament: Tournament, round_number: int):
        self.tournament = tournament
        self.round = Round(number=round_number)
        self.round.name = f"Round {round_number}"
        self.view = RoundView(self.round)
        self.tournament = tournament

    def manage_round(self):
        self.view.start_round()
        players = []
        if self.round.number == 1:
            # randomize players for firdst round
            random.shuffle(self.tournament.playerList)
            players = self.tournament.playerList
        else:
            # call matching player method
            players = self.pair_players()
        self.start_matches(players)
        self.round.endDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self.round.model_dump()

    def start_matches(self, players: list):
        match_count = self.match_count()

        # Utiliser la même méthode pour calculer les scores
        player_scores = self.calculate_player_scores()

        # players are paired two by two, getting the first and second player
        for i in range(0, len(players), 2):
            print(f"Match {(i//2) + 1} sur {match_count}")

            player1 = players[i]
            player2 = players[i + 1]

            # Show current scores before match
            print(f"{player1.first_name} {player1.last_name} (Score total: {player_scores.get(player1.chess_id, 0)})")
            print(f"{player2.first_name} {player2.last_name} (Score total: {player_scores.get(player2.chess_id, 0)})")

            match = self.new_match(player1, player2)
            result = match.play_match()
            self.round.matchList.append(result)

    def new_match(self, player1: Player, player2: Player) -> MatchController:
        match_controller = MatchController(self.tournament, player1, player2)
        return match_controller

    def match_count(self) -> int:
        return int((len(self.tournament.playerList) + 1) / 2)

    def pair_players(self):
        player_scores = self.calculate_player_scores()

        # ranking players by score
        sorted_players = sorted(
            self.tournament.playerList,
            key=lambda p: (player_scores.get(p.chess_id, 0), random.random()),
            reverse=True
        )

        # create pairs of players that have not played together
        paired_players = []
        used_players_ids = set()

        for player1 in sorted_players:
            if player1.chess_id in used_players_ids:
                continue

            # Recherche d'un adversaire pour player1
            for player2 in sorted_players:
                if (player2.chess_id not in used_players_ids and player1.chess_id != player2.chess_id
                   and not self.have_played_together(player1, player2)):

                    paired_players.extend([player1, player2])
                    used_players_ids.add(player1.chess_id)
                    used_players_ids.add(player2.chess_id)
                    break

        return paired_players

    def have_played_together(self, player1: Player, player2: Player) -> bool:
        for round_data in self.tournament.roundList:
            for match in round_data.get('matchList', []):
                match_data = match.get('match', [])
                p1 = match_data[0][0]
                p2 = match_data[1][0]

                if ((p1.chess_id == player1.chess_id and p2.chess_id == player2.chess_id) or (
                     p1.chess_id == player2.chess_id and p2.chess_id == player1.chess_id)):
                    return True
        return False

    def calculate_player_scores(self) -> dict:
        # Calculate player scores from previous rounds
        player_scores = {}
        if not self.tournament.roundList:
            return player_scores

        for round_data in self.tournament.roundList:
            for match in round_data.get('matchList', []):
                match_data = match.get('match', [])

                player1 = match_data[0][0]
                score1 = match_data[0][1]
                player2 = match_data[1][0]
                score2 = match_data[1][1]

                player_scores[player1.chess_id] = player_scores.get(player1.chess_id, 0) + score1
                player_scores[player2.chess_id] = player_scores.get(player2.chess_id, 0) + score2

        return player_scores
