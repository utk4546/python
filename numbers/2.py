

# PYTHON NUMBERS - COMPLETE PRACTICE CODE

print("===== 1. PYTHON NUMBER TYPES =====")

# Integer: Whole numbers
a = 10
b = -5
print("Integer:", a, b)

# Float: Decimal numbers
x = 8.9
y = 2.5
print("Float:", x, y)

# Complex: Real + imaginary part
z = 3 + 4j
print("Complex:", z)

print("\n===== 2. ARITHMETIC OPERATORS =====")

a = 14
b = 5

print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Power (**):", a ** b)

print("\n===== 3. NEGATIVE NUMBERS =====")

print("-17 // 5 =", -17 // 5)
print("-17 % 5 =", -17 % 5)

print("-11 // 3 =", -11 // 3)
print("-11 % 3 =", -11 % 3)

# Floor division rounds down toward negative infinity.
# For integers: a == (a // b) * b + (a % b)

print("\n===== 4. OPERATOR PRECEDENCE =====")

print("2 + 3 * 2 =", 2 + 3 * 2)
print("2 + 3 * 2 ** 3 =", 2 + 3 * 2 ** 3)
print("4 + 3 * 2 ** 2 =", 4 + 3 * 2 ** 2)
print("7 + 2 * (6 - 3) =", 7 + 2 * (6 - 3))

# Power is evaluated from right to left.
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)
print("(2 ** 3) ** 2 =", (2 ** 3) ** 2)

print("\n===== 5. TYPE CONVERSION =====")

number = 8.9

print("Original:", number)
print("int():", int(number))
print("float():", float(5))
print("complex():", complex(4))

# int() removes the decimal part; it does not round.
print("int(-8.9):", int(-8.9))

print("\n===== 6. ROUNDING =====")

print("round(8.765, 2):", round(8.765, 2))
print("round(8.765, 1):", round(8.765, 1))
print("round(8.765):", round(8.765))

print("\n===== 7. ABSOLUTE VALUE =====")

print("abs(-15):", abs(-15))
print("abs(-8.5):", abs(-8.5))

print("\n===== 8. USEFUL NUMBER FUNCTIONS =====")

print("Maximum:", max(10, 25, 7, 40))
print("Minimum:", min(10, 25, 7, 40))
print("Sum:", sum([10, 20, 30, 40]))

print("\n===== 9. CHECKING DATA TYPES =====")

print(type(10))
print(type(8.9))
print(type(3 + 4j))

print("\n===== 10. MINI CALCULATOR =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Remainder:", num1 % num2)
else:
    print("Cannot divide by zero!")

print("\n===== PRACTICE COMPLETE! =====")
