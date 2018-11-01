from unittest import TestCase, skip

from assassin_game_csss.domain.player import Player
from assassin_game_csss.domain.upid import UPID
from test.test_helper.anon import anon_player, anon_string, anon_upid


class TestPlayer(TestCase):

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenGivenNonStringName(self):
        # Act
        # noinspection PyTypeChecker
        def action_none(): Player(None, anon_upid())

        # noinspection PyTypeChecker
        def action_int(): Player(42, anon_upid())

        # noinspection PyTypeChecker
        def action_set(): Player(set(), anon_upid())

        # noinspection PyTypeChecker
        def action_list(): Player([], anon_upid())

        # Assert
        self.assertRaises(TypeError, action_none)
        self.assertRaises(TypeError, action_int)
        self.assertRaises(TypeError, action_set)
        self.assertRaises(TypeError, action_list)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenGivenNeitherUPIDNorStringForIdentifierArgument(self):
        # Act
        # noinspection PyTypeChecker
        def action_none(): Player(anon_string(), None)

        # noinspection PyTypeChecker
        def action_int(): Player(anon_string(), 42)

        # noinspection PyTypeChecker
        def action_set(): Player(anon_string(), set())

        # noinspection PyTypeChecker
        def action_list(): Player(anon_string(), [])

        # Assert
        self.assertRaises(TypeError, action_none)
        self.assertRaises(TypeError, action_int)
        self.assertRaises(TypeError, action_set)
        self.assertRaises(TypeError, action_list)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedEmptyStringName(self):
        # Act
        def action(): Player("", anon_upid())

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedEmptyStringUPID(self):
        # Act
        def action(): Player(anon_string(), "")

        # Assert
        self.assertRaises(ValueError, action)

    @skip("Not Yet Implemented")
    def test__name__shouldReturnName_whenAccessing(self):
        # Arrange
        expected_name = "Test Name"
        player = Player(expected_name, anon_upid())

        # Act
        actual = player.name

        # Assert
        self.assertEqual(expected_name, actual)

    @skip("Not Yet Implemented")
    def test__name__shouldThrowException__whenAttemptingToSet(self):
        # Arrange
        player = anon_player()

        # Act
        # noinspection PyPropertyAccess
        def action(): player.name = "New Name"

        # Assert
        self.assertRaises(AttributeError, action)

    @skip("Not Yet Implemented")
    def test__upid__shouldReturnUPID__whenConstructedWithStr(self):
        # Arrange
        expected_upid_string = str(anon_upid())
        player = Player(anon_string(), expected_upid_string)

        # Act
        actual = player.upid

        # Assert
        self.assertIsInstance(actual, UPID)
        self.assertEqual(expected_upid_string, str(actual))

    @skip("Not Yet Implemented")
    def test__upid__shouldReturnUPID__whenConstructedWithUPID(self):
        # Arrange
        expected_upid = anon_upid()
        player = Player(anon_string(), expected_upid)

        # Act
        actual = player.upid

        # Assert
        self.assertIsInstance(actual, UPID)
        self.assertEqual(expected_upid, actual)

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnTrue__whenUPIDIsIdenticalAndNameIsSame(self):
        # Arrange
        upid = anon_upid()
        name = anon_string()
        player_a = Player(name, upid)
        player_b = Player(name, upid)

        # Act
        actual = (player_a == player_b)

        # Assert
        self.assertTrue(actual)

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnTrue__whenUPIDIsIdenticalAndNameIsDifferent(self):
        # Arrange
        upid = anon_upid()
        player_a = Player(anon_string(), upid)
        player_b = Player(anon_string(), upid)

        # Act
        actual = (player_a == player_b)

        # Assert
        self.assertTrue(actual)

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnFalse__whenUPIDIsDifferentAndNameIsSame(self):
        # Arrange
        name = anon_string()
        player_a = Player(name, anon_upid())
        player_b = Player(name, anon_upid())

        # Act
        actual = (player_a == player_b)

        # Assert
        self.assertFalse(actual)
        self.assertTrue(actual)

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnFalse__whenUPIDIsDifferentAndNameIsDifferent(self):
        # Arrange
        player_a = Player(anon_string(), anon_upid())
        player_b = Player(anon_string(), anon_upid())

        # Act
        actual = (player_a == player_b)

        # Assert
        self.assertFalse(actual)

    @skip("Not Yet Implemented")
    def test__hash__shouldConsiderInstancesIdentical__whenUPIDIsSame(self):
        # Arrange
        upid = anon_upid()
        player_a = Player(anon_string(), upid)
        player_b = Player(anon_string(), upid)
        players = {player_a}

        # Act
        players.add(player_b)

        # Assert
        self.assertEqual(1, len(players))

    @skip("Not Yet Implemented")
    def test__hash__shouldConsiderInstancesDifferent__whenConstructionIsDifferent(self):
        # Arrange
        name = anon_string()
        player_a = Player(name, anon_upid())
        player_b = Player(name, anon_upid())
        players = {player_a}

        # Act
        players.add(player_b)

        # Assert
        self.assertEqual(2, len(players))

    @skip("Not Yet Implemented")
    def test__str__shouldReturnStringForm(self):
        # Arrange
        name = anon_string()
        upid = anon_upid()
        expected_string = "%s(\"%s\", \"%s\")" % (Player.__name__, name, str(upid))
        player = Player(name, upid)

        # Act
        actual = str(player)

        # Assert
        self.assertEqual(expected_string, actual)

    @skip("Not Yet Implemented")
    def test__repr__shouldReturnRepresentation(self):
        # Arrange
        name = anon_string()
        upid = anon_upid()
        expected_string = "%s(\"%s\",%s)" % (Player.__name__, name, repr(upid))
        player = Player(name, upid)

        # Act
        actual = str(player)

        # Assert
        self.assertEqual(expected_string, actual)
