import unittest

from translator import frenchToEnglish, englishToFrench

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    def test2(self):
        self.assertEqual(englishToFrench('How are you?'), "Comment es-tu?")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    def test2(self):
        self.assertEqual(frenchToEnglish('Comment es-tu?'), "How are you?")

unittest.main()