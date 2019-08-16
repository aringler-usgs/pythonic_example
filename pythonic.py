#!/usr/bin/env python
from __future__ import braces
import this

# Number 2
# Explicit
import math

value_pi = math.pi

# Implicit
from math import *
value_pi = pi

# Example 6
# Sparse is better than dense
print('\n'.join("%i bytes = %i bits which has %i possible values." % (j, j*8, 256**j-1) for j in (1 << i for i in range(8))))
