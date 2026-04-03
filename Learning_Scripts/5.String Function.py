# ================================================================================
# PYTHON LEARNING NOTES: String Functions
# ================================================================================
# Author: Akash
# Purpose: Understanding Python string operations from type conversion to search
# Focus: Conversion, length, count, replace, format, slice, clean, search, validate
# ================================================================================


# ┌──────────────────────────────────────────────────────────────────────────┐
# │  📑  INDEX / TABLE OF CONTENTS                                          │
# ├──────────────────────────────────────────────────────────────────────────┤
# │                                                                          │
# │   1. 🔄  Type Conversion: Numbers → Strings     → Line  59             │
# │   2. 📏  String Length                          → Line  97             │
# │   3. 🔢  Counting Substrings                    → Line 124             │
# │   4. 🔁  Replacing Characters                   → Line 156             │
# │   5. 📞  Challenge: Phone Number Cleanup        → Line 186             │
# │   6. ➕  Combining Strings                      → Line 218             │
# │   7. 🖊️  String Formatting with f-Strings       → Line 249             │
# │   8. ✂️  Splitting Strings                      → Line 291             │
# │   9. 🔂  Repeating Strings                      → Line 322             │
# │  10. 🔍  Indexing and Slicing                   → Line 348             │
# │  11. 🧹  Whitespace Cleanup                     → Line 390             │
# │  12. 🔡  Case Conversion                        → Line 458             │
# │  13. 🧩  Challenge: String Cleanup              → Line 492             │
# │  14. 🔎  Search Functions                       → Line 539             │
# │  15. 📍  Partial Extraction Using find()        → Line 577             │
# │  16. ✅  Validation: isalpha() / isnumeric()    → Line 613             │
# │                                                                          │
# └──────────────────────────────────────────────────────────────────────────┘


# ┌─────────────────────────────────────────────────────────────────────────┐
# │  📖  QUICK REFERENCE — String methods at a glance                      │
# ├─────────────────────────────────────────────────────────────────────────┤
# │                                                                         │
# │  str(x)          →  Convert any type to string                         │
# │  len(s)          →  Number of characters                               │
# │  s.count(x)      →  Count occurrences of x (case-sensitive)            │
# │  s.replace(a,b)  →  Swap every a with b                                │
# │  s.split(x)      →  Split into list on delimiter x                     │
# │  s.strip()       →  Remove leading & trailing whitespace               │
# │  s.lstrip()      →  Remove leading  whitespace (left side)             │
# │  s.rstrip()      →  Remove trailing whitespace (right side)            │
# │  s.lower()       →  All lowercase                                      │
# │  s.upper()       →  All uppercase                                      │
# │  s.startswith(x) →  True if string begins with x                       │
# │  s.endswith(x)   →  True if string ends with x                         │
# │  s.find(x)       →  Index of first x, or -1 if not found               │
# │  s.isalpha()     →  True if all characters are letters                 │
# │  s.isnumeric()   →  True if all characters are digits                  │
# │  x in s          →  True if x is a substring of s                      │
# │                                                                         │
# └─────────────────────────────────────────────────────────────────────────┘


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔄  SECTION 1 — Type Conversion: Numbers → Strings                    ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHY CONVERT?
#
# Python is strictly typed at runtime — you cannot mix types in the same
# operation without explicit conversion. Trying to concatenate a string and
# an integer crashes with a TypeError.
#
#   "Age: " + 29          →  TypeError ❌
#   "Age: " + str(29)     →  "Age: 29"  ✅
#
# str()  →  converts int, float, bool, or any object into its string form
# int()  →  converts a numeric string back to an integer
# type() →  reveals the current type of a variable — handy for debugging
#
# 💡 Once you assign str(age) back to age, the variable is now a string.
#    Adding 5 to it afterwards will crash — keep separate variables
#    (or use f-strings, shown in Section 7, to avoid conversion entirely).

# ---------------------------------------
# Type Conversion: Numbers to Strings
# ---------------------------------------
name = "AkasH"
print(type(name))  # <class 'str'>

age = 29
print(type(age))   # <class 'int'>
print("Your Age is: " + str(age))  # Must convert int to str for concatenation

age = age + 5       # ➜ 29 (int)
age = str(age)      # Convert to string
print(type(age))    # ➜ <class 'str'>

# age = age + 5     # Error: Cannot add int to str


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  📏  SECTION 2 — String Length                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS len()?
#
# len() counts every character in the string — letters, digits, spaces,
# punctuation — all count as 1. It returns an integer.
#
# Common uses:
#   ✅  Validate minimum password length
#   ✅  Truncate display text to fit a UI element
#   ✅  Detect if a field is empty (len == 0)
#
# 💡 len("") == 0 → empty string. Useful as an existence check alongside
#    the `not name` pattern from the logical operators section.

