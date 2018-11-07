from unittest import skip, TestCase

from assassin_game_csss.domain.target import Target
from assassin_game_csss.domain.item import Item
from assassin_game_csss.domain.location import Location
from assassin_game_csss.domain.player import Player
from test.test_helper.anon import anon_item, anon_player, anon_location, anon_string, anon_target


class TestTarget(TestCase):
    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenPlayerArgIsWrongType(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Target(None, anon_item(), anon_location())

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenItemArgIsWrongType(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Target(anon_player(), None, anon_location())

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenLocationArgIsWrongType(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Target(anon_player(), anon_item(), None)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__player__shouldReturnPlayer__whenAccessing(self):
        # Arrange
        expected_player = anon_player()
        target = Target(expected_player, anon_item(), anon_location())

        # Act
        actual = target.player

        # Assert
        self.assertEquals(expected_player, actual)

    @skip("Not Yet Implemented")
    def test__player__shouldThrowException__whenTryingToSetPlayer(self):
        # Arrange
        target = anon_target()

        # Act
        def action(): target.player = anon_player()

        # Assert
        self.assertRaises(AttributeError, action)

    @skip("Not Yet Implemented")
    def test__item__shouldReturnItem__whenAccessing(self):
        # Arrange
        expected_item = anon_item()
        target = Target(anon_player(), expected_item, anon_location())

        # Act
        actual = target.item

        # Assert
        self.assertEquals(expected_item, actual)

    @skip("Not Yet Implemented")
    def test__item__shouldThrowException__whenTryingToSetItem(self):
        # Arrange
        target = anon_target()

        # Act
        def action(): target.item = anon_item()

        # Assert
        self.assertRaises(AttributeError, action)

    @skip("Not Yet Implemented")
    def test__location__shouldReturnLocation__whenAccessing(self):
        # Arrange
        expected_location = anon_location()
        target = Target(anon_player(), anon_item(), expected_location)

        # Act
        actual = target.location

        # Assert
        self.assertEquals(expected_location, actual)

    @skip("Not Yet Implemented")
    def test__location__shouldThrowException__whenTryingToSetLocation(self):
        # Arrange
        target = anon_target()

        # Act
        def action(): target.location = anon_location()

        # Assert
        self.assertRaises(AttributeError, action)

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnTrue__whenConstructionIsIdentical(self):
        # Arrange
        target_a = Target(Player("Identical Player", "abc123"), Item("Identical Item"), Location("Identical Location"))
        target_b = Target(Player("Identical Player", "abc123"), Item("Identical Item"), Location("Identical Location"))

        # Act
        actual = (target_a == target_b)

        # Assert
        self.assertTrue(actual)

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnFalse__whenConstructionIsDifferent(self):
        # Arrange
        target_a = anon_target()
        target_b = anon_target()

        # Act
        actual = (target_a == target_b)

        # Assert
        self.assertFalse(actual)

    @skip("Not Yet Implemented")
    def test__hash__shouldReturnSameValue__whenConstructionIsIdentical(self):
        target_a = Target(Player("Identical Player", "abc123"), Item("Identical Item"), Location("Identical Location"))
        target_b = Target(Player("Identical Player", "abc123"), Item("Identical Item"), Location("Identical Location"))

        # Act
        actual = hash(target_a) == hash(target_b)

        # Assert
        self.assertTrue(actual)

    # TODO: hash negative (only Player different)

    # TODO: hash negative (only Item different)

    # TODO: hash negative (only Location different)

    # TODO: Str() (CLUE style!)

    # TODO: Repr()
