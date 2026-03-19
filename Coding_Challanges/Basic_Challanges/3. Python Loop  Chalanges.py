#===============================================================================
#                          PYTHON LOOPS - STUDY SCRIPT
#===============================================================================
# Purpose:
# This script demonstrates how loops work in Python.
# It covers:
# • Iterators
# • for loops
# • range()
# • Data aggregation
# • Data cleaning with loops
# • while loops with attempt control
#
# This file is designed as a study / teaching reference.
#===============================================================================



#===============================================================================
# SECTION 1 : WHAT ARE LOOPS?
#===============================================================================
# Loops allow a program to repeat actions for multiple values.
# They are commonly used for:
# • Processing collections of data
# • Transforming data
# • Aggregating values (sum, count, average)
#
# Basic Mechanism:
#
#      START
#        │
#        ▼
#    CONDITION
#        │
#   True │ False
#        ▼
#     ACTION
#        │
#        ▼
#      RESULT
#
#===============================================================================



#===============================================================================
# SECTION 2 : PYTHON ITERATOR
#===============================================================================
# An iterator is an object that allows you to go through items one by one
# in a sequence.
#
# It remembers:
# • What has already been processed
# • What comes next
#
# Examples of iterable objects:
# • List
# • Tuple
# • String
# • Range
# • Dictionary
#===============================================================================



#===============================================================================
# SECTION 3 : FOR LOOP ANATOMY
#===============================================================================
#
# for    i      in    (1, 2, 3):
# ^      ^            ^
# |      |            |
# |      |        Sequence / Iterable
# |      |
# |   Loop Variable
# |
# Loop Keyword
#
#     print(i)
#     ^
#     |
#     Action executed during each iteration
#
# NOTE:
# Indentation determines what code belongs inside the loop
#
# Loop Flow:
#
#  Sequence → Take first item → Execute code → Next item → Repeat
#
#===============================================================================



#===============================================================================
# SECTION 4 : LOOPING THROUGH A TUPLE
#===============================================================================
# Tuples are immutable sequences defined using parentheses ()
#===============================================================================

for i in (1, 2, 3, 4, 5):
    print(f"Round : {i}")



#===============================================================================
# SECTION 5 : LOOPING THROUGH A TUPLE STORED IN A VARIABLE
#===============================================================================
# Instead of writing the tuple directly in the loop,
# we store it in a variable first.
#===============================================================================

items = (1, 2, 3, 4, 5)

for item in items:
    print(f"Round : {item}")



#===============================================================================
# SECTION 6 : LOOPING THROUGH A LIST
#===============================================================================
# Lists use square brackets []
# Lists are mutable (can be modified).
#===============================================================================

items = [1, 2, 3, 4, "Hi"]

for item in items:
    print(f"Round : {item}")



#===============================================================================
# SECTION 7 : LOOPING THROUGH A STRING
#===============================================================================
# Strings are iterable.
# Each character is treated as a separate element.
#===============================================================================

items = "Python"

for item in items:
    print(f"Round : {item}")



#===============================================================================
# SECTION 8 : range() FUNCTION ANATOMY
#===============================================================================
#
# Optional     Required     Optional
# Default=0                 Default=1
#     |           |            |
# range(Start,   Stop,        Step)
#
# Start → number where counting begins (included)
# Stop  → number where counting stops (NOT included)
# Step  → increment between numbers
#
# Example:
#
# range(1, 5)
#
# Generated sequence:
#
# [ 1 | 2 | 3 | 4 ]
#   ^           ^
# Start       Stop-1
#
# Important:
# Stop value (5) is NOT included
# Default Step = 1
#
# Typical Use Cases:
# • Counter loops
# • Iterating fixed number of times
# • Generating number sequences
#===============================================================================



#===============================================================================
# SECTION 9 : LOOP USING range(stop)
#===============================================================================
# range(10) → Generates numbers from 0 to 9
#===============================================================================

for item in range(10):
    print(f"Round : {item}")



#===============================================================================
# SECTION 10 : LOOP USING range(start, stop)
#===============================================================================
# range(1, 10) → Generates numbers from 1 to 9
#===============================================================================

for item in range(1, 10):
    print(f"Round : {item}")



#===============================================================================
# SECTION 11 : LOOP USING range(start, stop, step)
#===============================================================================
# range(1, 10, 2)
#
# Start = 1
# Stop  = 10 (not included)
# Step  = 2
#
# Sequence generated:
# 1 → 3 → 5 → 7 → 9
#===============================================================================

for item in range(1, 10, 2):
    print(f"Round : {item}")



#===============================================================================
# SECTION 12 : DATA AGGREGATION WITH LOOPS
#===============================================================================
# Loops are often used to aggregate values like:
# • Sum
# • Count
# • Average
#
# Example problem:
# Calculate the total score from a list of scores.
#===============================================================================

scores = [80, 50, 60, 75]
total = 0

for score in scores:

    # Add current score to total
    total += score
    # Equivalent to: total = total + score

    # Show running total
    print(f"Current total : {total}")

print(f"Final total : {total}")



#===============================================================================
# SECTION 13 : DATA PROCESSING / DATA CLEANING
#===============================================================================
# Loops are often used to transform messy data before processing.
#
# Example dataset problems:
# • Extra spaces
# • Inconsistent casing
# • Different file extensions
#
# Raw data example:
# ' Report .csv '
# 'DATA .csv '
# ' final .TXT '
#
# Cleaning Steps:
# 1. Remove extra spaces
# 2. Convert to lowercase
# 3. Standardize file extension
#===============================================================================

files = [' Report .csv ', 'DATA .csv ', ' final .TXT ']

for file in files:

    # Clean the file name
    file = file.strip().lower().replace(".txt", ".csv")

    print(f"Processing : {file}")



#===============================================================================
# SECTION 14 : LOOP CONTROL CHALLENGE
#===============================================================================
# Task Description
#
# Allow the user to answer a question with limited attempts.
#
# Rules:
# • Maximum 3 attempts allowed
# • If the user types "yes" within those attempts:
#       → Print "Glad we're on the same page"
# • If the user fails all 3 attempts:
#       → Print "3 strikes. You're out!"
#
# This demonstrates:
# • while loop
# • counter control
# • break statement
# • while-else pattern
#===============================================================================

attempts = 0

while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we're on the same page")
        break
    attempts += 1
else:
    print("3 strikes. You're out!")