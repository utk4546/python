# Python Operators - basic examples

# 1. Arithmetic Operators
a = 10
b = 3
print(a + b)   # addition -> 13
print(a // b)  # floor division -> 3 (decimal hata deta hai)


# 2. Assignment Operators
x = 5
x += 2   # same as x = x + 2
print(x) # 7


# 3. Comparison Operators
print(5 > 3)    # True (5 bada hai 3 se)
print(5 == 5)   # True (dono equal hain)


# 4. Conditional (Ternary)
n = 4
result = "Even" if n % 2 == 0 else "Odd"
print(result)   # Even


# 5. Logical Operators
print(5 > 3 and 2 < 1)  # False (ek condition false hai)


# 6. Bitwise Operators
print(5 & 3)  # AND -> 1
print(5 | 3)  # OR  -> 7


# 7. Membership Operators
nums = [1, 2, 3]
print(3 in nums)  # True (3 list me hai)


# 8. Identity Operators
a = [1, 2]
b = a
print(a is b)  # True (dono same object ko point kar rahe hain)

a=5
b=5.0
c=5
print(a is b) # false (q ki a ur b dono alag alag memory location ko indicate kr rhe h )
# a=5
# >>> b=5.0
# >>> print(a is b)
# False