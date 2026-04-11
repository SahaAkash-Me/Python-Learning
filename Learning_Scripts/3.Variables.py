# ================================================================================
# 🐍 VARIABLES — COMPLETE GUIDE
# ================================================================================
#
# 📦 Variables act as named containers for storing data in Python.
# 📝 You give a variable a value using the assignment operator =, then
#    you can reuse that name throughout your code. We'll also use
#    the print() function to display both literals and variables.
#
# ================================================================================


# ================================================================================
# 📋 INDEX — FIND ANY TOPIC BY LINE NUMBER
# ================================================================================
#
#   SECTION 1 │ Without Variables — Hardcoded Text          .... Line  35
#   SECTION 2 │ Single Variable — Store & Reuse             .... Line  49
#   SECTION 3 │ Multiple Variables — Name + Language        .... Line  64
#   SECTION 4 │ Python Challenge — Dynamic Domain           .... Line  84
#              │   └─ + Concatenation vs , (comma) note     .... Line  89
#
# ================================================================================


# ================================================================================
# 🔷 SECTION 1: WITHOUT VARIABLES — HARDCODED TEXT           (Line 34)
# ================================================================================
#
# ⚠️  Here the name "Akash" is typed manually in every single line.
# 😓 Problem: If the name changes, you must update EVERY line by hand.
#    In a large program this becomes very risky — you will miss one.
# 💡 This is exactly the problem that variables solve.

print("My name is Akash")
print("Akash is learning Python")
print("Akash wants to become a python expert")


# ================================================================================
# 🔷 SECTION 2: SINGLE VARIABLE — STORE & REUSE              (Line 45)
# ================================================================================
#
# ✅ Store your name ONCE in a variable, then reuse it everywhere.
# 💡 Now if the name changes, you update it in ONE place only —
#    and every print() automatically gets the new value.
# 📌 Syntax: variable_name = value

name = "Akash"
print("My name is", name)
print(name,"is learning Python")
print(name,"wants to become a Python expert")


# ================================================================================
# 🔷 SECTION 3: MULTIPLE VARIABLES — NAME + LANGUAGE         (Line 58)
# ================================================================================
#
# 💡 You can store as many variables as you need.
# ✅ Now BOTH the name and the language are dynamic —
#    change either variable once and all three lines update automatically.
# 🔁 This is the power of variables: write once, reuse everywhere.

name = "Akash"
language = "python"
print("My name is", name)
print(name,"is learning", language)
print(name,"wants to become a", language, "expert")


# ================================================================================
# 🔷 SECTION 4: 🏆 PYTHON CHALLENGE — DYNAMIC DOMAIN         (Line 73)
# ================================================================================
#
# 🎯 Task: Print these three lines:
#       info@pythonlearning.com
#       support@pythonlearning.com
#       www.pythonlearning.com
#
# 💡 Store the repeated part "pythonlearning.com" in a variable.
#    Then prefix each line with the unique part using + concatenation.
# ✅ If the domain ever changes, update ONE variable — all three lines update.

domain = "pythonlearning.com"
print("info@"+domain)
print("support@"+domain)
print("www."+domain)

# 📌 NOTE: We used + instead of , in print() to concatenate the strings without spaces.
# 🔗 + (Concatenation) — Only works with strings. Joins them directly with NO space added.
#    Best when you need precise control over the final string format.
#
# ⚖️  QUICK COMPARISON:
#   print("info@" + domain)   →  info@pythonlearning.com   (no space — joined tightly)
#   print("info@",  domain)   →  info@ pythonlearning.com  (comma adds a space in between)
