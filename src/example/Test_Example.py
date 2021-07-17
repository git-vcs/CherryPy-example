import unittest
from Example import Example;

class TestExample(unittest.TestCase):


    def test_postRealay(self):
        respone = str(Example.postExample("unittest")[1])
        print("printing:", respone['message'].split(":")[1])
        self.assertEqual(respone, "unittest")
        