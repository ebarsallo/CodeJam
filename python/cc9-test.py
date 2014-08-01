import unittest
from cc9 import *

# Chapter 9| Recursion and Dynamic Programming

# -----------------------------------------------------------------------------------------
# Crackin the Code Interview. 5th Edition.
# Interview Questions
# Unittest
# -----------------------------------------------------------------------------------------

# 9.1   A child is running up a staircase with n steps, and can hop either 1 step, 2 steps,
#       or 3 steps at a time. Implement a method to count how many possible ways the
#       child can run up the stairs.

class Chapter9Test(unittest.TestCase):
    
    def test_count_step(self):
        ns = [1, 2, 3, 4] # Number of steps
        ne = [1, 2, 4, 7] # Expected ways to run up the stairs

        for i in ns:
            n = i
            M = [0 for x in range (n+1)]

            steps = count_step(n, M)
            self.assertEqual(steps, ne[i-1])

if __name__ == '__main__':
    unittest.main()
