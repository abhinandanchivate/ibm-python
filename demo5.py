from collections import deque

# Create a deque
my_deque = deque(['a', 'b', 'c', 'd'])
print("Original deque:", my_deque)
# Append elements to the right
my_deque.append('e')
print("After appending 'e':", my_deque)
# Append elements to the left
my_deque.appendleft('z')
print("After appending 'z' to the left:", my_deque)
# Pop elements from the right
popped_right = my_deque.pop()
print("Popped from the right:", popped_right)
print("After popping from the right:", my_deque)
# Pop elements from the left
popped_left = my_deque.popleft()
print("Popped from the left:", popped_left)
print("After popping from the left:", my_deque)
