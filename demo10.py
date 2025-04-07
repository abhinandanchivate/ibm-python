from collections import OrderedDict

# Create an ordered dictionary
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

print(ordered_dict)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Deleting and reinserting an element
ordered_dict.pop('b')
ordered_dict['b'] = 4

print(ordered_dict)  # OrderedDict([('a', 1), ('c', 3), ('b', 4)])
