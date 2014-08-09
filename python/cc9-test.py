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

    def test_robot(self):
        n = robot(2,1)
        self.assertEqual(n, 3)

    def test_robot_followup(self):
        path  = []
        cache = dict()
        bloq  = [(1,1),(1,2)]
        robot_followup(2,3, path, cache, bloq)        

        # Resulted path should not contain any blocked cell
        for i in path:
            self.assertTrue(i not in bloq)

        # Resulted path sould be any of the possible options
        exp1 = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]
        exp2 = [(1, 0), (2, 0), (3, 0), (3, 1), (2, 3)]
        self.assertTrue(exp1 == path or exp2 == path)
        

if __name__ == '__main__':
    unittest.main()
