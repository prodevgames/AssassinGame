from unittest import skip, TestCase

from assassin_game_csss.domain.target import Target
from test.test_helper.anon import anon_item, anon_player, anon_location


# noinspection PyTypeChecker
class TestTarget(TestCase):
    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenPlayerArgIsWrongType(self):
        # Act
        def action(): Target(None, anon_item(), anon_location())

        # Assert
        self.assertRaises(action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenItemArgIsWrongType(self):
        # Act
        def action(): Target(anon_player(), None, anon_location())

        # Assert
        self.assertRaises(action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenLocationArgIsWrongType(self):
        # Act
        def action(): Target(anon_player(), anon_item(), None)

        # Assert
        self.assertRaises(action)
