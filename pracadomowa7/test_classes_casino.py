from classes_casino import Casino, Player, NoPlayerError
from random import randint
from pytest import raises


def test_casino_add_player(monkeypatch):
    player1 = Player("Antek")
    player2 = Player("Janusz")
    player3 = Player("Kacper")
    player4 = Player("Radek")
    casino = Casino([player1, player2, player3])
    casino.add_player(player4)
    assert casino.players_list == [player1, player2, player3, player4]


def test_add_person_who_is_not_Player():
    casino = Casino()
    with raises(TypeError):
        casino.add_player('Mietek')


def test_remove_non_existing_player():
    player1 = Player('Kuba')
    player2 = Player('Gregory')
    casino = Casino([player2])
    with raises(NoPlayerError):
        casino.remove_player(player1)


def test_casino_remove_player(monkeypatch):
    player1 = Player("Antek")
    player2 = Player("Janusz")
    player3 = Player("Kacper")
    player4 = Player("Radek")
    casino = Casino([player1, player2, player3, player4])
    casino.remove_player(player3)
    assert casino.players_list == [player1, player2, player4]


def test_casino_throw_cubes(monkeypatch):
    def return_6(t, d):
        return 6
    monkeypatch.setattr("classes_casino.randint", return_6)
    player1 = Player("Antek")
    casino = Casino([player1])
    casino.throw_cubes(player1)
    assert player1.cubes == [6, 6, 6, 6]
    player1.calculate_score()
    assert casino.players_list[0].score == 36


def test_calculate_points_two_pairs(monkeypatch):
    def fake_throw_dices(casino, player):
        player.cubes = [1, 4, 4, 1]
    player = Player('Ryszard')
    casino = Casino([player])
    monkeypatch.setattr('classes_casino.Casino.throw_cubes', fake_throw_dices)
    casino.play_game()
    assert player.cubes == [1, 4, 4, 1]
    assert player.score == 10


def test_casino_player_with_odd_score(monkeypatch):
    def return_player_with_odd_score(casino, player):
        if (player.name == "Janusz"):
            player.cubes = [5, 5, 3, 3]
        else:
            player.cubes = [2, 2, 3, 3]
    monkeypatch.setattr("classes_casino.Casino.throw_cubes", return_player_with_odd_score)
    player1 = Player("Antek")
    player2 = Player("Janusz")
    player3 = Player("Kacper")
    player4 = Player("Radek")
    casino = Casino([player1, player2, player3, player4])
    casino.play_game()
    assert casino.players_list[1].score == 19
    assert casino.play_game() == player2


def test_casino_player_with_even_score(monkeypatch):
    def return_player_with_even_score(casino, player):
        if (player.name == "Janusz"):
            player.cubes = [6, 6, 2, 4]
        else:
            player.cubes = [2, 2, 3, 3]
    monkeypatch.setattr("classes_casino.Casino.throw_cubes", return_player_with_even_score)
    player1 = Player("Antek")
    player2 = Player("Janusz")
    player3 = Player("Kacper")
    player4 = Player("Radek")
    casino = Casino([player1, player2, player3, player4])
    casino.play_game()
    assert casino.players_list[1].score == 20


def test_casino_player_have_2_possible_scores(monkeypatch):
    def return_player_with_2_possible_scores(casino, player):
        if (player.name == "Janusz"):
            player.cubes = [6, 6, 6, 2]
        else:
            player.cubes = [2, 2, 3, 3]
    monkeypatch.setattr("classes_casino.Casino.throw_cubes", return_player_with_2_possible_scores)
    player1 = Player("Antek")
    player2 = Player("Janusz")
    player3 = Player("Kacper")
    player4 = Player("Radek")
    casino = Casino([player1, player2, player3, player4])
    casino.play_game()
    assert casino.players_list[1].score == 24


def test_casino_all_players_have_same_score(monkeypatch):
    def return_2(t, d):
        return 2

    monkeypatch.setattr("classes_casino.randint", return_2)
    player1 = Player("Antek")
    player2 = Player("Janusz")
    player3 = Player("Kacper")
    player4 = Player("Radek")
    casino = Casino([player1, player2, player3, player4])
    casino.play_game()
    assert player1.score == 12
    assert player2.score == 12


def test_casino_4_cubes_same_value(monkeypatch):
    def return_4_cubes_same_value_for_Janusz(casino, player):
        if (player.name == "Janusz"):
            player.cubes = [6, 6, 6, 6]
        else:
            for i in range(0, 4):
                player.cubes.append(randint(1, 6))
    monkeypatch.setattr("classes_casino.Casino.throw_cubes", return_4_cubes_same_value_for_Janusz)
    player1 = Player("Antek")
    player2 = Player("Janusz")
    player3 = Player("Kacper")
    player4 = Player("Radek")
    casino = Casino([player1, player2, player3, player4])
    assert casino.result_of_game() == "The winner is Janusz with score 36."
    assert casino.play_game() == player2
    assert player2.score == 36


def test_casino_all_even_and_two_pairs(monkeypatch):
    def fake_throw_dices(casino, player):
        player.cubes = [2, 2, 4, 4]
    player = Player('Ryszard')
    casino = Casino([player])
    monkeypatch.setattr('classes_casino.Casino.throw_cubes', fake_throw_dices)
    casino.play_game()
    assert player.cubes == [2, 2, 4, 4]
    assert player.score == 14


def test_casino_2_cubes_same_value(monkeypatch):
    def return_2_players_with_same_cubes(casino, player):
        if (player.name == "Janusz" or player.name == "Kacper"):
            player.cubes = [6, 6, 6, 5]
        else:
            player.cubes = [2, 2, 3, 3]
    monkeypatch.setattr("classes_casino.Casino.throw_cubes", return_2_players_with_same_cubes)
    player1 = Player("Antek")
    player2 = Player("Janusz")
    player3 = Player("Kacper")
    player4 = Player("Radek")
    casino = Casino([player1, player2, player3, player4])
    assert casino.play_game() is None
    assert casino.result_of_game() == "Game ended with draw."
    assert player2.score == 24
    assert player3.score == 24