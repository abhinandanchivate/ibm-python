import pandas as pd
from collections import namedtuple

df = pd.read_excel('tuple_data.xlsx')
df['Attributes'] = df['Attributes'].apply(lambda x: x.strip("[]").replace("'", "").split(", "))

named_tuple_classes = {}

for index, row in df.iterrows():
    tuple_name = row['TupleName']
    attributes = row['Attributes']
    named_tuple_class = namedtuple(tuple_name, attributes)
    named_tuple_classes[tuple_name] = named_tuple_class

print("Named Tuples Created:")
for name, cls in named_tuple_classes.items():
    print(f"- {name}: {cls._fields}")

Person = named_tuple_classes['Person']
person_instance = Person(name="John Doe", age=30, gender="Male", email="johndoe@example.com", phone="123-456-7890")

print("\nExample Person Instance:")
print(person_instance)