# ---------------------------------------
# String Length
# ---------------------------------------
password = "123a58478as"
print(len(password))  # ➜ 11

if len(password) < 8:
    print("Your Password is too short!")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔢  SECTION 3 — Counting Substrings                                    ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS .count()?
#
# .count(x) scans the entire string and returns how many times x appears.
# It is CASE-SENSITIVE — "Python" and "python" are treated as different words.
#
# Practical uses:
#   ✅  Count how many times a keyword appears in a document
#   ✅  Detect special characters (like "$") in dirty data
#   ✅  Audit log entries for a specific pattern
#
# 💡 Triple-quoted strings (""" """) allow multi-line text.
#    Notice the leading newline — it's part of the string but .count()
#    only matches your target substring, not newlines.

# ---------------------------------------
# Counting Substrings
# ---------------------------------------
text = """
Python is easy to learn.
Python is powerful$.
Many people love python.
"""

print(text.count("Python"))  # ➜ 2 (case-sensitive — capital P)
print(text.count("python"))  # ➜ 1 (lowercase p — different match)
print(text.count("$"))       # ➜ 1 (special character scan)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔁  SECTION 4 — Replacing Characters                                   ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS .replace()?
#
# .replace(old, new) returns a NEW string with every occurrence of `old`
# swapped out for `new`. The original string is NOT modified (strings are
# immutable in Python — methods always return new strings).
#
# Syntax:  string.replace(old, new)
#
# Passing "" as new effectively DELETES all occurrences of old.
#   phone.replace("-", "")  →  removes all hyphens
#
# 💡 .replace() is case-sensitive.
#    .replace() replaces ALL occurrences, not just the first.
#    Chain multiple .replace() calls to clean several patterns at once.

# ---------------------------------------
# Replacing Characters
# ---------------------------------------
price = "1234,56"
print(price.replace(",", "."))  # ➜ 1234.56  (EU decimal → universal decimal)

phone = "176-1234-56"
print(phone.replace("-", "/"))   # ➜ 176/1234/56   (swap separator style)
print(phone.replace("-", ""))    # ➜ 176123456      (remove all dashes)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  📞  SECTION 5 — Challenge: Phone Number Cleanup                        ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 CHALLENGE BREAKDOWN
#
# Input:  "+49 (176) 123-4567"
# Output: "00491761234567"
#
# Step-by-step chain of .replace() calls:
#   +49        →  0049   (international prefix conversion)
#   (          →  ""     (remove opening bracket)
#   )          →  ""     (remove closing bracket)
#   -          →  ""     (remove hyphen)
#   (space)    →  ""     (remove all spaces)
#
# 💡 Chaining .replace() calls reads left-to-right and applies each
#    substitution to the result of the previous one — not the original.
#    Order matters when one replacement could affect another.

# ---------------------------------------
# Phone Number Cleanup Challenge
# ---------------------------------------
# Convert the messy phone number into a clean number format with only digits:
# Input: "+49 (176) 123-4567"
# Output: "00491761234567"

raw_number = "+49 (176) 123-4567"
clean_number = raw_number.replace("+49", "0049").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
print(clean_number)  # ➜ 00491761234567


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  ➕  SECTION 6 — Combining Strings                                      ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 STRING CONCATENATION WITH +
#
# The + operator joins two strings end-to-end into a new string.
# It does NOT add spaces — you must include them manually if needed.
#
#   "Akash" + "Saha"   →  "AkashSaha"   ← no space
#   "Akash" + "-" + "Saha"  →  "Akash-Saha"  ← separator added manually
#
# 💡 For more than 2–3 pieces, f-strings (Section 7) are cleaner.
#    + is best for simple two-part joins like folder + filename.
#
# Common pattern: build file paths by joining folder and filename strings.

# ---------------------------------------
# Combining Strings
# ---------------------------------------
first_name = "Akash"
last_name = "Saha"
full_name = first_name + "-" + last_name
print(full_name)  # ➜ Akash-Saha

folder = "C:/Users/Akash/"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)  # ➜ C:/Users/Akash/report.csv


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🖊️  SECTION 7 — String Formatting with f-Strings                      ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT ARE f-STRINGS?
#
# f-strings (formatted string literals) let you embed variables and
# expressions directly inside a string using { } — no manual str() needed.
# Prefix the string with f (or F) before the opening quote.
#
# f  →  stands for "formatted"
#
# Two methods compared:
#   Concatenation →  messy, requires str() for every non-string variable
#   f-string      →  clean, readable, handles type conversion automatically
#
# Special cases:
#   {2 + 3}     →  evaluates the expression inline  →  5
#   {{...}}     →  double braces = literal { } in the output
#               →  f"{{This is me}}"  prints  {This is me}
#
# 💡 f-strings are the modern, recommended way to format strings in Python 3.6+.
#    They also support formatting specs: {price:.2f} → two decimal places.

