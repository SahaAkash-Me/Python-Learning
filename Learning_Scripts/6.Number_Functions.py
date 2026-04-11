# ════════════════════════════════════════════════════════════════════════════════
# 📚 PYTHON NUMERIC DATA TYPES - COMPREHENSIVE LEARNING GUIDE
# ════════════════════════════════════════════════════════════════════════════════
#
# This document covers fundamental concepts of numeric types in Python, including:
# integers, floats, complex numbers, type conversion, arithmetic operations,
# and practical applications with the math and random modules.
#
# ════════════════════════════════════════════════════════════════════════════════
# 📑 TABLE OF CONTENTS (with line numbers for quick navigation)
# ════════════════════════════════════════════════════════════════════════════════
#
# 1️⃣  NUMERIC TYPES                                    [Lines 22-31]
# 2️⃣  TYPE CONVERSION                                  [Lines 34-49]
# 3️⃣  BASIC ARITHMETIC OPERATIONS                      [Lines 52-61]
# 4️⃣  COMPOUND ASSIGNMENT OPERATORS                    [Lines 64-78]
# 5️⃣  ABSOLUTE VALUE                                   [Lines 81-83]
# 6️⃣  ROUNDING AND MATH MODULE                         [Lines 86-97]
# 7️⃣  RANDOM NUMBER GENERATION                         [Lines 100-104]
# 8️⃣  CHECKING INTEGER VALUES                          [Lines 107-115]
# 9️⃣  TYPE CHECKING WITH isinstance()                  [Lines 118-121]
# 🔟  PYTHON CHALLENGE                                  [Lines 124-128]
#
# ════════════════════════════════════════════════════════════════════════════════


# ════════════════════════════════════════════════════════════════════════════════
# 1️⃣ NUMERIC TYPES
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Python has three main numeric types:
#    • int (integer) → Whole numbers without decimal point (positive, negative, zero)
#    • float (floating-point) → Numbers with decimal point
#    • complex (complex number) → Numbers with real and imaginary parts (a + bj)
#
# The type() function returns the data type of a variable.
# ════════════════════════════════════════════════════════════════════════════════

x = 5              # ➤ Integer: whole number
y = 5.7            # ➤ Float: decimal number
z = 2 + 3j         # ➤ Complex: real part (2) + imaginary part (3j)

print(type(x))  # ➜ <class 'int'>
print(type(y))  # ➜ <class 'float'>
print(type(z))  # ➜ <class 'complex'>


# ════════════════════════════════════════════════════════════════════════════════
# 2️⃣ TYPE CONVERSION
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Type conversion (also called "casting") allows you to convert one data type
# into another. Python provides built-in functions: int(), float(), complex()
#
# Key points:
#    • int() → Removes decimal part (truncates, doesn't round)
#    • float() → Converts to decimal format
#    • complex(real, imaginary) → Creates complex number from two integers
#
# Use cases: Converting user input (strings) to numbers, combining data types
# ════════════════════════════════════════════════════════════════════════════════

x = "24"           # ➤ String type (looks like a number but isn't)
print(type(x))     # ➜ <class 'str'>

x = int(x)         # ➤ Convert string "24" to integer 24
print(type(x))     # ➜ <class 'int'>
print(x * 3)       # ➜ 72 (Now we can do math with it)

# 🔹 Float to Integer conversion (truncates decimal part)
x = 3.14
print(int(x))      # ➜ 3 (decimal part removed, not rounded)

# 🔹 Integer to Float conversion
x = 3
print(float(x))    # ➜ 3.0 (adds .0 to make it float)

# 🔹 Complex number creation from real and imaginary parts
x = 3              # ➤ Real part
y = 4              # ➤ Imaginary part
print(complex(x, y))  # ➜ (3+4j) (creates complex number)


# ════════════════════════════════════════════════════════════════════════════════
# 3️⃣ BASIC ARITHMETIC OPERATIONS
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Python supports standard mathematical operations on numeric types.
# All operators follow mathematical precedence (PEMDAS/BODMAS).
#
# Operator Guide:
#    + → Addition (combine two numbers)
#    - → Subtraction (difference between two numbers)
#    * → Multiplication (product of two numbers)
#    / → True Division (always returns float, even if result is whole)
#    // → Floor Division (returns integer, rounds down)
#    % → Modulus (returns remainder after division)
#    ** → Exponentiation (raises to power)
#
# Important: / and // behave differently!
#    7 / 2 = 3.5 (float)
#    7 // 2 = 3 (integer, rounds down)
# ════════════════════════════════════════════════════════════════════════════════

