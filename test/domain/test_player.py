from unittest import TestCase
from unittest import skip

from assassin_game_csss.domain.player import Player


# noinspection PyTypeChecker
class TestPlayer(TestCase):
    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedNone(self):
        # Act
        def action(): Player(None)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedInt(self):
        # Act
        def action_int(): Player(3)

        # Assert
        self.assertRaises(TypeError, action_int)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedFloat(self):
        # Act
        def action_float(): Player(3.4)

        # Assert
        self.assertRaises(TypeError, action_float)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedDict(self):
        # Act
        def action_dict(): Player(3)

        # Assert
        self.assertRaises(TypeError, action_dict)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedList(self):
        # Act
        def action_list(): Player(3)

        # Assert
        self.assertRaises(TypeError, action_list)

    @skip("Not Yet Implemented")
    def test__get_name__shouldReturnName(self):
        expected_name = "Test Name"
        player = Player(expected_name)
        self.assertEqual(expected_name, player.get_name())
