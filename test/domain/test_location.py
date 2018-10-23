from unittest import TestCase

from assassin_game_csss.domain.location import Location


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

    def test__get_name__shouldReturnName(self):
        expected_name = "Test Name"
        location = Location(expected_name)
        self.assertEqual(expected_name, location.get_name())

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
