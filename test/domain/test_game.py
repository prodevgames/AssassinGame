from unittest import TestCase
from uuid import UUID

from assassin_game_csss.domain.exceptions import IllegalActionError
from assassin_game_csss.domain.game import Game
from assassin_game_csss.domain.game_state import GameState
from assassin_game_csss.domain.target import Target
from test.test_helper.anon import anon_item, anon_location, anon_player, anon_game


class TestGame(TestCase):
    def test__constructor__shouldThrowException__whenPlayersArgIsNotSetOfPlayers(self):
        # Arrange
        invalid_players = {2, 3, 4}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        # noinspection PyTypeChecker
        def action(): Game(invalid_players, items, locations)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenItemsArgIsNotSetOfItems(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        invalid_items = {2, 3, 4}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        # noinspection PyTypeChecker
        def action(): Game(players, invalid_items, locations)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenLocationsArgIsNotSetOfLocations(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        invalid_locations = {2, 3, 4}

        # Act
        # noinspection PyTypeChecker
        def action(): Game(players, items, invalid_locations)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenLessThanTwoPlayersProvided(self):
        # Arrange
        players = {anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations)

        # Assert
        self.assertRaises(ValueError, action)

    def test__constructor__shouldThrowException__whenLessThanOneItemProvided(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = set()
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations)

        # Assert
        self.assertRaises(ValueError, action)

    def test__constructor__shouldThrowException__whenLessThanOneLocationProvided(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = set()

        # Act
        def action(): Game(players, items, locations)

        # Assert
        self.assertRaises(ValueError, action)

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

    def test__constructor__shouldThrowException__whenNumTargetArgIsLessThanOne(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        def action(): Game(players, items, locations, num_targets=0)

        # Assert
        self.assertRaises(ValueError, action)

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
        self.assertEqual(player2, player1_target.player)
        self.assertEqual(player1, player2_target.player)
        self.assertIn(player1_target.item, items)
        self.assertIn(player2_target.item, items)
        self.assertIn(player2_target.location, locations)
        self.assertIn(player2_target.location, locations)

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
            next_player = game.get_target(current_player).player
            self.assertNotIn(next_player, seen_players)
            seen_players.add(next_player)
            current_player = next_player
        self.assertEqual(current_player, initial_player)

    def test__constructor__shouldGenerateUniqueIdentifiers__whenGameInfoIsOtherwiseIdentical(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        items = {anon_item(), anon_item(), anon_item()}
        locations = {anon_location(), anon_location(), anon_location()}

        # Act
        game1 = Game(players, items, locations)
        game2 = Game(players, items, locations)

        # Assert
        self.assertNotEqual(game1.id, game2.id)

    def test__id__shouldReturnUuid__whenGameJustCreated(self):
        # Arrange
        game = anon_game()

        # Act
        game_id = game.id

        # Assert
        self.assertIsInstance(game_id, UUID)

    def test__id__shouldNotChange__whenGameStarts(self):
        # Arrange
        game = anon_game()
        expected_id = game.id
        game.start()

        # Act
        actual = game.id

        # Assert
        self.assertEqual(expected_id, actual)

    def test__id__shouldNotChange__whenEnds(self):
        # Arrange
        game = anon_game()
        expected_id = game.id
        game.start()
        game.end()

        # Act
        actual = game.id

        # Assert
        self.assertEqual(expected_id, actual)

    def test__status__shouldReturnCreated__whenGameJustConstructed(self):
        # Arrange
        game = anon_game()

        # Act
        actual = game.status

        # Assert
        self.assertEqual(GameState.CREATED, actual)

    def test__status__shouldReturnStarted__whenGameHasBeenStarted(self):
        # Arrange
        game = anon_game()
        game.start()

        # Act
        actual = game.status

        # Assert
        self.assertEqual(GameState.STARTED, actual)

    def test__status__shouldReturnEnded__whenGameHasBeenEnded(self):
        # Arrange
        game = anon_game()
        game.start()
        game.end()

        # Act
        actual = game.status

        # Assert
        self.assertEqual(GameState.ENDED, actual)

    def test__get_score__shouldThrowException__whenPlayerNotInGame(self):
        # Arrange
        game = anon_game()

        # Act
        def action(): game.get_score(anon_player())

        # Assert
        self.assertRaises(ValueError, action)

    def test__get_score__shouldReturnZeroForEveryPlayer__whenGameJustCreated(self):
        # Arrange
        players = {anon_player(), anon_player(), anon_player()}
        game = anon_game(players=players)

        # Act
        actual = [game.get_score(player) for player in players]

        # Assert
        for score in actual:
            self.assertEqual(0, score)

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
    
    def test__get_target__shouldThrowException__whenPlayerNotInGame(self):
        # ArrangeX
        game = anon_game()

        # Act
        def action(): game.get_target(anon_player())

        # Assert
        self.assertRaises(ValueError, action)
    
    def test__get_target__shouldReturnTarget__whenGameCreated(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player(), anon_player()})

        # Act
        actual = game.get_target(player)

        # Assert
        self.assertIsNotNone(actual)

    def test__get_target__shouldReturnSameTarget__whenCalledAfterGameStarted(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player(), anon_player()})
        expected_target = game.get_target(player)
        game.start()

        # Act
        actual = game.get_target(player)

        # Assert
        self.assertEqual(expected_target, actual)

    def test__get_target__shouldReturnSameTarget__whenCalledAfterGameEnded(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player(), anon_player()})
        game.start()
        expected_target = game.get_target(player)
        game.end()

        # Act
        actual = game.get_target(player)

        # Assert
        self.assertEqual(expected_target, actual)
    
    def test__get_target__shouldThrowException__whenPlayerIsDead(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player(), anon_player()})
        target = game.get_target(player)
        dead_player = target.player
        game.start()
        game.mark_kill(player, target)

        # Act
        def action(): game.get_target(dead_player)

        # Assert
        self.assertRaises(ValueError, action)

    def test__start__shouldThrowException__whenCalledAfterGameAlreadyStarted(self):
        # Arrange
        game = anon_game()
        game.start()

        # Act
        def action(): game.start()

        # Assert
        self.assertRaises(IllegalActionError, action)

    def test__start__shouldThrowException__whenCalledAfterGameEnded(self):
        # Arrange
        game = anon_game()
        game.start()
        game.end()

        # Act
        def action(): game.start()

        # Assert
        self.assertRaises(IllegalActionError, action)

    def test__start__shouldModifyStatusToStarted__whenCalledOnGameInCreatedState(self):
        # Arrange
        game = anon_game()

        # Act
        game.start()

        # Assert
        actual = game.status
        self.assertEqual(GameState.STARTED, actual)

    def test__end__shouldThrowException__whenCalledOnGameInCreatedState(self):
        # Arrange
        game = anon_game()

        # Act
        def action(): game.end()

        # Assert
        self.assertRaises(IllegalActionError, action)

    def test__end__shouldThrowException__whenCalledAfterGameEnded(self):
        # Arrange
        game = anon_game()
        game.start()
        game.end()

        # Act
        def action(): game.end()

        # Assert
        self.assertRaises(IllegalActionError, action)

    def test__end__shouldModifyStatusToEnded__whenCalledOnGameInStartedState(self):
        # Arrange
        game = anon_game()
        game.start()

        # Act
        game.end()

        # Assert
        self.assertEqual(GameState.ENDED, game.status)

    def test__mark_kill__shouldThrowException__whenPlayerNotInGameAndGameStarted(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player()})
        valid_target = game.get_target(player)
        game.start()

        # Act
        def action(): game.mark_kill(anon_player(), valid_target)

        # Assert
        self.assertRaises(ValueError, action)

    def test__mark_kill__shouldThrowException__whenTargetPlayerNotInGameAndGameStarted(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player()})
        valid_target = game.get_target(player)
        invalid_target = Target(anon_player(), valid_target.item, valid_target.location)
        game.start()

        # Act
        def action(): game.mark_kill(player, invalid_target)

        # Assert
        self.assertRaises(ValueError, action)

    def test__mark_kill__shouldThrowException__whenTargetPlayerIsKillingPlayer(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player(), anon_player()})
        game.start()

        # Act
        def action(): game.mark_kill(player, Target(player, anon_item(), anon_location()))

        # Assert
        self.assertRaises(ValueError, action)

    def test__mark_kill__shouldThrowException__whenGameIsNotStarted(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        location = anon_location()
        item = anon_item()
        game = Game({player1, player2}, {item}, {location})

        # Act
        def action(): game.mark_kill(player1, Target(player2, item, location))

        # Assert
        self.assertRaises(IllegalActionError, action)

    def test__mark_kill__shouldThrowException__whenGameHasEnded(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        location = anon_location()
        item = anon_item()
        game = Game({player1, player2}, {item}, {location})
        game.start()
        game.end()

        # Act
        def action(): game.mark_kill(player1, Target(player2, item, location))

        # Assert
        self.assertRaises(IllegalActionError, action)

    def test__mark_kill__shouldRaiseException__whenTargetIsIncorrect(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        location = anon_location()
        item1 = anon_item()
        item2 = anon_item()
        game = Game({player1, player2}, {item1, item2}, {location})
        target = game.get_target(player1)
        other_item = item1 if target.item != item1 else item2
        game.start()

        # Act
        def action(): game.mark_kill(player1, Target(player2, other_item, location))

        # Assert
        self.assertRaises(ValueError, action)

    def test__mark_kill__shouldRaiseException__whenPlayerIsNotInGame(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        location = anon_location()
        item1 = anon_item()
        item2 = anon_item()
        game = Game({player1, player2}, {item1, item2}, {location})
        target = game.get_target(player1)
        game.start()

        # Act
        def action(): game.mark_kill(anon_player(), target)

        # Assert
        self.assertRaises(ValueError, action)

    def test__mark_kill__shouldNotModifyTarget__whenTargetIsCorrectButGameIsNotStarted(self):
        # Arrange
        player1 = anon_player()
        players = {player1, anon_player(), anon_player()}
        location = anon_location()
        item = anon_item()
        game = Game(players, {item}, {location})
        p1_initial_target = game.get_target(player1)

        # Act
        try:
            game.mark_kill(player1, p1_initial_target)
        except IllegalActionError:
            pass

        # Assert
        p1_actual_target_player = game.get_target(player1).player
        self.assertEqual(p1_initial_target.player, p1_actual_target_player)

    def test__mark_kill__shouldNotModifyTarget__whenTargetIsIncorrectAndGameIsNotStarted(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        player3 = anon_player()
        game = anon_game(players={player1, player2, player3})
        target = game.get_target(player1)
        invalid_target = Target(player2 if target.player != player2 else player3,
                                target.item,
                                target.location)

        # Act
        try:
            game.mark_kill(player1, invalid_target)
        except IllegalActionError:
            pass

        # Assert
        p1_actual_target = game.get_target(player1)
        self.assertEqual(target, p1_actual_target)

    def test__mark_kill__shouldModifyTarget__whenTargetIsCorrectAndGameIsStarted(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        player3 = anon_player()
        game = anon_game(players={player1, player2, player3})
        target = game.get_target(player1)
        expected_next_target_player = player2 if target.player != player2 else player3
        game.start()

        # Act
        game.mark_kill(player1, target)

        # Assert
        self.assertEqual(expected_next_target_player, game.get_target(player1).player)

    def test__mark_kill__shouldNotModifyTarget__whenTargetIsIncorrectAndGameIsStarted(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        player3 = anon_player()
        game = anon_game(players={player1, player2, player3})
        target = game.get_target(player1)
        invalid_target = Target(player2 if target.player != player2 else player3,
                                target.item,
                                target.location)
        game.start()

        # Act
        try:
            game.mark_kill(player1, invalid_target)
        except ValueError:
            pass

        # Assert
        p1_actual_target = game.get_target(player1)
        self.assertEqual(target, p1_actual_target)

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
        try:
            game.mark_kill(player1, expected_target)
        except IllegalActionError:
            pass

        # Assert
        self.assertEqual(expected_target, game.get_target(player1))

    def test__mark_kill__shouldNotModifyTarget__whenTargetIsIncorrectGameHasEnded(self):
        # Arrange
        player1 = anon_player()
        player2 = anon_player()
        player3 = anon_player()
        game = anon_game(players={player1, player2, player3})
        expected_target = game.get_target(player1)
        invalid_target = Target(player2 if expected_target.player != player2 else player3,
                                expected_target.item,
                                expected_target.location)
        game.start()
        game.end()

        # Act
        try:
            game.mark_kill(player1, invalid_target)
        except IllegalActionError:
            pass

        # Assert
        p1_actual_target = game.get_target(player1)
        self.assertEqual(expected_target, p1_actual_target)

    def test__mark_kill__shouldGiveKilledPlayersTargetToKiller__whenKilledPlayerHasTargetThatIsNotKiller(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player(), anon_player()})
        target = game.get_target(player)
        expected_next_target = game.get_target(target.player)
        game.start()

        # Act
        game.mark_kill(player, target)

        # Assert
        self.assertEqual(expected_next_target, game.get_target(player))

    def test__mark_kill__shouldSetLastPlayersTargetToHimself__whenOnlyOnePlayerLeft(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player()})
        target = game.get_target(player)
        game.start()

        # Act
        game.mark_kill(player, target)

        # Assert
        self.assertEqual(player, game.get_target(player).player)

    def test__mark_kill__shouldEndGame__whenAllPlayersButLastHaveBeenKilled(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player(), anon_player()})
        game.start()
        first_target = game.get_target(player)
        game.mark_kill(player, first_target)
        final_target = game.get_target(player)

        # Act
        game.mark_kill(player, final_target)

        # Assert
        self.assertEqual(GameState.ENDED, game.status)

    def test__mark_kill__shouldRemovePlayersTarget__whenPlayerSuccessfullyKilled(self):
        # Arrange
        player = anon_player()
        game = anon_game(players={player, anon_player(), anon_player()})
        game.start()
        target = game.get_target(player)
        killed_player = target.player

        # Act
        game.mark_kill(player, target)

        # Assert
        self.assertRaises(ValueError, lambda: game.get_target(killed_player))

    def test__is_alive__shouldReturnCorrectBool__whenPlayersAreStillAliveAndGameIsNotStarted(self):
        # Arrange
        player1 = anon_player()
        game = anon_game(players={player1, anon_player(), anon_player()})
        player2 = game.get_target(player1).player
        player3 = game.get_target(player2).player

        # Act
        actual1 = game.is_alive(player1)
        actual2 = game.is_alive(player2)
        actual3 = game.is_alive(player3)

        # Assert
        self.assertTrue(actual1)
        self.assertTrue(actual2)
        self.assertTrue(actual3)

    def test__is_alive__shouldReturnCorrectBool__whenPlayersAreStillAliveAndGameIsActive(self):
        # Arrange
        player1 = anon_player()
        game = anon_game(players={player1, anon_player(), anon_player()})
        player2 = game.get_target(player1).player
        player3 = game.get_target(player2).player
        game.start()

        # Act
        actual1 = game.is_alive(player1)
        actual2 = game.is_alive(player2)
        actual3 = game.is_alive(player3)

        # Assert
        self.assertTrue(actual1)
        self.assertTrue(actual2)
        self.assertTrue(actual3)

    def test__is_alive__shouldReturnCorrectBool__whenSomePlayersAreDeadAndGameIsActive(self):
        # Arrange
        player1 = anon_player()
        game = anon_game(players={player1, anon_player(), anon_player()})
        player1_target = game.get_target(player1)
        player2 = player1_target.player
        player3 = game.get_target(player2).player
        game.start()
        game.mark_kill(player1, player1_target)

        # Act
        actual1 = game.is_alive(player1)
        actual2 = game.is_alive(player2)
        actual3 = game.is_alive(player3)

        # Assert
        self.assertTrue(actual1)
        self.assertFalse(actual2)
        self.assertTrue(actual3)

    def test__is_alive__shouldReturnCorrectBool__whenPlayersAreStillAliveAndGameIsOver(self):
        # Arrange
        player1 = anon_player()
        game = anon_game(players={player1, anon_player(), anon_player()})
        player2 = game.get_target(player1).player
        player3 = game.get_target(player2).player
        game.start()
        game.end()

        # Act
        actual1 = game.is_alive(player1)
        actual2 = game.is_alive(player2)
        actual3 = game.is_alive(player3)

        # Assert
        self.assertTrue(actual1)
        self.assertTrue(actual2)
        self.assertTrue(actual3)

    def test__is_alive__shouldReturnCorrectBool__whenSomePlayersAreDeadAndGameIsOver(self):
        # Arrange
        player1 = anon_player()
        game = anon_game(players={player1, anon_player(), anon_player()})
        player1_target = game.get_target(player1)
        player2 = player1_target.player
        player3 = game.get_target(player2).player
        game.start()
        game.mark_kill(player1, player1_target)
        game.end()

        # Act
        actual1 = game.is_alive(player1)
        actual2 = game.is_alive(player2)
        actual3 = game.is_alive(player3)

        # Assert
        self.assertTrue(actual1)
        self.assertFalse(actual2)
        self.assertTrue(actual3)

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
