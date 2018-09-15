from unittest import TestCase, skip

from assassin_game_csss.domain.game import Game
from test.test_helper.anon import anon_item, anon_location, anon_player


# noinspection PyTypeChecker
class TestGame(TestCase):
    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenPlayersArgIsNotSetOfPlayers(self):
        # Arrange
        invalid_players = {2, 3, 4}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(invalid_players, items, locations)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenItemsArgIsNotSetOfItems(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        invalid_items = {2, 3, 4}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, invalid_items, locations)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenLocationsArgIsNotSetOfLocations(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        invalid_locations = {2, 3, 4}

        # Act
        def action(): Game(players, items, invalid_locations)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenNumTargetsArgIsNotAnInt(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations, num_targets=None)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenNumTargetArgIsLessThanOne(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations, num_targets=0)

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenNumTargetArgIsNotOne(self):
        # TODO GH 2018-Sep-15: Add functionality to support multiple targets and change this test to match new behaviour
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations, num_targets=2)

        # Assert
        self.assertRaises(NotImplementedError, action)


