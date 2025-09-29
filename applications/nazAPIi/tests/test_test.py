import unittest


class TestAPI(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1 + 1, 2)
        
    def test_failure(self):
        self.assertNotEqual(1 + 1, 3)    
    