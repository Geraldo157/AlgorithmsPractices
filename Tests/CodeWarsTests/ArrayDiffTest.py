import unittest


class Test_Array_Diff(unittest.TestCase):
    def test_(self):
        array_1 = [1, 2, 3, 4, 5]
        array_2 = [1, 3, 5]
        self.assertEqual(array_diff(array_1, array_2), [2, 4])