# ---------------------------------------
# String Formatting with f-Strings "f" stands for "formatted"
# ---------------------------------------
name = "Akash"
age = 29
is_student = False

# Method 1: String Concatenation
print("My name is " + name + ", I am " + str(age) + " years old, and student status is " + str(is_student) + ".")

# Method 2: f-Strings (Recommended)
print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")

# f-String Expression and Escape Example
print(f"2 + 3 = {2 + 3}")      # ➜ 2 + 3 = 5         (expression evaluated inline)
print(f"{{This is me}}")       # ➜ {This is me}       (double braces = literal braces)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  ✂️  SECTION 8 — Splitting Strings                                      ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS .split()?
#
# .split(delimiter) breaks a string into a LIST of substrings,
# cutting at every occurrence of the delimiter. The delimiter itself
# is removed from the output.
#
# Returns: a list — so you can index, loop, or unpack the pieces.
#
# Common delimiters:
#   " "  →  split on space        (words, timestamp parts)
#   ","  →  split on comma        (CSV rows)
#   "-"  →  split on hyphen       (dates, IDs)
#   "\n" →  split on newline      (lines of a file)
#
# 💡 .split() with no argument splits on ANY whitespace and removes
#    empty strings — handy for messy multi-space input.

# ---------------------------------------
# Splitting Strings
# ---------------------------------------
stamp = "2026-09-20 14:30"
print(stamp.split(" "))  # ➜ ['2026-09-20', '14:30']   (date and time separated)

csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))  # ➜ ['1234', 'Max', 'USA', '1970-10-05', 'M']   (CSV parsed into list)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔂  SECTION 9 — Repeating Strings                                      ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 THE * OPERATOR ON STRINGS
#
# The * operator repeats a string N times and returns a new string.
#   "ha" * 3   →  "hahaha"
#   "=" * 30   →  "=============================="
#
# Common uses:
#   ✅  Print divider lines in console output
#   ✅  Generate padding or fill characters
#   ✅  Quickly test/visualise repeated patterns
#
# 💡 This is the string equivalent of list * N (repeating a list).
#    "=" * 30 is a clean, readable way to print a separator line
#    without typing 30 = characters manually.

# ---------------------------------------
# Repeating Strings
# ---------------------------------------
print("ha" * 3)              # ➜ hahaha
print("=" * 30)              # ➜ ============================== (separator line)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔍  SECTION 10 — Indexing and Slicing                                  ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 STRINGS ARE SEQUENCES
#
# Every character in a string has a position (index).
# Positive indices count from the LEFT  starting at 0.
# Negative indices count from the RIGHT starting at -1.
#
#   "Python"  →  P  y  t  h  o  n
#   +index    →  0  1  2  3  4  5
#   -index    → -6 -5 -4 -3 -2 -1
#
# Slicing syntax:  string[start : stop]
#   start is INCLUDED, stop is EXCLUDED (stop - 1 is the last character)
#   Omitting start → defaults to 0 (beginning)
#   Omitting stop  → defaults to end of string
#
# 💡 This is the same slicing syntax as lists — one rule to learn for both.
#    Practical use: extract year/month/day from a date string without splitting.

# ---------------------------------------
# Indexing and Slicing
# ---------------------------------------
text = "Python"

print(text[0])    # ➜ P  (first character, positive index)
print(text[-6])   # ➜ P  (same position via negative index)
print(text[5])    # ➜ n  (last character, positive index)
print(text[-1])   # ➜ n  (last character, negative index)
print(text[3])    # ➜ h

# ── Slicing a date string ──────────────────────────────────────────────────
date = "2026-09-20"
print(date[0:4])  # ➜ 2026  (year  — index 0 to 3)
print(date[:4])   # ➜ 2026  (same  — start defaults to 0)
print(date[5:7])  # ➜ 09    (month — index 5 to 6)
print(date[8:])   # ➜ 20    (day   — index 8 to end)
print(date[-2:])  # ➜ 20    (day   — last 2 chars via negative index)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🧹  SECTION 11 — Whitespace Cleanup                                    ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHY CLEAN WHITESPACE?
#
# User input, CSV imports, and database values often carry invisible
# leading/trailing spaces. These cause silent bugs:
#   "Akash " == "Akash"  →  False  ← the trailing space breaks equality
#
# Three methods:
#   .lstrip()  →  removes spaces from the LEFT  (leading)
#   .rstrip()  →  removes spaces from the RIGHT (trailing)
#   .strip()   →  removes spaces from BOTH sides
#
# .strip() also accepts a custom character set:
#   "###Abc***".strip("#***")  →  "Abc"
#   Removes any combination of #, *, space from both ends.
#   (Not a prefix/suffix match — it strips individual chars from the set)
#
# 💡 Always .strip() input before comparison or storage.
#    The len() arithmetic at the bottom quantifies exactly how much
#    padding was present — useful for data quality reports.

