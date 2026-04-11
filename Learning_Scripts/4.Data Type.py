# ================================================================================
# 🐍 DATA TYPES — COMPLETE GUIDE
# ================================================================================
#
# 📦 Python has multiple built-in data types to represent different kinds of values.
# 🔢 Common types include integers, floats, strings, booleans, and NoneType.
# 💡 The data type of a value determines what operations you can perform on it.
#
# ================================================================================


# ================================================================================
# 📋 INDEX — FIND ANY TOPIC BY LINE NUMBER
# ================================================================================
#
#   SECTION 1 │ Examples of Different Data Types              .... Line  45
#              │   ├─ int, float, str, bool, NoneType         .... Line  45
#              │   └─ Edge cases: str "1234", empty str, space .... Line  49
#   SECTION 2 │ Using type() to Check Data Types              .... Line  74
#              │   └─ len() — works on str, fails on int      .... Line  79
#   SECTION 3 │ Exploring Methods Per Data Type               .... Line  88
#              │   ├─ .upper() — string method                .... Line  98
#              │   └─ .bit_length() — integer method          .... Line  99
#   SECTION 4 │ Python Challenge — 5 Variables, 5 Types       .... Line 107
#              │   └─ Printing values + their types           .... Line 128
#
# ================================================================================


# ================================================================================
# 🔷 SECTION 1: EXAMPLES OF DIFFERENT DATA TYPES               (Line 36)
# ================================================================================
#
# 💡 Every value in Python has a data type. Python assigns it automatically
#    based on the value you give — you don't need to declare it manually.
#    This is called DYNAMIC TYPING.
#
# 📊 TYPE OVERVIEW:
#   🔢 int      → whole numbers, no decimal point         e.g. 10, -5, 0
#   🔣 float    → numbers with a decimal point            e.g. 3.14, -0.5
#   🔤 str      → text wrapped in " " or ' '              e.g. "Hello", 'Hi'
#   ✅ bool     → only two possible values                 True or False
#   ⬜ NoneType → represents the absence of a value       None

a = 10        # int
b = 3.15      # float
c = "Hello"   # str (double quotes)
d = 'Hi'      # str (single quotes)
e = "1234"    # str (looks like a number, but it's a string)
f = True      # bool
g = False     # bool
h = None      # NoneType
i = ""        # str - empty string
j = " "       # str - contains a single space

# ⚠️  IMPORTANT EDGE CASES:
#   e = "1234"  → looks like a number but it's a STRING because of the quotes
#                 you CANNOT do math with it directly (e.g. e + 1 would fail)
#   i = ""      → empty string — it EXISTS but has no characters inside
#   j = " "     → NOT empty — it contains one space character


# ================================================================================
# 🔷 SECTION 2: USING type() TO CHECK DATA TYPES               (Line 54)
# ================================================================================
#
# 🔍 type() is a built-in function that tells you exactly what data type
#    a variable holds. Useful for debugging when you're unsure of a type.
#    Output format: <class 'type_name'>
#
# 📏 len() returns the number of characters in a string.
#    ⚠️  It does NOT work on integers — integers have no "length".

text = "hi"
number = 10

print(type(text))    # ➜ <class 'str'>
print(type(number))  # ➜ <class 'int'>
print(len(text))
print(len(number))   # Doesn't work because integers don't have a length
# 💥 TypeError: object of type 'int' has no len()
# ⬆️  This line will raise an error — shown here intentionally to demonstrate
#     that len() only works on sequences (str, list, etc.), NOT numbers.


# ================================================================================
# 🔷 SECTION 3: EXPLORING METHODS FOR EACH DATA TYPE           (Line 70)
# ================================================================================
#
# 💡 Different data types come with different built-in methods.
#    A method is a function that belongs to a specific type.
#    Syntax: variable.method_name()
#
# ⚠️  You CANNOT call a string method on an integer, or vice versa.
#    Trying to do so will raise an AttributeError.

# Some methods are specific to certain types.
print(text.upper())           # "HI" (string method)
print(number.bit_length())    # 4   (integer method)
# print(text.bit_length())    # Error: str has no bit_length()
# ❌ AttributeError: 'str' object has no attribute 'bit_length'
# ⬆️  Commented out intentionally — shows that methods are TYPE-SPECIFIC


# ================================================================================
# 🔷 SECTION 4: 🏆 PYTHON CHALLENGE — 5 VARIABLES, 5 TYPES     (Line 84)
# ================================================================================
#
# 🎯 Task: Create 5 variables, each with a DIFFERENT data type:
#   1️⃣  Your age              → int
#   2️⃣  Your height           → float  (with decimals)
#   3️⃣  Your name             → str
#   4️⃣  Are you a student?    → bool
#   5️⃣  Something with no value yet → NoneType
#
# 💡 Aligned assignment (padding with spaces) makes the code easier to scan —
#    all the = signs line up in a column. This is a clean code habit.

age        = 30            # int
height     = 1.75          # float
name       = "Maria"       # str
is_student = False         # bool
has_kids   = None          # NoneType

# 🖨️  Printing values and their data types
# 💡 type() is called INSIDE print() here — the result is displayed directly.
#    Format: print("Label:", variable, "| Type:", type(variable))
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Student Status:", is_student, "| Type:", type(is_student))
print("Future Project:", future_project, "| Type:", type(future_project))
# 💥 NameError: name 'future_project' is not defined
# ⬆️  'future_project' was never assigned a value above.
#     To fix: add  future_project = None  before this print line.
