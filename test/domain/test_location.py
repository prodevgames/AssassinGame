from unittest import TestCase, skip

from assassin_game_csss.domain.location import Location
from test.test_helper.anon import anon_location


class TestLocation(TestCase):
    def test__constructor__shouldThrowException__whenProvidedNone(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Location(None)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedInt(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Location(3)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedFloat(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Location(3.4)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedDict(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Location(3)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedList(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Location(3)

        # Assert
        self.assertRaises(TypeError, action)

    def test__constructor__shouldThrowException__whenProvidedEmptyString(self):
        # Act
        def action(): Location("")

        # Assert
        self.assertRaises(ValueError, action)

    # TODO: Delete this test when the accessor is removed
    def test__get_name__shouldReturnName(self):
        # Arrange
        expected_name = "Test Name"
        location = Location(expected_name)

        # Act
        name = location.get_name()

        # Assert
        self.assertEqual(expected_name, name)

    @skip("Not Yet Implemented")
    def test__name__shouldReturnName__whenAccessing(self):
        # Arrange
        expected_name = "Test Name"
        location = Location(expected_name)

        # Act
        name = location.name

        # Assert
        self.assertEqual(expected_name, name)

    @skip("Not Yet Implemented")
    def test__name__shouldRaiseException__whenAttemptingToSet(self):
        # Arrange
        location = anon_location()

        # Act
        # noinspection PyPropertyAccess
        def action(): location.name = "New Name"

        # Assert
        self.assertRaises(AttributeError, action)

    def test__equals__shouldReturnTrue__whenConstructionIsIdentical(self):
        # Arrange
        location_a = Location("Identical Name")
        location_b = Location("Identical Name")

        # Act
        actual = (location_a == location_b)
        # Assert
        self.assertTrue(actual)

    def test__equals__shouldReturnFalse__whenConstructionIsDifferent(self):
        # Arrange
        location_a = Location("Not Location B")
        location_b = Location("Not Location A")

        # Act
        actual = (location_a == location_b)
        # Assert
        self.assertFalse(actual)

    def test__equals__shouldConsiderInstancesIdentical__whenConstructionIsIdentical(self):
        # Arrange
        location_a = Location("Identical Name")
        location_b = Location("Identical Name")
        locations = {location_a}

        # Act
        locations.add(location_b)

        # Assert
        self.assertEqual(1, len(locations))

    def test__equals__shouldConsiderInstancesDifferent__whenConstructionIsDifferent(self):
        # Arrange
        location_a = Location("Not Location B")
        location_b = Location("Not Location A")
        locations = {location_a}

        # Act
        locations.add(location_b)

        # Assert
        self.assertEqual(2, len(locations))