# ---------------------------------------
# Whitespace Cleanup
# ---------------------------------------
text = " Engineering".lstrip()
print(text)  # ➜ "Engineering"   (leading space removed)

text = "Engineering ".rstrip()
print(text)  # ➜ "Engineering"   (trailing space removed)

text = "  Engineering ".strip()
print(text)  # ➜ "Engineering"   (both sides stripped)

text = "Data Engineering".strip()
print(text)  # ➜ "Data Engineering"  (no change — no whitespace to remove)

text = "###Abc***".strip("#***")
print(text)  # ➜ "Abc"  (custom char set stripped from both ends)

name_L = " Akash".lstrip()
print(name_L)

name_R = "Akash ".rstrip()
print(name_R)

Is_Same = (len(name_L.lstrip())) == (len(name_R.rstrip()))
print(Is_Same)          # ✅ True — both reduce to "Akash" (5 chars)

name = " Akash ".strip()
print(name)

name = "*** Akash ###".strip("*# ")
print(name)

# ── Measure how much padding exists ───────────────────────────────────────
text = "  Data Analyst "
print(len(text))                                    # Total length including spaces
print(len(text.strip()))                            # Length after cleanup
print(len(text) - (len(text.strip())))              # Number of spaces removed

Number_Of_Spaces = (len(text) - len(text.strip()))
Is_Clean = len(text) == len(text.strip())           # True only if no padding exists
print(f"Number Of Spaces : {Number_Of_Spaces}\nIs My Data Clean ? {Is_Clean}")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔡  SECTION 12 — Case Conversion                                       ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHY NORMALISE CASE?
#
# Human input is inconsistent — "Email", "email", "EMAIL", "eMaIl" are
# all the same word but Python treats them as different strings.
# Before comparing user input, always normalise both sides to the same case.
#
#   .lower()  →  all characters → lowercase
#   .upper()  →  all characters → UPPERCASE
#
# Best practice for comparison:
#   Always apply both .lower() AND .strip() before comparing —
#   the combination catches both case variation and whitespace padding.
#
# 💡 The second print below chains .lower().strip() on both sides
#    before comparing — this is the idiomatic data-cleaning pattern.

# ---------------------------------------
# Case Conversion
# ---------------------------------------
text = "python PROGRAMMING"
print(text.lower())  # ➜ python programming
print(text.upper())  # ➜ PYTHON PROGRAMMING

# ── Case-insensitive comparison after cleanup ──────────────────────────────
search = "Email ".lower().strip()       # "email"
data = " emAil".lower().strip()         # "email"
print(search == data)  # ➜ True   (both normalised before comparing)
print((search.lower().strip()) == (data.lower().strip())) #➜ True


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🧩  SECTION 13 — Challenge: String Cleanup                             ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 CHALLENGE BREAKDOWN
#
# Input:  "968-Maria, ( D@t@ Engineer );; 27y.."
# Goal:   name: Maria | role: Data Engineer | age: 27
#
# Cleanup chain — each .replace() removes or fixes one pattern:
#   "968-"  →  ""    (remove numeric prefix)
#   "("     →  ""    (remove bracket)
#   "@"     →  "a"   (restore letter — D@t@ → Data)
#   ")"     →  ""    (remove bracket)
#   ";"     →  ""    (remove semicolons)
#   "y"     →  ""    (remove age suffix)
#   "."     →  ""    (remove trailing dots)
#
# After cleanup, .strip() removes any remaining edge whitespace.
# Slicing then extracts each field by known position in the cleaned string.
#
# 💡 This pattern — replace junk → strip → slice — is a core
#    data-cleaning technique for messy raw text from forms or scraped data.

# ---------------------------------------
# String Cleanup Challenge
# ---------------------------------------
# Input:  "968-Maria, ( D@ta Engineer );; 27y"
# Goal:   name: maria | role: data engineer | age: 27

