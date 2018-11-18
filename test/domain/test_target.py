from unittest import TestCase

from assassin_game_csss.domain.target import Target
from test.test_helper.anon import anon_item, anon_player, anon_location, anon_target


class TestTarget(TestCase):
    def test__constructor__shouldThrowException__whenPlayerArgIsWrongType(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Target(None, anon_item(), anon_location())

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenItemArgIsWrongType(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Target(anon_player(), None, anon_location())

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenLocationArgIsWrongType(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Target(anon_player(), anon_item(), None)

        # Assert
        self.assertRaises(TypeError, action)

    def test__player__shouldReturnPlayer__whenAccessing(self):
        # Arrange
        expected_player = anon_player()
        target = Target(expected_player, anon_item(), anon_location())

        # Act
        actual = target.player

        # Assert
        self.assertEquals(expected_player, actual)

    def test__player__shouldThrowException__whenTryingToSetPlayer(self):
        # Arrange
        target = anon_target()

        # Act
        def action(): target.player = anon_player()

        # Assert
        self.assertRaises(AttributeError, action)

    def test__item__shouldReturnItem__whenAccessing(self):
        # Arrange
        expected_item = anon_item()
        target = Target(anon_player(), expected_item, anon_location())

        # Act
        actual = target.item

        # Assert
        self.assertEquals(expected_item, actual)

    def test__item__shouldThrowException__whenTryingToSetItem(self):
        # Arrange
        target = anon_target()

        # Act
        def action(): target.item = anon_item()

        # Assert
        self.assertRaises(AttributeError, action)

    def test__location__shouldReturnLocation__whenAccessing(self):
        # Arrange
        expected_location = anon_location()
        target = Target(anon_player(), anon_item(), expected_location)

        # Act
        actual = target.location

        # Assert
        self.assertEquals(expected_location, actual)

    def test__location__shouldThrowException__whenTryingToSetLocation(self):
        # Arrange
        target = anon_target()

        # Act
        def action(): target.location = anon_location()

        # Assert
        self.assertRaises(AttributeError, action)

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

    def test__equals__shouldReturnFalse__whenConstructionIsDifferent(self):
        # Arrange
        target_a = anon_target()
        target_b = anon_target()

        # Act
        actual = (target_a == target_b)

        # Assert
        self.assertFalse(actual)

    def test__hash__shouldReturnSameValue__whenConstructionIsIdentical(self):
        player = anon_player()
        item = anon_item()
        location = anon_location()
        target_a = Target(player, item, location)
        target_b = Target(player, item, location)

        # Act
        actual = hash(target_a) == hash(target_b)

        # Assert
        self.assertTrue(actual)

    def test__hash__shouldReturnDifferentValues__whenPlayerArgumentIsDifferent(self):
        item = anon_item()
        location = anon_location()
        target_a = Target(anon_player(), item, location)
        target_b = Target(anon_player(), item, location)

        # Act
        actual = hash(target_a) == hash(target_b)

        # Assert
        self.assertFalse(actual)

    def test__hash__shouldReturnDifferentValues__whenItemArgumentIsDifferent(self):
        player = anon_player()
        location = anon_location()
        target_a = Target(player, anon_item(), location)
        target_b = Target(player, anon_item(), location)

        # Act
        actual = hash(target_a) == hash(target_b)

        # Assert
        self.assertFalse(actual)

    def test__hash__shouldReturnDifferentValues__whenLocationArgumentIsDifferent(self):
        player = anon_player()
        item = anon_item()
        target_a = Target(player, item, anon_location())
        target_b = Target(player, item, anon_location())

        # Act
        actual = hash(target_a) == hash(target_b)

        # Assert
        self.assertFalse(actual)

    def test__str__shouldReturnAllTargetInfo__whenCalled(self):
        # Arrange
        target = anon_target()
        expected = "%s at %s with a %s" % (str(target.player), str(target.location), str(target.item))

        # Act
        actual = str(target)

        # Assert
        self.assertEquals(expected, actual)

    def test__repr__shouldReturnRepresentation__whenCalled(self):
        # Arrange
        target = anon_target()
        expected = "%s(%s, %s, %s)" % (Target.__name__, repr(target.player), repr(target.location), repr(target.item))

        # Act
        actual = repr(target)

        # Assert
        self.assertEquals(expected, actual)
