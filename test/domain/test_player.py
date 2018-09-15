from unittest import TestCase
from unittest import skip

from assassin_game_csss.domain.player import Player


class TestPlayer(TestCase):
    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedNone(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Player(None)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedInt(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Player(3)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedFloat(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Player(3.4)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedDict(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Player(3)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedList(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Player(3)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedEmptyString(self):
        # Act
        def action(): Player("")

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__get_name__shouldReturnName(self):
        expected_name = "Test Name"
        player = Player(expected_name)
        self.assertEqual(expected_name, player.get_name())

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnTrue__whenConstructionIsIdentical(self):
        # Arrange
        player_a = Player("Identical Name")
        player_b = Player("Identical Name")

        # Act
        actual = (player_a == player_b)

        # Assert
        self.assertTrue(actual)
