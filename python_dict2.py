# ================================================
# ✅ Python Dictionary Operations (Complete Notes)
# ================================================

# 1. Creating a Dictionary
student = {"name": "Alice", "roll": 101, "marks": 95}
print("1. Dictionary:", student)

# 2. Accessing Values
print("2. Access name:", student["name"])
print("   Access roll (using get):", student.get("roll"))

# 3. Changing Values
student["marks"] = 98
print("3. Updated marks:", student)

# 4. Adding New Key-Value Pair
student["grade"] = "A+"
print("4. Added grade:", student)

# 5. Removing Items
removed_roll = student.pop("roll")  # Removes key 'roll'
print("5. Removed roll:", removed_roll, "| Dict:", student)

student["temp"] = "remove_me"
student.popitem()  # Removes last inserted item
print("   After popitem:", student)

del student["name"]  # Removes key 'name'
print("   After del:", student)

student.clear()  # Clears all items
print("   After clear:", student)

# Resetting dictionary for further examples
student = {"name": "Alice", "roll": 101, "marks": 95}

# 6. Length of Dictionary
print("6. Length of dict:", len(student))

# 7. Check if Key Exists
print("7. Is 'name' in dict?:", "name" in student)
print("   Is 'email' not in dict?:", "email" not in student)

# 8. Looping Through Dictionary
print("8. Looping using keys:")
for key in student:
    print(f"   {key} -> {student[key]}")

print("   Looping using items():")
for k, v in student.items():
    print(f"   {k} = {v}")

# 9. Dictionary Methods
print("9. keys():", student.keys())
print("   values():", student.values())
print("   items():", student.items())

copy_dict = student.copy()
print("   Copied dict:", copy_dict)

student.update({"city": "Pune", "marks": 90})
print("   After update:", student)

# 10. Nested Dictionary
data = {
    "student1": {"name": "Alice", "marks": 95},
    "student2": {"name": "Bob", "marks": 88}
}
print("10. Nested dictionary:", data)

# 11. Creating Dictionary from List of Tuples
pairs = [("a", 1), ("b", 2)]
dict_from_list = dict(pairs)
print("11. Dict from list of tuples:", dict_from_list)

# 12. Using fromkeys()
keys = ["name", "age", "marks"]
dict_from_keys = dict.fromkeys(keys, None)
print("12. Fromkeys:", dict_from_keys)

# 13. Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
print("13. Dict comprehension (squares):", squares)

# 14. Convert Dictionary to JSON
import json
json_data = json.dumps(student)
print("14. Dict to JSON:", json_data)

# 15. Convert JSON to Dictionary
original_dict = json.loads(json_data)
print("15. JSON to dict:", original_dict)

# =======================================================
# ✅ Python Dictionary Methods (Complete Notes & Code)
# =======================================================

# 1. Creating a Dictionary
student = {"name": "Alice", "age": 22, "course": "Computer Science"}
print("1. Dictionary:", student)

# 2. clear() - Removes all elements from the dictionary
student.clear()
print("2. After clear():", student)

# 3. copy() - Returns a copy of the dictionary
student = {"name": "Alice", "age": 22, "course": "Computer Science"}
student_copy = student.copy()
print("3. Copied dictionary:", student_copy)

# 4. fromkeys() - Returns a dictionary with the specified keys and value
keys = ["name", "age", "course"]
default_value = "Unknown"
new_dict = dict.fromkeys(keys, default_value)
print("4. Dictionary using fromkeys():", new_dict)

# 5. get() - Returns the value of the specified key
print("5. Get value of 'name':", student.get("name"))  # Existing key
print("   Get value of 'address' (non-existing):", student.get("address", "Not found"))

# 6. items() - Returns a list of tuples with key-value pairs
print("6. Items (key-value pairs):", student.items())

# 7. keys() - Returns a list of dictionary's keys
print("7. Keys:", student.keys())

# 8. pop() - Removes an element with the specified key
removed_value = student.pop("age", "Not found")  # Removes 'age'
print("8. Popped value (age):", removed_value)
print("   Dictionary after pop():", student)

# 9. popitem() - Removes the last inserted key-value pair
last_item = student.popitem()  # Removes the last item
print("9. Popped last item:", last_item)
print("   Dictionary after popitem():", student)

# 10. setdefault() - Returns the value of the specified key. If the key does not exist, inserts it with the specified value
default_value = student.setdefault("address", "Unknown Address")
print("10. Setdefault 'address':", default_value)
print("   Dictionary after setdefault:", student)

# 11. update() - Updates the dictionary with the specified key-value pairs
student.update({"age": 23, "city": "New York"})
print("11. Dictionary after update:", student)

# 12. values() - Returns a list of all the values in the dictionary
print("12. Values in dictionary:", student.values())

# 13. Nested Dictionary Example
employee = {
    "name": "Bob",
    "details": {
        "age": 30,
        "position": "Software Engineer"
    }
}
print("13. Nested dictionary:", employee)
print("   Access nested value:", employee["details"]["position"])  # Access nested dictionary value
