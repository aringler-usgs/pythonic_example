#!/usr/bin/env python
#from __future__ import braces
import this
import numpy as np
import antigravity
# James is responsible for antigravity

# Various examples from different places for a tutorial on being more pythonic

# Number 1 and number 10
print('############################  Examples 1 and 10 ################')
print('Beautiful is better than ugly.')
print('Errors should never pass sielently.')
colors = ['red', 'green', 'blue', 'yellow']

# Bad
for i in range(len(colors), -1, -1):
    try:
        print(colors[i])
    except:
        pass

# Good
for color in reversed(colors):
    print(color)

# Don't let exceptions pass silently.  Try to avoid indexing when you can itterate over it

print('############################  Example 2 ################')
print('Explicit is better than implicit.')
# Number 2
# Explicit
import math

value_pi = math.pi

# Implicit
from math import *
value_pi = pi

print('############################  Example 3 ################')
print('Simple is better than complex')


class acolor:

    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


blah = acolor('red')
print(blah)
print(blah.get_color())
# Don't use oop to do simple procedural tasks

# Less code == less confusion == more clarity

# When simple is not possible, then complex is better than complicated
print('############################  Example 4 ################')
print('Complex is better than complicated.')
# Complicated
val = [1, 2, 3, 4, 5, 6]
double = list(map(lambda x: x * 2, val))
print(double)

# Complex
val = np.asarray(val)
print(list(val*2))

print('############################  Example 5 ################')
print('Flat is better than nested.')

for i in range(10):
    for j in range(i):
        print(i, end='')

    print()

for i in range(1, 10):
    print(str(i)*i)


print('############################  Example 6 and 7 ################')
print('Sparse is better than nested.')
print('Readability counts.')
print('\n'.join("%i bytes = %i bits which has %i possible values." %
      (j, j*8, 256**j-1) for j in (1 << i for i in range(8))))

print('############################  Example 12 ################')
print('In the face of ambiguity, refuse the temptation to guess.')

# You need to know the types you are using and
# how various things change based on type
numbers = range(10)
numbers = [*numbers]

print(numbers*10)
print(np.asarray(numbers)*10)

print('############################  Examples 15 and 16 ################')
print('Now is better than never.')
print('Although never is often better than *right* now.')

# Write good code the first time, but don't fixate
# on writing code so carefully it never gets done.

# Go to https://github.com/aringler-usgs/HVratios to see an example.

# 20 minutes of planning would have saved 10+ hours of coding.
# Don't make intellectual debt at the cost of getting something done.

print('############################  Example 19 ################')
print('Namespaces are one honking great idea -- let\'s do more of those!')


# Use modules, use functions, import your own modules.
def outer_function():
    # variable a in the outer_function local name space
    a = 20

    def inner_function():
        # variable in the inner function namespace
        a = 30
        print('a =', a)

    inner_function()
    print('a', a)


# Global name space
a = 10
outer_function()
print('a =', a)
