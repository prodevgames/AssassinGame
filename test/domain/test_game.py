from unittest import TestCase, skip

from assassin_game_csss.domain.game import Game
from assassin_game_csss.domain.game_state import GameState
from assassin_game_csss.domain.target import Target
from test.test_helper.anon import anon_item, anon_location, anon_player, anon_game


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
    def test__constructor__shouldThrowException__whenLessThanTwoPlayersProvided(self):
        # Arrange
        players = {anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations)

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenLessThanOneItemProvided(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = set()
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations)

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenLessThanOneLocationProvided(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = set()

        # Act
        def action(): Game(players, items, locations)

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenNumTargetsArgIsNotAnInt(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        # noinspection PyTypeChecker
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

    @skip("Not Yet Implemented")
    def test__constructor__shouldGenerateTargetsForEachPlayerFromProvidedOptions__whenGameJustCreated(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        game = Game({player1, player2}, items, locations)

        # Assert
        player1_target = game.get_target(player1)
        player2_target = game.get_target(player2)
        self.assertEqual(player2, player1_target.get_player())
        self.assertEqual(player1, player2_target.get_player())
        self.assertIn(player1_target.get_item(), items)
        self.assertIn(player2_target.get_item(), items)
        self.assertIn(player2_target.get_location(), locations)
        self.assertIn(player2_target.get_location(), locations)

    @skip("Not Yet Implemented")
    def test__constructor__shouldGenerateSingleCompleteLoopOfPlayerTargets__whenNumTargetsArgIsOne(self):
        # Arrange
        initial_player = anon_player()
        players = {initial_player, anon_player(), anon_player(), anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        game = Game(players, items, locations, num_targets=1)

        # Assert
        current_player = initial_player
        seen_players = set()
        for index in range(0, len(players)):
            next_player = game.get_target(current_player).get_player()
            self.assertNotIn(next_player, seen_players)
            seen_players.add(next_player)
            current_player = next_player
        self.assertEqual(current_player, initial_player)

    @skip("Not Yet Implemented")
    def test__constructor__shouldGenerateUniqueIdentifiers__whenGameInfoIsOtherwiseIdentical(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        game1 = Game(players, items, locations)
        game2 = Game(players, items, locations)

        # Assert
        self.assertNotEqual(game1.get_game_id(), game2.get_game_id())

    @skip("Not Yet Implemented")
    def test__get_status__shouldReturnCreated__whenGameJustConstructed(self):
        # Arrange
        game = anon_game()

        # Act
        actual = game.get_status()

        # Assert
        self.assertEqual(GameState.CREATED, actual)

    @skip("Not Yet Implemented")
    def test__get_status__shouldReturnStarted__whenGameHasBeenStarted(self):
        # Arrange
        game = anon_game()
        game.start()

        # Act
        actual = game.get_status()

        # Assert
        self.assertEqual(GameState.STARTED, actual)

    @skip("Not Yet Implemented")
    def test__get_status__shouldReturnEnded__whenGameHasBeenEnded(self):
        # Arrange
        game = anon_game()
        game.start()
        game.end()

        # Act
        actual = game.get_status()

        # Assert
        self.assertEqual(GameState.ENDED, actual)

    @skip("Not Yet Implemented")
    def test__get_score__shouldReturnZeroForEveryPlayer__whenGameJustCreated(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        game = anon_game(players=players)

        # Act
        actual = [game.get_score(player) for player in players]

        # Assert
        for score in actual:
            self.assertEqual(0, score)

    @skip("Not Yet Implemented")
    def test__get_score__shouldReturnOne__whenPlayerSuccessfullyKillsTarget(self):
        # Arrange
        first_player = anon_player()
        target_player = anon_player()
        target_item = anon_item()
        target_location = anon_location()
        game = Game({first_player, target_player}, {target_item}, {target_location})
        game.start()
        game.mark_kill(first_player, Target(target_player, target_item, target_location))

        # Act
        actual = game.get_score(first_player)

        # Assert
        self.assertEqual(1, actual)

    @skip("Not Yet Implemented")
    def test__get_score__shouldIncrement__whenPlayerKillsSuccessiveTargets(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player(), anon_player()})
        game.start()
        target = game.get_target(player)
        game.mark_kill(player, target)
        target = game.get_target(player)
        game.mark_kill(player, target)

        # Act
        actual = game.get_score(player)

        # Assert
        self.assertEqual(2, actual)

    @skip("Not Yet Implemented")
    def test__start__shouldThrowException__whenCalledAfterGameAlreadyStarted(self):
        # Arrange
        game = anon_game()
        game.start()

        # Act
        def action(): game.start()

        # Assert
        self.assertRaises(RuntimeError, action)

    @skip("Not Yet Implemented")
    def test__start__shouldThrowException__whenCalledAfterGameEnded(self):
        # Arrange
        game = anon_game()
        game.start()
        game.end()

        # Act
        def action(): game.start()

        # Assert
        self.assertRaises(RuntimeError, action)

    @skip("Not Yet Implemented")
    def test__start__shouldModifyStatusToStarted__whenCalledOnGameInCreatedState(self):
        # Arrange
        game = anon_game()

        # Act
        game.start()

        # Assert
        actual = game.get_status()
        self.assertEqual(GameState.STARTED, actual)

    @skip("Not Yet Implemented")
    def test__end__shouldThrowException__whenCalledOnGameInCreatedState(self):
        # Arrange
        game = anon_game()

        # Act
        def action(): game.end()

        # Assert
        self.assertRaises(RuntimeError, action)

    @skip("Not Yet Implemented")
    def test__end__shouldThrowException__whenCalledAfterGameEnded(self):
        # Arrange
        game = anon_game()
        game.start()
        game.end()

        # Act
        def action(): game.end()

        # Assert
        self.assertRaises(RuntimeError, action)

    @skip("Not Yet Implemented")
    def test__end__shouldModifyStatusToEnded__whenCalledOnGameInStartedState(self):
        # Arrange
        game = anon_game()
        game.start()

        # Act
        game.end()

        # Assert
        self.assertEqual(GameState.ENDED, game.get_status())

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldReturnFalse__whenTargetIsCorrectButGameIsNotStarted(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        location = anon_location()
        item = anon_item()
        game = Game({player1, player2}, {item}, {location})

        # Act
        actual = game.mark_kill(player1, Target(player2, item, location))

        # Assert
        self.assertFalse(actual)

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldReturnFalse__whenTargetIsIncorrectAndGameIsNotStarted(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        location = anon_location()
        item1 = anon_item()
        item2 = anon_item()
        game = Game({player1, player2}, {item1, item2}, {location})
        target = game.get_target(player1)
        other_item = item1 if target.get_item() != item1 else item2

        # Act
        actual = game.mark_kill(player1, Target(player2, other_item, location))

        # Assert
        self.assertFalse(actual)

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldReturnTrue__whenTargetIsCorrectAndGameIsStarted(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        location = anon_location()
        item = anon_item()
        game = Game({player1, player2}, {item}, {location})
        game.start()

        # Act
        actual = game.mark_kill(player1, Target(player2, item, location))

        # Assert
        self.assertTrue(actual)

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldReturnFalse__whenTargetIsIncorrectAndGameIsStarted(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        location = anon_location()
        item1 = anon_item()
        item2 = anon_item()
        game = Game({player1, player2}, {item1, item2}, {location})
        target = game.get_target(player1)
        other_item = item1 if target.get_item() != item1 else item2
        game.start()

        # Act
        actual = game.mark_kill(player1, Target(player2, other_item, location))

        # Assert
        self.assertFalse(actual)

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldReturnFalse__whenTargetIsCorrectButGameHasEnded(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        location = anon_location()
        item = anon_item()
        game = Game({player1, player2}, {item}, {location})
        game.start()
        game.end()

        # Act
        actual = game.mark_kill(player1, Target(player2, item, location))

        # Assert
        self.assertFalse(actual)

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldReturnFalse__whenTargetIsIncorrectGameHasEnded(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        location = anon_location()
        item1 = anon_item()
        item2 = anon_item()
        game = Game({player1, player2}, {item1, item2}, {location})
        target = game.get_target(player1)
        other_item = item1 if target.get_item() != item1 else item2
        game.start()
        game.end()

        # Act
        actual = game.mark_kill(player1, Target(player2, other_item, location))

        # Assert
        self.assertFalse(actual)

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldNotModifyTarget__whenTargetIsCorrectButGameIsNotStarted(self):
        # Arrange
        player1 = anon_player()
        players = {player1, anon_player(), anon_player()}
        location = anon_location()
        item = anon_item()
        game = Game(players, {item}, {location})
        p1_initial_target = game.get_target(player1)

        # Act
        game.mark_kill(player1, p1_initial_target)

        # Assert
        p1_actual_target_player = game.get_target(player1).get_player()
        self.assertEqual(p1_initial_target.get_player(), p1_actual_target_player)

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldNotModifyTarget__whenTargetIsIncorrectAndGameIsNotStarted(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        player3 = anon_player()
        game = anon_game(players={player1, player2, player3})
        target = game.get_target(player1)
        invalid_target = Target(player2 if target.get_player() != player2 else player3,
                                target.get_item(),
                                target.get_location())

        # Act
        game.mark_kill(player1, invalid_target)

        # Assert
        p1_actual_target = game.get_target(player1)
        self.assertEqual(target, p1_actual_target)

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldModifyTarget__whenTargetIsCorrectAndGameIsStarted(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        player3 = anon_player()
        game = anon_game(players={player1, player2, player3})
        target = game.get_target(player1)
        expected_next_target_player = player2 if target.get_player() != player2 else player3
        game.start()

        # Act
        game.mark_kill(player1, target)

        # Assert
        self.assertEqual(expected_next_target_player, game.get_target(player1).get_player())

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldNotModifyTarget__whenTargetIsIncorrectAndGameIsStarted(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        player3 = anon_player()
        game = anon_game(players={player1, player2, player3})
        target = game.get_target(player1)
        invalid_target = Target(player2 if target.get_player() != player2 else player3,
                                target.get_item(),
                                target.get_location())
        game.start()

        # Act
        game.mark_kill(player1, invalid_target)

        # Assert
        p1_actual_target = game.get_target(player1)
        self.assertEqual(target, p1_actual_target)

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldNotModifyTarget__whenTargetIsCorrectButGameHasEnded(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        player3 = anon_player()
        game = anon_game(players={player1, player2, player3})
        expected_target = game.get_target(player1)
        game.start()
        game.end()

        # Act
        game.mark_kill(player1, expected_target)

        # Assert
        self.assertEqual(expected_target, game.get_target(player1))

    @skip("Not Yet Implemented")
    def test__mark_kill__shouldNotModifyTarget__whenTargetIsIncorrectGameHasEnded(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        player3 = anon_player()
        game = anon_game(players={player1, player2, player3})
        expected_target = game.get_target(player1)
        invalid_target = Target(player2 if expected_target.get_player() != player2 else player3,
                                expected_target.get_item(),
                                expected_target.get_location())
        game.start()
        game.end()

        # Act
        game.mark_kill(player1, invalid_target)

        # Assert
        p1_actual_target = game.get_target(player1)
        self.assertEqual(expected_target, p1_actual_target)

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnFalse__whenGamesCreatedWithIdenticalOptions(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}
        game1 = Game(players, items, locations)
        game2 = Game(players, items, locations)

        # Act
        actual = (game1 == game2)

        # Assert
        self.assertFalse(actual)
