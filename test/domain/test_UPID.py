from unittest import TestCase

from assassin_game_csss.domain.upid import UPID


class TestUPID(TestCase):

    def test__constructor__shouldThrowException__whenGivenNonString(self):
        # Act
        # noinspection PyTypeChecker
        def action_none(): UPID(None)

        # noinspection PyTypeChecker
        def action_int(): UPID(42)

        # noinspection PyTypeChecker
        def action_set(): UPID(set())

        # noinspection PyTypeChecker
        def action_list(): UPID([])

        # Assert
        self.assertRaises(TypeError, action_none)
        self.assertRaises(TypeError, action_int)
        self.assertRaises(TypeError, action_set)
        self.assertRaises(TypeError, action_list)

    def test__constructor__shouldThrowException__whenUPIDDoesNotMatchExpectedPattern(self):
        # Arrange
        upid1 = "snto264"
        upid2 = "vrz1234"
        upid3 = "123abc"
        upid4 = "ske 123"
        upid5 = " skl153"
        upid6 = "abc123 "

        # Act
        def action1(): UPID(upid1)

        def action2(): UPID(upid2)

        def action3(): UPID(upid3)

        def action4(): UPID(upid4)

        def action5(): UPID(upid5)

        def action6(): UPID(upid6)

        # Assert
        self.assertRaises(ValueError, action1)
        self.assertRaises(ValueError, action2)
        self.assertRaises(ValueError, action3)
        self.assertRaises(ValueError, action4)
        self.assertRaises(ValueError, action5)
        self.assertRaises(ValueError, action6)

    def test__constructor__shouldConvertUppercaseUPIDToLower__whenGivenValidButUpperUPID(self):
        # Arrange
        upid = "aCe249"
        expected_upid = upid.lower()

        # Act
        actual = UPID(upid)

        # Assert
        self.assertEqual(expected_upid, actual.upid)

    def test__upid__shouldReturnProvidedUPID__whenAccessing(self):
        # Arrange
        upid = "ern395"

        # Act
        actual = UPID(upid)

        # Assert
        self.assertEqual(upid, actual.upid)

    def test__equals__shouldReturnTrue__whenConstructionIsIdentical(self):
        # Arrange
        upid_a = UPID("ans235")
        upid_b = UPID("ans235")

        # Act
        actual = (upid_a == upid_b)

        # Assert
        self.assertTrue(actual)

    def test__equals__shouldReturnFalse__whenConstructionIsDifferent(self):
        # Arrange
        upid_a = UPID("sof252")
        upid_b = UPID("dso351")

        # Act
        actual = (upid_a == upid_b)

        # Assert
        self.assertFalse(actual)

    def test__hash__shouldConsiderInstancesIdentical__whenConstructionIsIdentical(self):
        # Arrange
        upid_a = UPID("spo130")
        upid_b = UPID("spo130")
        upids = {upid_a}

        # Act
        upids.add(upid_b)

        # Assert
        self.assertEqual(1, len(upids))

    def test__hash__shouldConsiderInstancesDifferent__whenConstructionIsDifferent(self):
        # Arrange
        upid_a = UPID("enp234")
        upid_b = UPID("soe503")
        upids = {upid_a}

        # Act
        upids.add(upid_b)

        # Assert
        self.assertEqual(2, len(upids))
