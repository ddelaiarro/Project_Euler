#----------------------------------------------------------------------------
# Name:         Project Euler
# Purpose:      Problem 2
#
# Author:       D. DeLaiarro
#
# Created:      31-Dec-2022
#----------------------------------------------------------------------------
#
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

import time
start = time.time()

a = 1
b = 2
c = a + b
sum = 2

while c <= 4000000:
  c = a + b
#  print(c)
  a = b
  b = c
  if c % 2 == 0:
    sum = sum + c

elapsed = (time.time() - start)
print(sum)

print()
print("This code took",elapsed,"seconds to execute")