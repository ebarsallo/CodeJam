# Chapter 5| Bit Manipulation

# -----------------------------------------------------------------------------------------
# Crackin the Code Interview. 5th Edition.
# Interview Questions
# Solutions
# -----------------------------------------------------------------------------------------

# 5.1   You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write
#       a methodto insert M into N such that M starts at bit j and ends at bit i. You can
#       assume that the bits j throught i have enough space to fit all of M. That is, if
#       M = 10011, you can assume that there are at least 5 bits between j and i. You
#       would not, for example, have j = 3 and i = 2, because M could not fully fit
#       between bit 3 and bit 2.
#
#       EXAMPLE
#       Input:   N = 10000000000, M = 10011, i = 2, j = 6
#       Output:  N = 10001001100

# 5.2   Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
#       print the binary representation if the number cannot be represented accurately
#       in binary with at most 32 characters, print "ERROR".

# 5.8   A monocrhome screen is stored as a single array of bytes, allowing eight 
#       consecutive pixels to be stored in one byte. The screen has a width w, where w 
#       is divisible by 8 (that is, no byte will be split across rows). The height of 
#       the screen, of course, can be derived from the lenght of the array and the width. 
#       Implement a function drawHorizontalLine(byte[] screen, int width, int x1, int x2,
#       int y) which draws a horizontal line from (x1, y) to (x2, y).