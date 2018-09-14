from unittest import TestCase
from unittest import skip


from assassin_game_csss.domain.player import Player


class TestPlayer(TestCase):
    @skip("Not Yet Implemented")
    def test_get_name(self):
        expected_name = "Test Name"
        player = Player(expected_name)
        self.assertEqual(expected_name, player.get_name())
