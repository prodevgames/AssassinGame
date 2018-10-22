from unittest import TestCase, skip

from assassin_game_csss.domain.player import Player
from test.test_helper.anon import anon_player


class TestPlayer(TestCase):
    def test__constructor__shouldThrowException__whenProvidedNone(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Player(None)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedInt(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Player(3)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedFloat(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Player(3.4)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedDict(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Player({"a": 2})

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedList(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Player([1, 2])

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedEmptyString(self):
        # Act
        def action(): Player("")

        # Assert
        self.assertRaises(ValueError, action)

    def test__get_name__shouldReturnName(self):
        # Arrange
        expected_name = "Test Name"
        player = Player(expected_name)

        # Act
        actual = player.get_name()

        # Assert
        self.assertEqual(expected_name, actual)

    @skip
    def test__name__shouldReturnName_whenAccessing(self):
        # Arrange
        expected_name = "Test Name"
        player = Player(expected_name)

        # Act
        actual = player.name

        # Assert
        self.assertEqual(expected_name, actual)

    @skip
    def test__name__shouldThrowException__whenAttemptingToSet(self):
        # Arrange
        player = anon_player()

        # Act
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

    def test__equals__shouldConsiderInstancesIdentical__whenConstructionIsIdentical(self):
        # Arrange
        player_a = Player("Identical Name")
        player_b = Player("Identical Name")
        players = {player_a}

        # Act
        players.add(player_b)

        # Assert
        self.assertEqual(1, len(players))

    def test__equals__shouldConsiderInstancesDifferent__whenConstructionIsDifferent(self):
        # Arrange
        player_a = Player("Not Player B")
        player_b = Player("Not Player A")
        players = {player_a}

        # Act
        players.add(player_b)

        # Assert
        self.assertEqual(2, len(players))
