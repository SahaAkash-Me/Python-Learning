# ================================================================================
# VARIABLES 
# ----------------------------------------
# Variables act as named containers for storing data in Python.
# You give a variable a value using the assignment operator `=`, then
# you can reuse that name throughout your code. We’ll also use
# the `print()` function to display both literals and variables.
# ================================================================================

# ---------------------------------------
# Without Variables
# ---------------------------------------
# Here we print fixed text directly using print()

print("My name is Akash")
print("Akash is learning Python")
print("Akash wants to become a python expert")

# ---------------------------------------
# Single Variable
# ---------------------------------------
# Store your name in a variable and reuse it in print().
name = "Akash"
print("My name is", name)
print(name,"is learning Python")
print(name,"wants to become a Python expert")

# ---------------------------------------
# Multiple Variables
# ---------------------------------------
# Now we’ll keep both your name and the language in variables.
name = "Akash"
language = "python"
print("My name is", name)
print(name,"is learning", language)
print(name,"wants to become a", language, "expert")

# ---------------------------------------
# Python Challenge
# ---------------------------------------
# Print the following three lines:
#     info@pythonlearning.com
#     support@pythonlearning.com
#     www.pythonlearning.com
# Use a variable for the base domain to make it dynamic!
domain = "pythonlearning.com"
print("info@"+domain)
print("support@"+domain)
print("www."+domain)

# We used + instead of , in print() to concatenate the strings without spaces. 
# Only works with strings (Concatenation).
#Best when you need precise control over the final string format.