from random import randint


class NoPlayerError(Exception):
    pass


class Player:
    def __init__(self, name) -> None:
        """
        Player constructor:
        :cubes: list of values on cubes player gets (list of ints)
        :score: his total score in casino (int)
        """
        self.name = name
        self.cubes = []
        self.score = 0

    def calculate_score(self):
        """Calculating players score depending on his cubes"""
        possible_scores = [0, 0]
        all_even = True
        all_odd = True
        for each_number in set(self.cubes):
            if self.cubes.count(each_number) == 4:
                possible_scores[0] += each_number*6
            elif self.cubes.count(each_number) == 3:
                possible_scores[0] += each_number*4
            elif self.cubes.count(each_number) == 2:
                possible_scores[0] += each_number*2

            if (each_number % 2 != 0):
                all_even = False
            if (each_number % 2 != 1):
                all_odd = False
        if (all_even):
            possible_scores[1] += sum(self.cubes) + 2
        elif (all_odd):
            possible_scores[1] += sum(self.cubes) + 3
        self.score = max(possible_scores)


class Casino:
    def __init__(self, players_list=None) -> None:
        """
        Casino constructor:
        :players_list: list of players participating in game
        """
        if players_list is None:
            self.players_list = []
        else:
            self.players_list = players_list

    def add_player(self, player):
        """Adds player to casino"""
        if type(player) is not Player:
            raise TypeError()
        self.players_list.append(player)

    def remove_player(self, player):
        """Remove player from casino"""
        if player not in self.players_list:
            raise NoPlayerError()
        self.players_list.remove(player)

    def play_game(self):
        """
        Plays game:
        Throw 4 cubes for every player
        After throwing cubes calculates his score depending on it
        Checks who have highest score
        Returns None if draw or the winner and his score if there
        is only one winner
        """
        winner = []
        winner_score = 0
        for player in self.players_list:
            self.throw_cubes(player)
            player.calculate_score()
            if (player.score > winner_score):
                winner_score = player.score
                winner = [player]
            elif (player.score == winner_score):
                winner.append(player)
        if (len(winner) > 1):
            return None
        else:
            return winner[0]

    def result_of_game(self):
        winner = self.play_game()
        if (winner is None):
            return "Game ended with draw."
        else:
            return f'The winner is {winner.name} with score {winner.score}.'

    def throw_cubes(self, player):
        """Throw randomized values from 1 to 6 for 4 cubes for player"""
        for _ in range(0, 4):
            player.cubes.append(randint(1, 6))