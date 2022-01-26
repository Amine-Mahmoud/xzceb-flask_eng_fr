""" This is the test module"""

import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Good'), 'Bonne') # test when 'Good' is given as input the output is 'Bonne'.
        self.assertEqual(english_to_french('Bad'), 'Mauvais')  # test when 'Bad' is given as input the output is 'Mauvais'.
        self.assertEqual(english_to_french(''), '')  # test when null is given as input the output is not also null.
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.


class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Trois'), 'Three') # test when 'Trois' is given as input the output is 'Three'.
        self.assertEqual(french_to_english('Deux'), 'Two')  # test when 'Deux' is given as input the output is 'Two'.
        self.assertEqual(french_to_english(''), '')  # test when null is given as input the output is not also null.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.

unittest.main()
