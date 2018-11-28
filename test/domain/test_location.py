from unittest import TestCase

from assassin_game_csss.domain.location import Location
from test.test_helper.anon import anon_location, anon_string


class TestLocation(TestCase):

    def test__constructor__shouldThrowException__whenGivenNonString(self):
        # Act
        # noinspection PyTypeChecker
        def action_none(): Location(None)

        # noinspection PyTypeChecker
        def action_int(): Location(42)

        # noinspection PyTypeChecker
        def action_set(): Location(set())

        # noinspection PyTypeChecker
        def action_list(): Location([])

        # Assert
        self.assertRaises(TypeError, action_none)
        self.assertRaises(TypeError, action_int)
        self.assertRaises(TypeError, action_set)
        self.assertRaises(TypeError, action_list)

    def test__constructor__shouldThrowException__whenProvidedEmptyString(self):
        # Act
        def action(): Location("")

        # Assert
        self.assertRaises(ValueError, action)

    def test__name__shouldReturnName__whenAccessing(self):
        # Arrange
        expected_name = anon_string()
        location = Location(expected_name)

        # Act
        name = location.name

        # Assert
        self.assertEqual(expected_name, name)

    def test__name__shouldRaiseException__whenAttemptingToSet(self):
        # Arrange
        location = anon_location()

        # Act
        # noinspection PyPropertyAccess
        def action(): location.name = anon_string()

        # Assert
        self.assertRaises(AttributeError, action)

    def test__equals__shouldReturnTrue__whenNameIsSame(self):
        # Arrange
        name = anon_string()
        location_a = Location(name)
        location_b = Location(name)

        # Act
        actual = (location_a == location_b)
        # Assert
        self.assertTrue(actual)

    def test__equals__shouldReturnFalse__whenNameIsDifferent(self):
        # Arrange
        location_a = Location(anon_string())
        location_b = Location(anon_string())

        # Act
        actual = (location_a == location_b)
        # Assert
        self.assertFalse(actual)

    def test__hash__shouldReturnSameHash__whenNameIsSame(self):
        # Arrange
        name = anon_string()
        location_a = Location(name)
        location_b = Location(name)

        # Act
        hash_a = location_a
        hash_b = location_b

        # Assert
        self.assertEqual(hash_a, hash_b)

    def test__hash__shouldReturnDifferentHash__whenNameIsDifferent(self):
        # Arrange
        location_a = Location(anon_string())
        location_b = Location(anon_string())

        # Act
        hash_a = location_a
        hash_b = location_b

        # Assert
        self.assertNotEqual(hash_a, hash_b)

    def test__str__shouldReturnLocationName(self):
        # Arrange
        expected_name = anon_string()
        location = Location(expected_name)

        # Act
        actual = str(location)

        # Assert
        self.assertEquals(expected_name, actual)

    def test__repr__shouldReturnRepresentation(self):
        # Arrange
        name = anon_string()
        location = Location(name)
        expected = "%s(\"%s\")" % (Location.__name__, name)

        # Act
        actual = repr(location)

        # Assert
        self.assertEquals(expected, actual)
