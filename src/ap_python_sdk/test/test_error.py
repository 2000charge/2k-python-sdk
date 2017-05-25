from ap_python_sdk.error import 2000ChargeError, APIError, \
    InvalidParameterError
from numpy.ma.testutils import assert_equal
import unittest


class ErrorTest(unittest.TestCase):

    def test_2000_charge_error(self):
        err = 2000ChargeError("Unexpected error communicating with 2000Charge.")
        assert_equal(err.message, "Unexpected error communicating with 2000Charge.")

    def test_api_error(self):
        err = APIError("Unexpected error communicating with 2000Charge.")
        assert_equal(err.message, "Unexpected error communicating with 2000Charge.")

    def test_invalid_parameter_error(self):
        err = InvalidParameterError("Invalid parameter name.", "name")
        assert_equal("Invalid parameter name.", err.message)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
