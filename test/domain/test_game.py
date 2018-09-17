from unittest import TestCase, skip

from assassin_game_csss.domain.game import Game
from assassin_game_csss.domain.game_state import GameState
from assassin_game_csss.domain.target import Target
from test.test_helper.anon import anon_item, anon_location, anon_player, anon_game


class TestGame(TestCase):
    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenPlayersArgIsNotSetOfPlayers(self):
        # Arrange
        invalid_players = {2, 3, 4}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(invalid_players, items, locations)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenItemsArgIsNotSetOfItems(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        invalid_items = {2, 3, 4}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, invalid_items, locations)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenLocationsArgIsNotSetOfLocations(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        invalid_locations = {2, 3, 4}

        # Act
        def action(): Game(players, items, invalid_locations)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenLessThanTwoPlayersProvided(self):
        # Arrange
        players = {anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations)

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenLessThanOneItemProvided(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = set()
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations)

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenLessThanOneLocationProvided(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = set()

        # Act
        def action(): Game(players, items, locations)

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenNumTargetsArgIsNotAnInt(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        # noinspection PyTypeChecker
        def action(): Game(players, items, locations, num_targets=None)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenNumTargetArgIsLessThanOne(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations, num_targets=0)

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenNumTargetArgIsNotOne(self):
        # TODO GH 2018-Sep-15: Add functionality to support multiple targets and change this test to match new behaviour
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations, num_targets=2)

        # Assert
        self.assertRaises(NotImplementedError, action)

    @skip("Not Yet Implemented")
    def test__get_status__shouldReturnCreated__whenGameJustConstructed(self):
        # Arrange
        game = anon_game()

        # Act
        actual = game.get_status()

        # Assert
        self.assertEqual(GameState.CREATED, actual)

    @skip("Not Yet Implemented")
    def test__get_status__shouldReturnStarted__whenGameHasBeenStarted(self):
        # Arrange
        game = anon_game()
        game.start()

        # Act
        actual = game.get_status()

        # Assert
        self.assertEqual(GameState.STARTED, actual)

    @skip("Not Yet Implemented")
    def test__get_status__shouldReturnEnded__whenGameHasBeenEnded(self):
        # Arrange
        game = anon_game()
        game.start()
        game.end()

        # Act
        actual = game.get_status()

        # Assert
        self.assertEqual(GameState.ENDED, actual)

    @skip("Not Yet Implemented")
    def test__get_score__shouldReturnZeroForEveryPlayer__whenGameJustCreated(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        game = anon_game(players=players)

        # Act
        actual = [game.get_score(player) for player in players]

        # Assert
        for score in actual:
            self.assertEqual(0, score)

    @skip("Not Yet Implemented")
    def test__get_score__shouldReturnOne__whenPlayerSuccessfullyKillsTarget(self):
        # Arrange
        first_player = anon_player()
        target_player = anon_player()
        target_item = anon_item()
        target_location = anon_location()
        game = anon_game(players={first_player, target_player}, items={target_item}, locations={target_location})
        game.start()
        game.confirm_kill(first_player, Target(target_player, target_item, target_location))

        # Act
        actual = game.get_score(first_player)

        # Assert
        self.assertEqual(1, actual)

    @skip("Not Yet Implemented")
    def test__get_score__shouldIncrement__whenPlayerKillsSuccessiveTargets(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player(), anon_player()})
        game.start()
        target = game.get_target(player)
        game.confirm_kill(player, target)
        target = game.get_target(player)
        game.confirm_kill(player, target)

        # Act
        actual = game.get_score(player)

        # Assert
        self.assertEqual(2, actual)
