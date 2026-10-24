# ==========================================
# 1. INITIALIZATION & ADDING ELEMENTS
# ==========================================
print("--- 1. Creation and Adding Elements ---")
# Creating a set
fruits = {"apple", "banana", "cherry"}
print(f"Initial set: {fruits}")

# Add a single element
fruits.add("orange")
print(f"After add('orange'): {fruits}")

# Add multiple elements (using a list)
fruits.update(["mango", "grapes"])
print(f"After update() with list: {fruits}\n")


# ==========================================
# 2. REMOVING ELEMENTS
# ==========================================
print("--- 2. Removing Elements ---")
# remove(): Deletes an item, throws KeyError if not found
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

# discard(): Deletes an item safely, does NOT throw error if missing
fruits.discard("watermelon") 
print(f"After discard('watermelon') [No Error]: {fruits}")

# pop(): Removes and returns a random element
popped_item = fruits.pop()
print(f"Popped item: {popped_item}")
print(f"Set after pop(): {fruits}")

# clear(): Empties the entire set
temp_set = {"x", "y", "z"}
temp_set.clear()
print(f"After clear(): {temp_set}\n")


# ==========================================
# 3. MATHEMATICAL SET OPERATIONS
# ==========================================
print("--- 3. Mathematical Operations ---")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(f"Set A: {setA}")
print(f"Set B: {setB}")

# UNION (All items from both sets)
print(f"Union (A | B): {setA.union(setB)}")

# INTERSECTION (Common items)
print(f"Intersection (A & B): {setA.intersection(setB)}")

# DIFFERENCE (Items in A but not in B)
print(f"Difference (A - B): {setA.difference(setB)}")

# SYMMETRIC DIFFERENCE (Items in either A or B, but NOT both)
print(f"Symmetric Difference (A ^ B): {setA.symmetric_difference(setB)}\n")


# ==========================================
# 4. ALL IN-PLACE UPDATE OPERATIONS 
# ==========================================
print("--- 4. All In-Place Update Operations ---")
# ये सभी मेथड्स ओरिजिनल सेट को सीधे बदल (modify) देते हैं

# A. update() या |= (Union Update - सब कुछ जोड़ना)
base_set = {1, 2}
base_set.update({3, 4})
print(f"After update() / Union Update: {base_set}") # Output: {1, 2, 3, 4}

# B. difference_update() या -= (Difference Update - हटाना)
set_diff = {1, 2, 3, 4}
set_diff.difference_update({3, 4, 5})
print(f"After difference_update(): {set_diff}") # Output: {1, 2}

# C. intersection_update() या &= (Intersection Update - सिर्फ कॉमन रखना)
set_inter = {1, 2, 3, 4}
set_inter.intersection_update({3, 4, 5})
print(f"After intersection_update(): {set_inter}") # Output: {3, 4}

# D. symmetric_difference_update() या ^= (Symmetric Difference Update - कॉमन को छोड़कर बाकी रखना)
set_sym = {1, 2, 3, 4}
set_sym.symmetric_difference_update({3, 4, 5})
print(f"After symmetric_difference_update(): {set_sym}\n") # Output: {1, 2, 5}


# ==========================================
# 5. SUBSETS, SUPERSETS & DISJOINT
# ==========================================
print("--- 5. Comparison Operations ---")
small_set = {1, 2}
big_set = {1, 2, 3, 4}
other_set = {5, 6}

print(f"Is small_set subset of big_set? {small_set.issubset(big_set)}")
print(f"Is big_set superset of small_set? {big_set.issuperset(small_set)}")
print(f"Are big_set and other_set disjoint (no common items)? {big_set.isdisjoint(other_set)}\n")


# ==========================================
# 6. BULK CONVERSIONS & MEMBERSHIP
# ==========================================
print("--- 6. Conversion & Membership ---")
# Membership test (Very fast in sets)
print(f"Is 2 in big_set? {2 in big_set}")

# Converting list with duplicates to a unique set
numbers_list = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers_list)
print(f"List converted to Set (duplicates removed): {unique_numbers}")
