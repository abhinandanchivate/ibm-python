from collections import Counter


# list of elements
elements = ['a', 'b', 'c', 'a', 'b', 'a']
# create a counter object
counter = Counter(elements)
# print the count of each element
print("Count of each element:", counter)
# get the most common elements
most_common = counter.most_common(2)
print("Most common elements:", most_common)
# get the count of a specific element
count_a = counter['z']
print("Count of 'a':", count_a)
# count words in a paragraph
