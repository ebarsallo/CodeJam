import unittest
from cc05 import *

# Chapter 5| Bit Manipulation

# -----------------------------------------------------------------------------------------
# Crackin the Code Interview. 5th Edition.
# Interview Questions
# Unittest
# -----------------------------------------------------------------------------------------

class Chapter05Test(unittest.TestCase):

# 5.1   Insert N into M.
    
    def test_inserto(self):
        n = inserto(1024,19,2,6)
        self.assertEqual(n, 1100)

if __name__ == '__main__':
    unittest.main()