print(2 + 3)       # ➜ 5 (Addition: 2 plus 3)
print(5 - 3)       # ➜ 2 (Subtraction: 5 minus 3)
print(4 * 2)       # ➜ 8 (Multiplication: 4 times 2)
print(7 / 2)       # ➜ 3.5 (True division: returns float)
print(7 // 2)      # ➜ 3 (Floor division: rounds down to nearest int)
print(9 % 2)       # ➜ 1 (Modulus: remainder of 9 ÷ 2)
print(2 ** 3)      # ➜ 8 (Exponentiation: 2 raised to power 3)


# ════════════════════════════════════════════════════════════════════════════════
# 4️⃣ COMPOUND ASSIGNMENT OPERATORS
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Compound assignment operators combine an arithmetic operation with assignment.
# They provide a shorthand way to modify a variable's value.
#
# Syntax: variable op= value is equivalent to: variable = variable op value
#
# Available operators:
#    += → Add and assign
#    -= → Subtract and assign
#    *= → Multiply and assign
#    /= → Divide and assign
#    //= → Floor divide and assign
#    %= → Modulus and assign
#    **= → Exponentiate and assign
#
# Benefit: Makes code more concise and readable
# ════════════════════════════════════════════════════════════════════════════════

x = 2              # ➤ Step 1: Initialize x with value 2
print(f"Initial x: {x}")

x += 3             # ➤ Step 2: x = x + 3 (add 3 to x)
print(f"After x += 3: {x}")  # ➜ 5

x -= 1             # ➤ Step 3: x = x - 1 (subtract 1 from x)
print(f"After x -= 1: {x}")  # ➜ 4

x *= 2             # ➤ Step 4: x = x * 2 (multiply x by 2)
print(f"After x *= 2: {x}")  # ➜ 8

x = 2              # ➤ Reset x for exponentiation example
x **= 3            # ➤ Step 5: x = x ** 3 (x raised to power 3)
print(f"After x **= 3: {x}")  # ➜ 8 (2 to the power of 3)


# ════════════════════════════════════════════════════════════════════════════════
# 5️⃣ ABSOLUTE VALUE
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# The abs() function returns the absolute value of a number.
# Absolute value is the distance from zero, always positive (or zero).
#
# Use cases:
#    • Finding magnitude without sign
#    • Error calculations (how far off you are)
#    • Distance measurements
#
# Formula: abs(x) = |x|
# Examples: abs(-5) = 5, abs(5) = 5, abs(0) = 0
# ════════════════════════════════════════════════════════════════════════════════

print(abs(2 - 10))  # ➜ 8 (absolute value of -8 is 8)


# ════════════════════════════════════════════════════════════════════════════════
# 6️⃣ ROUNDING AND MATH MODULE
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Python provides multiple ways to handle decimal precision and rounding.
#
# round() function (built-in):
#    • round(number) → Rounds to nearest whole number
#    • round(number, decimals) → Rounds to specified decimal places
#    • Uses "banker's rounding" (round half to even)
#
# math module functions (requires: import math):
#    • math.floor(x) → Rounds DOWN to nearest integer
#    • math.ceil(x) → Rounds UP to nearest integer
#    • math.trunc(x) → Removes decimal part (truncates)
#
# Key difference:
#    round(3.5) = 4, but round(2.5) = 2 (banker's rounding)
#    math.floor always goes down, math.ceil always goes up
# ════════════════════════════════════════════════════════════════════════════════

import math

price = 35.54879865  # ➤ Example: product price with many decimal places

# 🔹 round() function - standard rounding
print(round(price))      # ➜ 36 (rounds to nearest whole number)
print(round(price, 2))   # ➜ 35.55 (rounds to 2 decimal places)
print(round(price, 1))   # ➜ 35.5 (rounds to 1 decimal place)

# 🔹 math.floor() - always rounds DOWN
print(math.floor(price))  # ➜ 35 (removes everything after decimal)

# 🔹 math.ceil() - always rounds UP
print(math.ceil(price))   # ➜ 36 (goes to next whole number)

# 🔹 math.trunc() - removes decimal part (same as int())
print(math.trunc(price))  # ➜ 35 (truncates, doesn't round)
print(int(price))         # ➜ 35 (same result as trunc)


# ════════════════════════════════════════════════════════════════════════════════
# 7️⃣ RANDOM NUMBER GENERATION
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# The random module generates random numbers for simulations, games, testing.
#
# Common functions:
#    • random.random() → Random float between 0.0 and 1.0 (exclusive)
#    • random.randint(a, b) → Random integer between a and b (inclusive)
#    • random.choice(list) → Random element from a list
#    • random.shuffle(list) → Randomly reorder a list
#
# Use cases:
#    • Games (dice rolls, card draws)
#    • Simulations and statistical analysis
#    • Testing with random data
#
# Note: Not cryptographically secure; use secrets module for sensitive data
# ════════════════════════════════════════════════════════════════════════════════

import random

# 🔹 Generate random float between 0 and 1
print(random.random())       # ➜ Random float (example: 0.3729...)

# 🔹 Simulate a dice roll (integer from 1 to 6)
print(random.randint(1, 6))  # ➜ Random int (example: 4)


# ════════════════════════════════════════════════════════════════════════════════
# 8️⃣ CHECKING INTEGER VALUES
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# The is_integer() method checks if a float represents a whole number.
# This is useful when you have float data but need to know if it's actually integral.
#
# Important distinction:
#    • 7.0 is a float, but represents integer 7 → is_integer() = True
#    • 7.1 is a float that doesn't represent an integer → is_integer() = False
#    • This method only works on float objects, not on int
#
# Use cases:
#    • Data validation (checking if decimal input is actually whole)
#    • Deciding whether to display .0 or not
# ════════════════════════════════════════════════════════════════════════════════

# 🔹 Float that represents a whole number
x = 7.0
print(x.is_integer())  # ➜ True (7.0 is a whole number)

# 🔹 Float that doesn't represent a whole number
y = 7.1
print(y.is_integer())  # ➜ False (7.1 has decimal part)


# ════════════════════════════════════════════════════════════════════════════════
# 9️⃣ TYPE CHECKING WITH isinstance()
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# The isinstance() function checks if a variable is of a specific type.
# Returns True if the object is an instance of the class, False otherwise.
#
# Syntax: isinstance(object, classinfo)
#
# Advantages over type():
#    • More Pythonic way to check types
#    • Supports inheritance (important for OOP)
#    • More readable and explicit
#
# Common type checks:
#    isinstance(x, int) → Is x an integer?
#    isinstance(x, float) → Is x a float?
#    isinstance(x, str) → Is x a string?
#    isinstance(x, (int, float)) → Is x int or float?
# ════════════════════════════════════════════════════════════════════════════════

x = 70.4
print(isinstance(x, int))    # ➜ False (70.4 is not an integer)
print(isinstance(x, float))  # ➜ True (70.4 is a float)


# ════════════════════════════════════════════════════════════════════════════════
# 🔟 PYTHON CHALLENGE
# ════════════════════════════════════════════════════════════════════════════════
# 📌 CHALLENGE DESCRIPTION:
# Test your understanding of random numbers and modulus operator!
#
# Task:
#    1. Generate a random integer between 1 and 100
#    2. Check if the result is an even number
#    3. Print both the number and whether it's even
#
# Hint:
#    • Use random.randint() for step 1
#    • Use modulus (%) operator: if number % 2 == 0, it's even
#    • Use if-else for step 2
#
# Challenge extension (advanced):
#    • How many random numbers do you need to generate before you get an even?
#    • Generate 10 random numbers and count how many are even
# ════════════════════════════════════════════════════════════════════════════════

# 💡 Solution approach:
random_number = random.randint(1, 100)  # ➤ Generate random int (1-100)

# 🔹 Check if even: number % 2 == 0 (even), number % 2 == 1 (odd)
if random_number % 2 == 0:
    print(f"✅ {random_number} is EVEN")  # ➜ Even number
else:
    print(f"❌ {random_number} is ODD")   # ➜ Odd number

# 🔹 Extended challenge: Generate and analyze 10 random numbers
print("\n📊 Extended Challenge - Analyzing 10 Random Numbers:")
even_count = 0  # ➤ Counter for even numbers
odd_count = 0   # ➤ Counter for odd numbers

for i in range(10):
    num = random.randint(1, 100)
    if num % 2 == 0:
        even_count += 1
        print(f"   #{i+1}: {num} → EVEN ✓")
    else:
        odd_count += 1
        print(f"   #{i+1}: {num} → ODD ✗")

print(f"\n📈 Summary: {even_count} even, {odd_count} odd out of 10 numbers")


# ════════════════════════════════════════════════════════════════════════════════
# 🎓 KEY TAKEAWAYS & SUMMARY
# ════════════════════════════════════════════════════════════════════════════════
#
# ✓ Python has 3 main numeric types: int, float, complex
# ✓ Use int(), float(), complex() to convert between types
# ✓ Division (/) returns float; floor division (//) returns int
# ✓ Compound operators (+=, -=, etc.) make code cleaner
# ✓ round(), math.floor(), math.ceil() have different behaviors
# ✓ random module is great for games, simulations, and testing
# ✓ is_integer() checks if float represents whole number
# ✓ isinstance() is the Pythonic way to check types
# ✓ Modulus (%) finds remainder; useful for even/odd checks
#
# 🔗 NEXT TOPICS TO EXPLORE:
#    • Strings and string manipulation
#    • Lists and list operations
#    • Dictionaries and sets
#    • Loops and conditionals
#    • Functions and scope
#
# ════════════════════════════════════════════════════════════════════════════════
