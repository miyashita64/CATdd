import unittest
from common.difference import Difference
from common.catdd_info import CATddInfo
from common.log import Log

class TestDifference(unittest.TestCase):
    def test_difference_print(self):
        Log.output_path = CATddInfo.path("output/test_difference_print.log")
        text1 = "".join(str([1,2,3,4,5,6,7,8,9]))
        text2 = "".join(str([1,2,3,5,6,7,8,9]))
        Log.log(f"text1: {text1}")
        Log.log(f"text2: {text2}")
        diff = Difference(text1, text2)
        diff.print()
        Log.save()
