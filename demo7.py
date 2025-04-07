# defaultdict : dictionary with default values

## A defaultdict is a subclass of the regular Python dictionary (dict) that provides a default value for non-existent keys. If you try to access or modify a key that doesn't exist, it automatically initializes it with a default value instead of raising a KeyError.
from collections import defaultdict
d = defaultdict(list)

d['fruits'].append('apple')
d['fruits'].append('banana')
d['vegetables'].append('carrot')
print(d)  # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})