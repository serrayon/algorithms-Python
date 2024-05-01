import unittest

def linear(inputList, targetValue):
    for item in inputList:
        if item == targetValue:
            return True
    return False

class TestLinearFunction(unittest.TestCase):
    def test_present_in_list(self):
        test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        look = 4
        result = linear(test, look)
        print(f"Test present in list: {result}")
        self.assertTrue(result)

    def test_not_present_in_list(self):
        test = [11, 12, 13, 14, 15]
        look = 10
        result = linear(test, look)
        print(f"Test not present in list: {result}")
        self.assertFalse(result)

    def test_empty_list(self):
        test = []
        look = 5
        result = linear(test, look)
        print(f"Test empty list: {result}")
        self.assertFalse(result)

    def test_single_element_list(self):
        test = [8]
        look = 8
        result = linear(test, look)
        print(f"Test single element list: {result}")
        self.assertTrue(result)

    def test_multiple_occurrences(self):
        test = [5, 6, 7, 5, 9, 10]
        look = 5
        result = linear(test, look)
        print(f"Test multiple occurrences: {result}")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
