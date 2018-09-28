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
        player = anon_player()
        item = anon_item()
        location = anon_location()
        target_a = Target(player, item, location)
        target_b = Target(player, item, location)

        # Act
        actual = (target_a == target_b)

        # Assert
        self.assertTrue(actual)

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnFalse__whenConstructionIsDifferent(self):
        # Arrange
        player_a = anon_player()
        player_b = anon_player()
        item_a = anon_item()
        item_b = anon_item()
        location_a = anon_location()
        location_b = anon_location()

        target_a = Target(player_a, item_a, location_a)
        target_b = Target(player_b, item_b, location_b)

        # Act
        actual = (target_a == target_b)

        # Assert\
        self.assertFalse(actual)

    @skip("Not Yet Implemented")
    def test__equals__shouldConsiderInstancesIdentical__whenConstructionIsIdentical(self):
        # Arrange
        player = anon_player()
        item = anon_item()
        location = anon_location()
        target_a = Target(player, item, location)
        target_b = Target(player, item, location)
        targets = {target_a}

        # Act
        targets.add(target_b)

        # Assert
        self.assertEqual(1, len(targets))

    @skip("Not Yet Implemented")
    def test__equals__shouldConsiderInstancesDifferent__whenConstructionIsDifferent(self):
        # Arrange
        player_a = anon_player()
        player_b = anon_player()
        item_a = anon_item()
        item_b = anon_item()
        location_a = anon_location()
        location_b = anon_location()

        target_a = Target(player_a, item_a, location_a)
        target_b = Target(player_b, item_b, location_b)
        targets = {target_a}

        # Act
        targets.add(target_b)

        # Assert
        self.assertEqual(2, len(targets))
