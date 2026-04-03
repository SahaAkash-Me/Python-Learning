# ================================================================================
# PYTHON LEARNING NOTES: Logical Operators & Identity Checks
# ================================================================================
# Author: Akash
# Purpose: Understanding and, or, not, in, not in, is, is not
# Focus: Truth tables, operator precedence, real-world access control & validation
# ================================================================================


# ┌──────────────────────────────────────────────────────────────────────────┐
# │  📑  INDEX / TABLE OF CONTENTS                                          │
# ├──────────────────────────────────────────────────────────────────────────┤
# │                                                                          │
# │   1. 🔗  Basic Logical Operators: and / or       → Line  48             │
# │   2. 🖥️  Real-World Example: System Monitoring   → Line  80             │
# │   3. 🔑  Login Validation                        → Line 104             │
# │   4. ⚖️  Operator Precedence: and / or           → Line 129             │
# │   5. ❗  Logical NOT                             → Line 163             │
# │   6. 🔒  Complex Access Control Logic            → Line 201             │
# │   7. 🔍  Membership Operators: in / not in       → Line 241             │
# │   8. 🧠  Identity Operators: is / is not         → Line 279             │
# │   9. 📧  Validate Email (not empty check)        → Line 328             │
# │  10. 🔎  Identity Operators for None Checks      → Line 355             │
# │  11. 🏆  Python Challenges                       → Line 394             │
# │                                                                          │
# └──────────────────────────────────────────────────────────────────────────┘


# ┌─────────────────────────────────────────────────────────────────────────┐
# │  📖  QUICK REFERENCE — All operators at a glance                       │
# ├─────────────────────────────────────────────────────────────────────────┤
# │                                                                         │
# │  and        →  Both conditions must be True         (strict)           │
# │  or         →  At least one condition must be True  (lenient)          │
# │  not        →  Flips True → False, False → True     (negation)         │
# │  in         →  Value exists in a sequence           (membership)       │
# │  not in     →  Value does NOT exist in a sequence   (exclusion)        │
# │  is         →  Same object in memory                (identity)         │
# │  is not     →  Different objects in memory          (non-identity)     │
# │                                                                         │
# │  Precedence (high → low):  not  →  and  →  or                         │
# │  Use parentheses ( ) to make intent explicit and avoid surprises       │
# │                                                                         │
# └─────────────────────────────────────────────────────────────────────────┘


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔗  SECTION 1 — Basic Logical Operators: and / or                      ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 TRUTH TABLES
#
# and — BOTH must be True for the result to be True:
#   True  and True   →  True   ✅
#   True  and False  →  False  ❌
#   False and True   →  False  ❌
#   False and False  →  False  ❌
#
# or  — AT LEAST ONE must be True for the result to be True:
#   True  or  True   →  True   ✅
#   True  or  False  →  True   ✅
#   False or  True   →  True   ✅
#   False or  False  →  False  ❌
#
# 💡 Shortcut:
#   and = "strict" — one failure = total failure
#   or  = "lenient" — one success = total success

# ---------------------------------------
# Basic Logical Operators: and / or
# ---------------------------------------
print(3 > 1 and 5 < 1)   # ➜ False: first is True, second is False
print(3 > 1 and 5 > 1)   # ➜ True: both are True

print(3 > 1 or 5 < 1)    # ➜ True: first is True, second is False
print(3 > 1 or 5 > 1)    # ➜ True: both are True


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🖥️  SECTION 2 — Real-World Example: System Monitoring                 ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 USE CASE: SERVER HEALTH ALERT
#
# In a monitoring system you want to trigger an alert if EITHER
# CPU or memory crosses a threshold — one overloaded resource is enough
# to cause a problem. `or` is the right operator:
#   cpu_usage > 90  →  False  (70 is fine)
#   memory_usage > 90  →  False  (90 is not > 90, it equals 90)
#   False or False  →  False  → no alert triggered
#
# 💡 Change `>` to `>=` if you want to trigger at exactly 90.

# ---------------------------------------
# Real-World Example: System Monitoring
# ---------------------------------------
cpu_usage    = 70
memory_usage = 90

print(cpu_usage > 90 or memory_usage > 90)  # ➜ False: both values are within limits


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔑  SECTION 3 — Login Validation                                       ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 USE CASE: AUTHENTICATION GATE
#
# Login requires BOTH a valid email AND a valid password.
# If either is missing/wrong → access denied.
# `and` is the right operator — both conditions must be True:
#   email    = True   ✅
#   password = False  ❌
#   True and False  →  False  →  login rejected
#
# 💡 In production both would be strings, not booleans —
#    e.g. email != "" and len(password) >= 8

# ---------------------------------------
# Login Validation
# ---------------------------------------
email    = True
password = False

