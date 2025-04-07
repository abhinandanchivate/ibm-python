from collections import namedtuple

# Define a NamedTuple
Person = namedtuple('Person', ['name', 'age', 'gender'])

# Create instances
person1 = Person(name="Alice", age=30, gender="Female")
person2 = Person(name="Bob", age=25, gender="Male")

print(person1.name)
print(person2.age)
print(person1)
