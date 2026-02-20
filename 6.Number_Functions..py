# ================================================================================
# NUMERIC DATA TYPES
# ----------------------------------------
# Python supports different numeric types: int, float, complex.
# You can also convert between types and perform arithmetic operations.
# ================================================================================

# ---------------------------------------
# Numeric Types
# ---------------------------------------
x = 5
y = 5.7
z = 2 + 3j

print(type(x))  # ➜ <class 'int'>
print(type(y))  # ➜ <class 'float'>
print(type(z))  # ➜ <class 'complex'>

# ---------------------------------------
# Type Conversion
# ---------------------------------------
x = "24"
print(type(x))    # ➜ <class 'str'>

x = int(x)
print(type(x))    # ➜ <class 'int'>
print(x * 3)      # ➜ 72

x = 3.14
print(int(x))     # ➜ 3

x = 3
print(float(x))   # ➜ 3.0

x = 3      # real part
y = 4      # imaginary part
print(complex(x, y))  # ➜ (3+4j)

# ---------------------------------------
# Basic Arithmetic Operations
# ---------------------------------------
print(2 + 3)     # ➜ 5 (Addition)
print(5 - 3)     # ➜ 2 (Subtraction)
print(4 * 2)     # ➜ 8 (Multiplication)
print(7 / 2)     # ➜ 3.5 (True division → float)
print(7 // 2)    # ➜ 3 (Floor division → int)
print(9 % 2)     # ➜ 1 (Modulus → remainder)
print(2 ** 3)    # ➜ 8 (Exponentiation)


# ---------------------------------------
# Compound Assignment Operators
# ---------------------------------------
x = 2         # Step 1: Initialize x with value 2

x += 3        # Step 2: x = x + 3 → x becomes 5
print(x)      # ➜ 5

x -= 1        # Step 3: x = x - 1 → x becomes 4
print(x)      # ➜ 4

x *= 2        # Step 4: x = x * 2 → x becomes 8
print(x)      # ➜ 8

x = 2 
x **= 3 # Step 5: x = x ** 3 → x becomes 8 (2 raised to the power of 3)F
print(x)     # ➜ 8 (2 raised to the power of 3)


# ---------------------------------------
# Absolute Value
# ---------------------------------------
print(abs(2 - 10))  # ➜ 8

# ---------------------------------------
# Rounding and Math Module
# ---------------------------------------
import math

price = 35.54879865

print(round(price))        # ➜ 36 (nearest whole number)
print(round(price, 2))     # ➜ 35.55 (2 decimal places)
print(round(price, 1))     # ➜ 35.5

print(math.floor(price))   # ➜ 35 (round down)
print(math.ceil(price))    # ➜ 36 (round up)
print(math.trunc(price))   # ➜ 35 (truncate decimal part)
print(int(price))          # ➜ 35 (same as trunc)

# ---------------------------------------
# Random Numbers
# ---------------------------------------
import random

print(random.random())       # ➜ Random float between 0 and 1
print(random.randint(1, 6))  # ➜ Simulates a dice roll (1 to 6)

# ---------------------------------------
# Checking Integer Values
# ---------------------------------------
x = 7.0
print(x.is_integer())  # ➜ True → 7.0 is float but represents an int

y = 7.1
print(y.is_integer())  # ➜ False → not a whole number

# ---------------------------------------
# Type Checking
# ---------------------------------------
x = 70.4
print(isinstance(x, int))    # ➜ False
print(isinstance(x, float))  # ➜ True

# ---------------------------------------
# Python Challenge
# ---------------------------------------
# Generate a random integer between 1 and 100,
# then check if the result is an even number.