print(email and password)  # ➜ False: both must be True to allow login


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  ⚖️  SECTION 4 — Operator Precedence: and / or                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 PRECEDENCE ORDER (high → low)
#
#   not   →  evaluated FIRST
#   and   →  evaluated SECOND
#   or    →  evaluated LAST
#
# This mirrors maths:  * before +
# Just like 2 + 3 * 4 = 14 (not 20), Python evaluates `and` before `or`.
#
# Line 1 breakdown — no parentheses:
#   5==5  or  8>5  and  3<1
#   →  and binds tighter:   5==5  or  (8>5 and 3<1)
#   →  8>5=True, 3<1=False  →  (True and False) = False
#   →  5==5=True  or  False  =  True  ✅
#
# Line 2 breakdown — with parentheses:
#   (5==5 or 8>5)  and  3<1
#   →  (True or True) = True
#   →  True and 3<1=False  =  False  ❌
#
# 💡 RULE: Always use parentheses when mixing `and` and `or`.
#    Don't rely on precedence to communicate intent — parentheses are free.

# ---------------------------------------
# Operator Precedence: and / or
# ---------------------------------------
print(5==5 or 8>5 and 3<1)     # ➜ True: 'and' has higher precedence, so evaluated as (5==5) or (8>5 and 3<1)
print((5==5 or 8>5) and 3<1)   # ➜ False: 'and' has higher precedence, so evaluated as ((5==5 or 8>5) and 3<1)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  ❗  SECTION 5 — Logical NOT                                            ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS not?
#
# `not` is a unary operator — it takes ONE operand and flips its truth value:
#   not True   →  False
#   not False  →  True
#
# not works on any expression, not just booleans:
#   not 3 > 2  →  not True  →  False
#
# Falsy values (evaluate to False without not):
#   0, "", None, [], {}, False
# Truthy values (evaluate to True without not):
#   Any non-zero number, non-empty string, non-empty collection
#
# not name   →  True  when name is "" (empty string is falsy)
# not 10     →  False when 10 is truthy
#
# Double not:
#   not not False  →  not True  →  False  (back to original)
#   Useful trick: not not x converts any value to its boolean equivalent

# ---------------------------------------
# Logical NOT
# ---------------------------------------
print(not 3 > 2)       # ➜ False: 3>2 is True, not True = False
print(not True)        # ➜ False
print(not False)       # ➜ True
print(not not False)   # ➜ False: double negation returns to original

name = ""
print(not name)        # ➜ True: empty string is falsy
print(not 10)          # ➜ False: 10 is truthy


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔒  SECTION 6 — Complex Access Control Logic                           ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 USE CASE: PERMISSION SYSTEM
#
# Rule: Allow access if the user is logged in OR a guest,
#       BUT they must NOT be banned.
#
# The two lines show a critical precedence trap:
#
# Line 1 — WITHOUT parentheses (wrong logic):
#   is_logged_in or is_guest and not is_banned
#   →  and binds first:  is_guest and not is_banned  →  False and True  →  False
#   →  is_logged_in or False  →  True or False  →  True  ✅  ← WRONG!
#   →  The banned user got through because is_logged_in was evaluated in isolation
#
# Line 2 — WITH parentheses (correct logic):
#   (is_logged_in or is_guest) and not is_banned
#   →  (True or False) = True
#   →  True and not True  →  True and False  →  False  ❌  ← CORRECT!
#   →  Banned user is blocked regardless of login status
#
# 💡 THIS is why parentheses matter — same values, same operators,
#    completely different security outcome.

# ---------------------------------------
# Complex Access Control Logic
# ---------------------------------------
# Allow access if the user is logged in OR a guest,
# BUT they must not be banned.

is_logged_in = True
is_guest     = False
is_banned    = True

print(is_logged_in or is_guest and not is_banned)      # ➜ True (wrong logic)
print((is_logged_in or is_guest) and not is_banned)    # ➜ False (correct logic)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔍  SECTION 7 — Membership Operators: in / not in                      ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT ARE in AND not in?
#
# These operators check whether a value EXISTS inside a collection or string.
# They work on: strings, lists, tuples, sets, dicts (checks keys)
#
#   x in collection       →  True if x is found anywhere inside
#   x not in collection   →  True if x is NOT found anywhere inside
#
# For strings: checks for substring match — "A" in "Akash" checks if 'A'
#              appears anywhere in the string (case-sensitive!)
#
# For lists:   checks for exact element match — 3 in [1,2,3] → True
#
# 💡 Real-world use (shown below):
#    Check if a domain is on a banned list before allowing a sign-up.
#    `not in` reads almost like English: "if domain not in banned_domains"

# ---------------------------------------
# Membership Operators: in / not in
# ---------------------------------------
print("A" in "Akash")          # ➜ True:  'A' is a substring of 'Akash'
print("A" not in "Akash")      # ➜ False: 'A' IS in 'Akash', so not in = False

print("f" not in "python")      # ➜ True:  'f' does not appear in 'python'
print(3 not in [1, 2, 3])       # ➜ False: 3 IS in the list

