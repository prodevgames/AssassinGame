from unittest import TestCase, skip

from assassin_game_csss.domain.location import Location


class TestLocation(TestCase):
    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedNone(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Location(None)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedInt(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Location(3)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedFloat(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Location(3.4)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
    def test__constructor__shouldThrowException__whenProvidedDict(self):
        # Act
        # noinspection PyTypeChecker
        def action(): Location(3)

        # Assert
        self.assertRaises(TypeError, action)

    @skip("Not Yet Implemented")
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

    @skip("Not Yet Implemented")
    def test__get_name__shouldReturnName(self):
        expected_name = "Test Name"
        location = Location(expected_name)
        self.assertEqual(expected_name, location.get_name())

    @skip("Not Yet Implemented")
    def test__equals__shouldReturnTrue__whenConstructionIsIdentical(self):
        # Arrange
        location_a = Location("Identical Name")
        location_b = Location("Identical Name")

        # Act
        actual = (location_a == location_b)
        # Assert
        self.assertTrue(actual)