Text = "968-Maria, ( D@t@ Engineer );; 27y.."
CT = Text.replace("968-","").replace("(","").replace("@","a").replace(")", "").replace(";", "").replace("y","").replace(".","")
print(CT)
FT = CT.strip()                     # 🧹 Remove leading and trailing whitespace
print(FT)
print(FT == CT.strip())             # ✅ Confirm strip produced same result
print(len(FT))                      # 📏 Length of the cleaned text
print(len(CT))                      # 📏 Length before final strip

# ── Extract fields by position ─────────────────────────────────────────────
name = CT[:5]
role = CT[6:21]
Final_role = role.strip()           # 🧹 Trim any leftover spaces from role
age = CT[-2:]
print(f"name: {name} | role: {Final_role} | age: {age}")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔎  SECTION 14 — Search Functions                                      ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 THREE WAYS TO SEARCH A STRING
#
#   .startswith(x)  →  True if the string BEGINS with x
#   .endswith(x)    →  True if the string ENDS   with x
#   x in s          →  True if x appears ANYWHERE in s
#
# These return True/False — perfect for if conditions and filter logic.
#
# Real-world applications:
#   .startswith("+49")  →  check country code on a phone number
#   .endswith(".csv")   →  validate file extension before processing
#   "@" in email        →  basic email format check
#   "/api" in url       →  route detection in web logs
#
# 💡 These are case-sensitive. Combine with .lower() for case-insensitive search.

# ---------------------------------------
# Search Functions
# ---------------------------------------
phone = "+48-176-12345"
print(phone.startswith("+49"))         # ➜ False: starts with +48, not +49

email = "baraa@outlook.com"
print(email.endswith("gmail.com"))     # ➜ False: ends with outlook.com

file = "data_backup.csv"
print(file.endswith(".csv"))           # ➜ True:  correct file type ✅

print("@" in email)                    # ➜ True:  @ found in email string

url = "https://api.company.com/v1/data"
print("/api" in url)                   # ➜ True: /api path detected in URL


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  📍  SECTION 15 — Partial Extraction Using find()                       ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS .find()?
#
# .find(x) returns the INDEX of the FIRST occurrence of x in the string.
# If x is not found → returns -1 (does NOT raise an error).
#
# Slicing from find() + 1:
#   phone1.find("-")        →  3   (index of first "-")
#   phone1[3 + 1:]          →  everything AFTER the first dash
#   phone1[phone1.find("-") + 1:]  →  "176-12345"
#
# Why + 1?
#   find() returns the index OF the delimiter.
#   Adding 1 moves past it to the first character of what follows.
#
# 💡 This technique works regardless of where the delimiter appears —
#    each phone number has a different prefix length, but the result is
#    always "everything after the first dash". Robust and reusable.

# ---------------------------------------
# Partial Extraction Using find()
# ---------------------------------------
phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"

print(phone1[phone1.find("-") + 1:])  # ➜ 176-12345   (skip country code)
print(phone2[phone2.find("-") + 1:])  # ➜ 654-16548
print(phone3[phone3.find("-") + 1:])  # ➜ 654-16548

print(phone1.find("-"))               # ➜ 3  (dash is at index 3)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  ✅  SECTION 16 — Validation: isalpha() / isnumeric()                   ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 STRING CONTENT VALIDATORS
#
# .isalpha()    →  True ONLY if every character is a letter (a–z, A–Z)
#                  False if there is ANY digit, space, or special character
#
# .isnumeric()  →  True ONLY if every character is a digit (0–9)
#                  False if there is ANY letter, dash, dot, or space
#
# Real-world uses:
#   isalpha()    →  validate country names, names (no digits allowed)
#   isnumeric()  →  validate phone/ID numbers that must be pure digits
#
# ⚠️  .isnumeric() returns False for "-", ".", "+" — so formatted numbers
#    like "+49-176-123" fail. Strip punctuation first if needed.
#
# 💡 These are binary checks — True or False only.
#    Combine with if statements to gate input validation.

# Validation
country = "INDIA"
country1 = "INDIA1"
print(country.isalpha())   # ➜ True:  all letters ✅
print(country1.isalpha())  # ➜ False: contains digit '1' ❌

phone = "0123456789"
phone2 = "01-23456789"
phone3 = "01.23456789"
print(phone.isnumeric())    # ➜ True:  all digits ✅
print(phone2.isnumeric())   # ➜ False: contains dash ❌
print(phone3.isnumeric())   # ➜ False: contains dot  ❌

# ---------------------------------------
# String Cleanup Challenge
# ---------------------------------------
# Input:  "968-Maria, ( D@ta Engineer );; 27y"
# Goal:   name: maria | role: data engineer | age: 27

# Answer Is From Line 190