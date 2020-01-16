import unittest
from findstring.finder import Finder


class FinderTests(unittest.TestCase):
    """
    Class defined to initialize the string list and find_match function to retrieve matching string patterns.
    """
    
    def setUp(self):
        """
        Setup class to initialize the Finder objects
        """
        self.alphan_strings = [
                        "asd",
                        "1asd",
                        "asdf",
                        "sad",
                        "das",
                        "1234asdf"
                        ]
        self.special_strings = [
                        "@!123asdf",
                        "@123",
                        "sad sad",
                        "123asd 123asd",
                        "@asd",
                        "sad@"
                        ]
        # Initialize the Finder Objects
        self.alphan_obj = Finder(self.alphan_strings)
        self.special_obj = Finder(self.special_strings)

    def tearDown(self):
        pass
    
    def test_alphanumeric_strings(self):
        """
        Test cases to test alpha numeric characters
        """
        aplha_string = "asd"
        alphan_string = "1asd"
        # Strings that doesnt match any string in list
        alpha_string1 = "den"
        aplhan_string1 = "12asd"
        empty_string = ""
        self.assertEqual(self.alphan_obj.find_match(aplha_string), ["asd", "sad", "das"])
        self.assertEqual(self.alphan_obj.find_match(alphan_string), ["1asd"])
        self.assertEqual(self.alphan_obj.find_match(alpha_string1), [])
        self.assertEqual(self.alphan_obj.find_match(aplhan_string1), [])
        with self.assertRaises(ValueError):
            self.alphan_obj.find_match(empty_string)
    
    def test_special_strings(self):
        """
        Test cases to test special character based strings containing !@#$^&*()
        """
        sp_string1 = "@asd"
        sp_string_no_match = "@sad1"
        self.assertEqual(self.special_obj.find_match(sp_string1), ["@asd", "sad@"])
        self.assertEqual(self.special_obj.find_match(sp_string_no_match), [])
    
    def test_space_contained_strings(self):
        """
        Test cases to check the find_match compatibility with space contained strings
        """
        spaced_string = "asd asd"
        spaced_string1 = "asd1 asd1"
        self.assertEqual(self.special_obj.find_match(spaced_string), ["sad sad"])
        self.assertEqual(self.special_obj.find_match(spaced_string1), [])

    def test_unprintable_strings(self):
        """
        Test case to raise exceptions when Strings contain '\n\t' or escape sequences
        https://realpython.com/python-strings/#built-in-string-methods
        """
        unprintable_string = "sad\n"
        with self.assertRaises(Exception):
            self.alphan_obj.find_match(unprintable_string)
        pass
        
    def test_numerical_values(self):
        """
        Test cases if the string given is numerical values or digits.
        """
        int_input = 10
        float_input = 10.00
        with self.assertRaises(TypeError):
            self.alphan_obj.find_match(int_input)
        with self.assertRaises(TypeError):
            self.alphan_obj.find_match(float_input)


if __name__ == "__main__":
    unittest.main()
