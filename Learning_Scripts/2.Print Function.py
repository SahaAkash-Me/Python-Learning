# ===================================================================
# 🐍 PRINT() — COMPLETE GUIDE
# ===================================================================
#
# 📌 The print() built-in Python function is used to display text
#    on the screen. It's your main way to communicate with users
#    and check what your code is doing.
#    You'll use it in almost every Python program!
#
# ===================================================================


# ===================================================================
# 📋 INDEX — FIND ANY TOPIC BY LINE NUMBER
# ===================================================================
#
#   SECTION 1 │ print() Basics — Quotes                .... Line  38
#   SECTION 2 │ Escape Sequences                        .... Line  58
#              │   ├─ \" and \'  Print quotes           .... Line  70
#              │   ├─ \\         Backslash              .... Line  83
#              │   ├─ \n         New Line               .... Line  91
#              │   └─ \t         Tab                    .... Line 112
#   SECTION 3 │ Python Challenge (One print() only)     .... Line 118
#   SECTION 4 │ Real Use Case — Shopping Bill           .... Line 143
#   SECTION 5 │ String Concatenation with +             .... Line 168
#
# ===================================================================


# ===================================================================
# 🔷 SECTION 1: print() BASICS — QUOTES                   (Line 35)
# ===================================================================
#
# 💡 You can use either double quotes " " or single quotes ' '
#    Both work exactly the same way in Python.
#    Pick one style and stay consistent throughout your project.

print("Hi Python") # Double quotes
print('Hello Python') # Single quotes
# print("Hi') # ❌ Mixing quote types — SyntaxError

# 🎨 Print a Header with Separators
# 💡 Using dashes to visually frame a title — common for menus and headers
print("--------------------")
print("    LEARN PYTHON    ")
print("--------------------")

# 🎉 For Fun!


# ===================================================================
# 🔷 SECTION 2: ESCAPE SEQUENCES                          (Line 55)
# ===================================================================
#
# 💡 Escape sequences are special characters that start with a
#    backslash \ and tell Python to do something special instead
#    of printing the character literally.
#    They let you represent characters that would otherwise be
#    impossible or confusing to type inside a string.


# -------------------------------------------------------------------
# 🔸 \" and \' — Print quotes INSIDE strings               (Line 60)
# -------------------------------------------------------------------
#
# ⚠️  Problem: Using the same quote type inside a string breaks it.
# ✅ Fix 1: Use a backslash \ before the quote (escape character)
# ✅ Fix 2: Wrap the string in the OTHER type of quote

# print("Hi "Python"") # ❌ Invalid: Double quotes inside Double quotes
print("Hi \"Python\"") # Fix1: Use escape character (backslash)
print('Hi "Python"') # Fix2: Mix single and double quotes
# print('Hi 'Python'') # ❌ Invalid: Single quote inside Single quotes
print('Hi \'Python\'') # Fix1: Use escape character (backslash)
print("Hi 'Python'") # Fix2: Mix single and double quotes


# -------------------------------------------------------------------
# 🔸 \\ — Backslash                                        (Line 72)
# -------------------------------------------------------------------
#
# ⚠️  A single \ starts an escape sequence — Python won't print it as-is.
# ✅ Use \\ (double backslash) to print one literal backslash.
# 📁 This is especially important for Windows file paths!

# print("Path: C:\Users\Akash") #Invalid ← \U treated as Unicode escape in Python 3
print("Path: C:\\Users\\Akash") # Fix: Use double backslashes


# -------------------------------------------------------------------
# 🔸 \n — New Line                                         (Line 77)
# -------------------------------------------------------------------
#
# 💡 \n moves the cursor to the next line inside a string.
#    You can use multiple \n\n\n to add several blank lines at once.
#    print() with no arguments also gives you one blank line.

print("Message1")
print()  # Blank Line
print("Message2")

print("Message1\n") # Adds one new line
print("Message2")

print("Message1\n\n\nMessage2")  # Adds three new lines
print("Message1\nMessage2") # One new line between


# -------------------------------------------------------------------
# 🔸 \t — Tab                                              (Line 93)
# -------------------------------------------------------------------
#
# 💡 \t inserts a tab space — great for indenting and aligning output.

print("Message1\tMessage2")


# ===================================================================
# 🔷 SECTION 3: 🏆 PYTHON CHALLENGE                        (Line 97)
# ===================================================================
#
# 🎯 Task: Recreate the following using ONLY ONE print() function:
#
#    Your learning Path:
#         -Python Basics
#         -Data Engineering
#         -AI
#
# 💡 Combine \n (new line) and \t (tab) inside a single print() call.
#    OR use triple quotes """ """ to write across multiple lines naturally.

# ✅ Solution 1: Multi-line string with escape sequences
print("Your learning Path:\n\t-Python Basics\n\t-Data Engineering\n\t-AI")

# ✅ Solution 2: Alternative using triple quotes (easier to read)
print("""Your learning Path:
\t- Python Basics
\t- Data Engineering
\t- AI""")


# ===================================================================
# 🔷 SECTION 4: 🛒 REAL USE CASE — SHOPPING BILL          (Line 115)
# ===================================================================
#
# 💡 This is how print() is used in real programs — not just "Hello World".
#    Here we calculate a shopping bill step by step and display each result.
#    Notice: print() can display both a label (text) and a value together
#    by separating them with a comma → print("Label:", variable)

price_shirt = 25.00
price_jeans = 45.50

qty_shirt = 2
qty_jeans = 1

total_shirt = price_shirt * qty_shirt
total_jeans = price_jeans * qty_jeans
subtotal = total_shirt + total_jeans
print("Subtotal:", subtotal)        # 💰 print label + calculated value
discount = subtotal * 0.10
print("Discount:", discount)        # 🏷️  10% discount shown
final_total = subtotal - discount
print("Final Total:", final_total)  # 🧾 final amount after discount


# ===================================================================
# 🔷 SECTION 5: STRING CONCATENATION WITH +               (Line 134)
# ===================================================================
#
# 💡 The + operator joins (concatenates) two strings into one.
#    Unlike the comma in print(), the + merges them with NO space added.
#    You control the spacing yourself by adding " " between strings.

print("HI" + " Python")  # 🔗 joins "HI" and " Python" → "HI Python"
