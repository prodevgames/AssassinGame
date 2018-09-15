from unittest import TestCase
from unittest import skip

from assassin_game_csss.domain.player import Player


# noinspection PyTypeChecker
class TestPlayer(TestCase):
    @skip("Not Yet Implemented")
    def test__get_name(self):
        expected_name = "Test Name"
        player = Player(expected_name)
        self.assertEqual(expected_name, player.get_name())

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedNone(self):
        def action(): Player(None)

        self.assertRaises(action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedInt(self):
        def action_int(): Player(3)

        self.assertRaises(action_int)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedFloat(self):
        def action_float(): Player(3.4)

        self.assertRaises(action_float)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedDict(self):
        def action_dict(): Player(3)

        self.assertRaises(action_dict)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedList(self):
        def action_list(): Player(3)

        self.assertRaises(action_list)
