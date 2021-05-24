from unittest.mock import MagicMock, Mock
import unittest
import Wheel

class GIVEN_Wheel_WHEN_Spin_THEN_return_bin(unittest.TestCase):
    def setUp(self):
        self.bins = ["bin1", "bin2"]
        self.wheel = Wheel.Wheel( self.bins )
        self.wheel.rng = Mock()
        self.wheel.rng.choice = Mock( return_value="bin1")

    def runTest(self):
        value = self.wheel.next()
        self.assertEqual(value, "bin1")
        self.wheel.rng.choice.assert_called_with( self.bins )

if __name__ == "__main__":
    unittest.main()