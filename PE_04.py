#----------------------------------------------------------------------------
# Name:         Project Euler
# Purpose:      Problem 4
#
# Author:       D. DeLaiarro
#
# Created:      01-Jan-2023
#----------------------------------------------------------------------------
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import time

start = time.time()

ans = 0

for i in range(1000,500,-1):
  for j in range(1000,500,-1):

    a = i * j
    a_str = str(a)
    a_str_inv = a_str[::-1]
    if a_str == a_str_inv and ans < a:
      ans = a

elapsed = (time.time() - start)
print(ans)

print()
print("This code took",elapsed,"seconds to execute")