"Akash" in ["Akash", "Alice", "Bob"]      # ➜ True  (not printed — no print() wrapper)
"Akash" not in ["Akash", "Alice", "Bob"]  # ➜ False (not printed — no print() wrapper)

domain = "spam.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)  # ➜ False: spam.com IS in the banned list → access denied


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🧠  SECTION 8 — Identity Operators: is / is not                        ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 == vs is — THE CRITICAL DIFFERENCE
#
#   ==  checks VALUE equality     →  "do they contain the same data?"
#   is  checks IDENTITY equality  →  "are they the exact same object in memory?"
#
# Two separate lists with identical contents:
#   x == y  →  True   (same data)
#   x is y  →  False  (different objects — two separate spots in RAM)
#
# Small integer caching (CPython implementation detail):
#   Python caches integers from -5 to 256.
#   x = 10; y = 10  →  both point to the SAME cached object
#   x is y  →  True  (same memory address, because Python reused the object)
#   ⚠️  Don't rely on this — it's an implementation detail, not a language rule
#
# Assignment (x = y):
#   y = x  →  y now points to the EXACT same list object as x
#   x is y →  True  (one object, two names)
#   Changing x also changes y (same reference — see the Copy section)
#
# 💡 Use is for: None checks, singleton comparisons
#    Use == for: all value comparisons

# ---------------------------------------
# Identity Operators: is / is not
# ---------------------------------------
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y)  # ➜ True:  same content — values match
print(x is y)  # ➜ False: different objects — two separate lists in memory

x = 10
y = 10

print(x == y)  # ➜ True: same value
print(x is y)  # ➜ True: same object (small integers are cached by CPython)

x = ['a', 'b', 'c']
y = x             # y is now an alias — both names point to the same list

print(x == y)  # ➜ True: same values
print(x is y)  # ➜ True: same object (same memory reference)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  📧  SECTION 9 — Validate Email (not empty check)                       ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 USE CASE: FORM FIELD VALIDATION
#
# Before processing user input, always verify it is not blank.
# `!= ""` checks that the string is not an empty string.
#
# email = "b@gmail.com"  →  "b@gmail.com" != ""  →  True  ✅  (has content)
# email = ""             →  "" != ""              →  False ❌  (empty, reject it)
#
# 💡 Alternative approaches:
#   len(email) > 0   →  same result, more explicit
#   bool(email)      →  truthy check — empty string is falsy
#   email            →  bare truthy check (simplest)

# ---------------------------------------
# Validate Email Exists and Is Not Empty
# ---------------------------------------
email = "b@gmail.com"
print(email != "")              # ➜ True:  email has content

email = ""
print(email != "")              # ➜ False: email is empty


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔎  SECTION 10 — Identity Operators for None Checks: is / is not       ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHY USE is FOR NONE?
#
# None is a singleton in Python — there is only ONE None object in memory.
# `is None` and `is not None` are the correct, idiomatic way to check for it.
# Using == None works but is considered bad practice (PEP 8 recommends `is`).
#
# Two separate list objects:
#   a == b  →  True   (same values)
#   a is b  →  False  (different objects)
#
# Compound None + empty check:
#   email is not None and email != ""
#   →  email = None  →  None is not None  →  False
#   →  Python short-circuits: second condition is never evaluated
#   →  Result: False  ❌  (email is None — not safe to use)
#
# 💡 SHORT-CIRCUIT EVALUATION:
#    With `and` — if the first condition is False, Python stops immediately.
#    The second condition is never checked. This is efficient AND safe
#    (avoids errors like calling .strip() on None).

# ---------------------------------------
# Identity Operators for None Checks || is / is not
# ---------------------------------------

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # ➜ True:  same content
print(a is b)  # ➜ False: different objects in memory

email = None
print(email is not None and email != "")  # ➜ False: email is None — short-circuits at first condition


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🏆  SECTION 11 — Python Challenges                                     ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 CHALLENGE SET — combining everything from this file
#
# Each challenge below requires applying the operators from this file.
# Try to solve each one before checking the solutions file.
#
# Tips:
#   Challenge 1  →  use `and`, check name != "" and age comparison
#   Challenge 2  →  use `and` + len() + `not in` (check for space character)
#   Challenge 3  →  use `and` + `in` + str.endswith()
#   Challenge 4  →  use `is not` + isinstance() + len()
#   Challenge 5  →  use `or` + `and` + `not` — watch the precedence!

# ---------------------------------------
# Python Challenges
# ---------------------------------------
# 1. Name is not empty and age is >= 18
# 2. Password is at least 8 chars and has no spaces
# 3. Email is not empty, contains '@', and ends with '.com'
# 4. Username is a string, not None, and longer than 5 characters
# 5. User is admin or moderator, and not banned or email verified

# Solved In D:\Python\Python Challanges\1.# --- Python Challenges Logic ---.py