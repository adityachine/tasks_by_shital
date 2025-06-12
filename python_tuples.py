thistuple = (
    "Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple",
    "Watermelon", "Papaya", "Guava", "Lychee", "Strawberry", "Blueberry",
    "Raspberry", "Blackberry", "Peach", "Plum", "Pear", "Kiwi",
    "Cherry", "Pomegranate", "Dragonfruit", "Fig", "Avocado", "Jackfruit",
    "Coconut", "Apricot", "Tangerine", "Mulberry", "Cranberry", "Starfruit"
)
print(thistuple[-4:-1])
print(thistuple[0])
print(thistuple[-1])
print(thistuple[-4:-1])

if "Apple" in thistuple:
    print("the item is in the list")
    
print(len(thistuple))

#membership test 

print("Plum" in thistuple)
print("Plum" not in thistuple)

#iteration (looping through a tuple)

for x in thistuple:
    print(x)
    
#concatenation that means joing of the two or more tuples 

thistuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
concatenated_tuple = thistuple + thistuple2
print(concatenated_tuple)

#nastedtuples
"""print(tuple_name[2][1])
this actully means 2 is the 2 tuple into the tuple and form nasted tuple 2 we have o print 
item that is at the indexed value 1
"""
"""    
#immutability check 
thistuple[0]= "newelement"
"""
for i in range(len(concatenated_tuple)):
    print(concatenated_tuple[i])
    
    
# ==================================================
# ✅ Python Tuple Operations (Complete Notes & Code)
# ==================================================

# 1. Creating Tuples
fruits = ("apple", "banana", "cherry", "date")
print("1. Tuple:", fruits)

# 2. Accessing Elements
print("2. First fruit:", fruits[0])
print("   Last fruit:", fruits[-1])

# 3. Slicing Tuples
print("3. Slice [1:3]:", fruits[1:3])  # banana to cherry

# 4. Looping Through Tuple
print("4. Looping through tuple:")
for item in fruits:
    print("  ", item)

# 5. Checking Existence
print("5. Is 'banana' in tuple?:", "banana" in fruits)

# 6. Tuple Length
print("6. Length of tuple:", len(fruits))

# 7. Single Element Tuple (MUST use comma)
one_item = ("mango",)
print("7. One-item tuple:", one_item)

# 8. Tuple with Different Data Types
mixed = ("John", 25, 5.5, True)
print("8. Mixed type tuple:", mixed)

# 9. Nested Tuple
nested = (("apple", "banana"), (1, 2, 3))
print("9. Nested tuple:", nested)
print("   Access nested item:", nested[0][1])  # banana

# 10. Concatenation of Tuples
t1 = (1, 2)
t2 = (3, 4)
combined = t1 + t2
print("10. Concatenated tuple:", combined)

# 11. Repetition
repeat = ("Hi",) * 3
print("11. Repeated tuple:", repeat)

# 12. Count occurrences
colors = ("red", "blue", "red", "green", "red")
print("12. Count of 'red':", colors.count("red"))

# 13. Index of Element
print("13. Index of 'green':", colors.index("green"))

# 14. Converting List to Tuple
list_data = ["a", "b", "c"]
tuple_data = tuple(list_data)
print("14. List to tuple:", tuple_data)

# 15. Tuple Unpacking
person = ("Alice", 22, "Engineer")
name, age, profession = person
print("15. Unpacked values -> Name:", name, "Age:", age, "Profession:", profession)

# 16. Using tuple() constructor
numbers = tuple([1, 2, 3, 4])
print("16. Tuple using constructor:", numbers)

# 17. Immutable nature (demonstration)
try:
    fruits[0] = "orange"  # This will throw error
except TypeError as e:
    print("17. Tuple is immutable:", e)

# 18. Loop with index (using enumerate)
print("18. Loop with index:")
for i, v in enumerate(fruits):
    print(f"   Index {i} -> {v}")

# 19. Tuple vs List (Memory Efficient Demo)
import sys
list_ex = [1, 2, 3]
tuple_ex = (1, 2, 3)
print("19. Memory size of list:", sys.getsizeof(list_ex))
print("    Memory size of tuple:", sys.getsizeof(tuple_ex))

# 20. Tuple inside a list
combo = [("apple", 10), ("banana", 20)]
print("20. Tuple inside list:", combo)

