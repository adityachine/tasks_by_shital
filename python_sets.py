new_sets ={
    "Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple",
    "Watermelon", "Papaya", "Guava", "Lychee", "Strawberry", "Blueberry",
    "Raspberry", "Blackberry", "Peach", "Plum", "Pear", "Kiwi",
}
print(type(new_sets))
print(len(new_sets))
 
for x in new_sets:
    print(x)

#Add Set Items
new_sets.add("Chiku")
print(new_sets)

thisdict = {}

# ===================================================
# ✅ Python Set Operations (Complete Notes & Code)
# ===================================================

# 1. Creating Sets
fruits = {"apple", "banana", "cherry"}
print("1. Set:", fruits)

# 2. Adding Elements
fruits.add("date")
print("2. Add 'date':", fruits)

# 3. Adding Multiple Elements
fruits.update(["fig", "grape"])
print("3. Update with multiple items:", fruits)

# 4. Removing Elements
fruits.remove("banana")  # Error if not exists
print("4. Remove 'banana':", fruits)

fruits.discard("kiwi")  # No error if not exists
print("   Discard 'kiwi' (safe):", fruits)

popped = fruits.pop()  # Removes random item
print("   Popped item:", popped)
print("   Set after pop:", fruits)

# 5. Clearing Set
temp = fruits.copy()
temp.clear()
print("5. Cleared set:", temp)

# 6. Copying Set
copied = fruits.copy()
print("6. Copied set:", copied)

# 7. Set Length
print("7. Length of set:", len(fruits))

# 8. Looping Through Set
print("8. Looping through set:")
for item in fruits:
    print("   ", item)

# 9. Membership Test
print("9. Is 'apple' in set?:", "apple" in fruits)

# 10. Set Union
a = {1, 2, 3}
b = {3, 4, 5}
print("10. Union of sets:", a.union(b))

# 11. Set Intersection
print("11. Intersection of sets:", a.intersection(b))

# 12. Set Difference
print("12. a - b (difference):", a.difference(b))
print("    b - a (difference):", b.difference(a))

# 13. Symmetric Difference
print("13. Symmetric difference:", a.symmetric_difference(b))

# 14. Update Variants
a1 = {1, 2, 3}
b1 = {3, 4, 5}
a1.intersection_update(b1)
print("14. Intersection update (a1):", a1)

# 15. Subset and Superset Check
x = {1, 2}
y = {1, 2, 3}
print("15. x ⊆ y:", x.issubset(y))
print("    y ⊇ x:", y.issuperset(x))

# 16. Disjoint Sets
a = {1, 2}
b = {3, 4}
print("16. Are a & b disjoint?:", a.isdisjoint(b))

# 17. Set from List
list_data = [1, 2, 2, 3]
unique = set(list_data)
print("17. Set from list (removes duplicates):", unique)

# 18. Frozen Set (immutable)
frozen = frozenset(["apple", "banana", "cherry"])
print("18. Frozen set:", frozen)

# 19. Set Comprehension
squares = {x**2 for x in range(6)}
print("19. Set comprehension (squares):", squares)

# 20. Removing duplicates from list using set
dup_list = [1, 2, 2, 3, 3, 4]
no_duplicates = list(set(dup_list))
print("20. Remove duplicates:", no_duplicates)
