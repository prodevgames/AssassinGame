from unittest import skip, TestCase

from assassin_game_csss.domain.target import Target
from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player
from test.test_helper.anon import anon_item, anon_player, anon_location


class TestTarget(TestCase):
    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenPlayerArgIsWrongType(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Target(None, anon_item(), anon_location())

        # Assert
        self.assertRaises(action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenItemArgIsWrongType(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Target(anon_player(), None, anon_location())

        # Assert
        self.assertRaises(action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenLocationArgIsWrongType(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Target(anon_player(), anon_item(), None)

        # Assert
        self.assertRaises(action)

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnTrue__whenConstructionIsIdentical(self):
        # Arrange
        target_a = Target(Player("Identical Player"), Item("Identical Item"), Location("Identical Location"))
        target_b = Target(Player("Identical Player"), Item("Identical Item"), Location("Identical Location"))

        # Act
        actual = (target_a == target_b)

        # Assert
        self.assertTrue(actual)
