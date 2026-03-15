#===============================================================================
# PYTHON LOOPS - STUDY SCRIPT
#===============================================================================
# Loops allow a program to repeat actions for multiple values.
# They are commonly used for:
# • Processing collections of data
# • Transforming data
# • Aggregating values (sum, count, average)
#
# Basic Mechanism:
# Start → Condition → Action → End Result
#===============================================================================



#===============================================================================
# PYTHON ITERATOR
#===============================================================================
# An iterator is an object that allows you to go through items one by one
# in a sequence.
#
# It remembers:
# • What has already been processed
# • What comes next
#===============================================================================



#===============================================================================
# FOR LOOP ANATOMY
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
#===============================================================================



#===============================================================================
# LOOPING THROUGH A TUPLE
#===============================================================================
for i in (1, 2, 3, 4, 5):
    print(f"Round : {i}")



#===============================================================================
# LOOPING THROUGH A TUPLE (stored in a variable)
#===============================================================================
items = (1, 2, 3, 4, 5)

for item in items:
    print(f"Round : {item}")



#===============================================================================
# LOOPING THROUGH A LIST
#===============================================================================
items = [1, 2, 3, 4, "Hi"]   # Lists use square brackets []

for item in items:
    print(f"Round : {item}")



#===============================================================================
# LOOPING THROUGH A STRING
#===============================================================================
items = "Python"

for item in items:
    print(f"Round : {item}")



#===============================================================================
# range() ANATOMY
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
#===============================================================================



#===============================================================================
# LOOP USING range(stop)
#===============================================================================
for item in range(10):
    print(f"Round : {item}")



#===============================================================================
# LOOP USING range(start, stop)
#===============================================================================
for item in range(1, 10):
    print(f"Round : {item}")



#===============================================================================
# LOOP USING range(start, stop, step)
#===============================================================================
for item in range(1, 10, 2):
    print(f"Round : {item}")



#===============================================================================
# DATA AGGREGATION WITH LOOPS
#===============================================================================
# Loops are often used to aggregate values like:
# • Sum
# • Count
# • Average
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
# DATA PROCESSING / DATA CLEANING
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
#===============================================================================

files = [' Report .csv ', 'DATA .csv ', ' final .TXT ']

for file in files:

    # Clean the file name
    file = file.strip().lower().replace(".txt", ".csv")

    print(f"Processing : {file}")