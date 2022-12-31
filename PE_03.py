#----------------------------------------------------------------------------
# Name:         Project Euler
# Purpose:      Problem 3
#
# Author:       D. DeLaiarro
#
# Created:      31-Dec-2022
#----------------------------------------------------------------------------
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import time
import math

start = time.time()

num = 600851475143
if num % 2 == 0:
  lpf = 2                                     # lpf = largest prime factor
else:
  for i in range (3,int(math.sqrt(num)+1),2):
    if num % i == 0:                          # determines if i is a factor
      fac = i        
      x = 0                                   # reset x to zero
      for j in range(2, int(fac/2)+1):        # determines if fac is prime 
        if fac % j == 0:                      
          x += 1
      if x == 0:                              # if x = 0, fac is prime
        lpf = fac                             # fac becomes largest prime factor

elapsed = (time.time() - start)
print(lpf)

print()
print("This code took",elapsed,"seconds to execute")