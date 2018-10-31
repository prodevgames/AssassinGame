from unittest import TestCase

from assassin_game_csss.domain.player import Player
from test.test_helper.anon import anon_player


class TestPlayer(TestCase):

    def test__constructor__shouldThrowException__whenGivenNonString(self):
        # Act
        # noinspection PyTypeChecker
        def action_none(): Player(None)

        # noinspection PyTypeChecker
        def action_int(): Player(42)

        # noinspection PyTypeChecker
        def action_set(): Player(set())

        # noinspection PyTypeChecker
        def action_list(): Player([])

        # Assert
        self.assertRaises(TypeError, action_none)
        self.assertRaises(TypeError, action_int)
        self.assertRaises(TypeError, action_set)
        self.assertRaises(TypeError, action_list)

    def test__constructor__shouldThrowException__whenProvidedEmptyString(self):
        # Act
        def action(): Player("")

        # Assert
        self.assertRaises(ValueError, action)

    def test__name__shouldReturnName_whenAccessing(self):
        # Arrange
        expected_name = "Test Name"
        player = Player(expected_name)

        # Act
        actual = player.name

        # Assert
        self.assertEqual(expected_name, actual)

    def test__name__shouldThrowException__whenAttemptingToSet(self):
        # Arrange
        player = anon_player()

        # Act
        # noinspection PyPropertyAccess
        def action(): player.name = "New Name"

        # Assert
        self.assertRaises(AttributeError, action)

    def test__equals__shouldReturnTrue__whenConstructionIsIdentical(self):
        # Arrange
        player_a = Player("Identical Name")
        player_b = Player("Identical Name")

        # Act
        actual = (player_a == player_b)

        # Assert
        self.assertTrue(actual)

    def test__equals__shouldReturnFalse__whenConstructionIsDifferent(self):
        # Arrange
        player_a = Player("Not Player B")
        player_b = Player("Not Player A")

        # Act
        actual = (player_a == player_b)

        # Assert
        self.assertFalse(actual)

    def test__hash__shouldConsiderInstancesIdentical__whenConstructionIsIdentical(self):
        # Arrange
        player_a = Player("Identical Name")
        player_b = Player("Identical Name")
        players = {player_a}

        # Act
        players.add(player_b)

        # Assert
        self.assertEqual(1, len(players))

    def test__hash__shouldConsiderInstancesDifferent__whenConstructionIsDifferent(self):
        # Arrange
        player_a = Player("Not Player B")
        player_b = Player("Not Player A")
        players = {player_a}

        # Act
        players.add(player_b)

        # Assert
        self.assertEqual(2, len(players))
