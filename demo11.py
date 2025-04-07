from collections import ChainMap

dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4}
chain = dict1 | dict2
# chain = ChainMap(dict1, dict2)
# print('x:', chain)  # 1
# print(chain['y'])
# print all keys y 
print(list(chain.keys()))
# print all values y
print(list(chain.values()))
# traversal for chain
for key, value in chain.items():
    print(key, value)