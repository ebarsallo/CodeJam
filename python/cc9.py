# Chapter 9| Recursion and Dynamic Programming
from math import factorial

# -----------------------------------------------------------------------------------------
# Crackin the Code Interview. 5th Edition.
# Interview Questions
# Solutions
# -----------------------------------------------------------------------------------------

# 9.1   A child is running up a staircase with n steps, and can hop either 1 step, 2 steps,
#       or 3 steps at a time. Implement a method to count how many possible ways the
#       child can run up the stairs.

def count_step(n, M):
    if n == 0:
        return 1
    elif n < -1:
        return 0
    elif M[n]:
        return M[n]
    else:
        M[n] = count_step (n-3, M) + count_step (n-2, M) + count_step (n-1, M)
        return M[n]

# 9.2   Imagine a robot sitting on the upper left corner of an X by Y grid. The robot can
#       only move in two directions: right and down. How many possible paths are there
#       for the robot to go from (0,0) to (X,Y)?
#       FOLLOW UP
#       Imagine certain spots are "off limits", such that the robot cannot step on them.
#       Design an algorithm to find a path for the robot from the top left to the bottom
#       right.

# Path lenght: x + y, using combination formula the possible paths will follows the
# diff possible combination of x or y given a (x + y).
def robot(x, y):
    return factorial (x + y) / factorial (x) / factorial (y)

# FOLLOW UP:
# Check if a specific cell (x,y) is free 
def is_free_cell(x,y, BLQ):
    if (x,y) in BLQ:
        return False
    else:
        return True

# We go from x,y to 0,0
def robot_followup(x, y, path, M, BLQ):

    p = (x,y)                               # Point
    if p in M:                              # Memory (cache), p has been already visited
        return M[p]
    
    if x == 0 and y == 0:                   # Path found!
        return True

    success = False
    if x > 0 and is_free_cell (x-1,y, BLQ): # Go LEFT (in fact: RIGHT)
        success = robot_followup (x-1, y, path, M, BLQ)

    if not success:                         # Go UP   (in fact: DOWN)
        if y > 0 and is_free_cell (x,y-1, BLQ):    
            success = robot_followup (x, y-1, path, M, BLQ)

    if success:                             # Add to path
        path.append(p)

    M[p] = success                          # Save result (success) in cache
    return success


# 9.3   A magic index in an index A[0..n-1] is defined to be an index such that A[i]
#       = i. Given a sorted array of distinct integers, write a method to find a magic
#       index, if one exists, in array A.
#       FOLLOW UP
#       What if the values are not distinct?

#Answer:
#Just simple brute force (getting GIT ready and testing python)

from array import *
A = array("i", [1,2,3,4,5,6,7,8])
i = 0
for a in A:
  if A[i]==a:
    print "There exist at least this magic index: %s" %i
  else:
    i=i+1


