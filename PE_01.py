#----------------------------------------------------------------------------
# Name:         Project Euler
# Purpose:      Problem 1
#
# Author:       D. DeLaiarro
#
# Created:      31-Dec-2022
#----------------------------------------------------------------------------
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

import time
start = time.time()

sum = 0
for i in range (1,1000):
  if i % 3 == 0 or i % 5 == 0:
    sum = sum + i

elapsed = (time.time() - start)
print(sum)

print()
print("This code took",elapsed,"seconds to execute")