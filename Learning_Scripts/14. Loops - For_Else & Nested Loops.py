# =============================================================================
# PYTHON LEARNING NOTES: for-else, break, nested loops & practical patterns
# =============================================================================
# Author: Akash
# Purpose: Understanding loop control flow (for-else, break) and nested iterations
# Focus: Real-world scenarios in data validation, file checking, duplicate detection
# Last Updated: March 2026
# =============================================================================


# INDEX / TABLE OF CONTENTS
# ─────────────────────────────────────────────
# 1. Basic for-else Explanation & Flow Diagram
# 2. Simple for-else Examples (normal completion & with break)
# 3. Summary Table of Elements
# 4. Check items for even numbers
# 5. Real-time Scenario: Checking for missing names in a list
# 6. Real-time Scenario: Checking all files are CSV
# 7. TASK: Detect duplicates in file list (original version)
# 8. Nested Loop Flowchart & Execution Trace
# 9. Nested Loop Examples (simple & triple nested)
# 10. Nested Loop Use Cases (combinations & report generation)
# 11. SQL-like NULL check generation pattern
# ─────────────────────────────────────────────


# 1. Basic for-else Explanation & Flow Diagram
# ─────────────────────────────────────────────
# Iterator Example
# Iterator: [1] [2] [3]
#
#                (Start)
#                   │
#                   ▼
#           ◇ Last item ? ◇   ← for loop check
#            /            \
#         True            False
#          │                │
#          │                ▼
#          │            Print(i)
#          │                │
#          │                │
#          │        (Loop back to check
#          │         next item in iterator)
#          │
#          ▼
#      (else block)
#      Print("End")
#          │
#          ▼
#        (End)
#
# Meaning:
# The loop prints each item.
# When the loop finishes normally (no break),
# the `else` block runs.
# ─────────────────────────────────────────────


# Python code representing the flow

sequence = [1, 2, 3]

for i in sequence:
    print(i)

else:
    print("End")

# ─────────────────────────────────────────────
#                (Start)
#                   │
#                   ▼
#              FOR LOOP
#            (iterate items)
#                   │
#                   ▼
#                [ IF ]
#              condition ?
#               /      \
#            True      False
#             │           │
#             ▼           ▼
#         [ BREAK ]   [ DO SOMETHING ]
#             │           │
#             │           │
#             ▼           │
#           (End) ◄───────┘
#
# If BREAK happens
# → loop stops immediately
# → else block is skipped
#
# If loop completes normally
# (no break occurs):
#
#        else:
#        [ SOMETHING ELSE ]
#             │
#             ▼
#            (End)
#
# ─────────────────────────────────────────────
# Key idea:
#
# break  → loop broken → else does NOT run
# no break → loop completed → else DOES run
# ─────────────────────────────────────────────


# 2. Simple for-else Examples (normal completion & with break)

# Example Python code

numbers = [1, 2, 3]

for n in numbers:
    if n == 2:
        break
    print(n)
else:
    print("Something else")

print("End")

#==========================================================================
# Iterator Flow with Break and Else
#==========================================================================

# ┌─────────────────────────────────────────────────────────────────────┐
# │                        FLOW DIAGRAM                                 │
# │                                                                     │
# │                           START                                     │
# │                             │                                       │
# │                             ▼                                       │
# │                    ┌─────────────────┐                              │
# │                    │  for i in [1,3] │                              │
# │                    │  Iterator = 1   │                              │
# │                    └────────┬────────┘                              │
# │                             │                                       │
# │                             ▼                                       │
# │                    ┌─────────────────┐                              │
# │                    │   i == 2 ?      │                              │
# │                    └────────┬────────┘                              │
# │                           /    \                                    │
# │                      True        False                              │
# │                        /            \                               │
# │                       ▼              ▼                              │
# │              ┌─────────────┐  ┌─────────────┐                       │
# │              │   break     │  │  Print(i)   │                       │
# │              │ (exit loop) │  └──────┬──────┘                       │
# │              └──────┬──────┘         │                              │
# │                     │                 │                             │
# │                     └──────┬──────────┘                             │
# │                            │                                        │
# │                            ▼                                        │
# │                   ┌─────────────────┐                               │
# │                   │ More items?     │                               │
# │                   │ (Next = 3)      │                               │
# │                   └────────┬────────┘                               │
# │                           /    \                                    │
# │                       Yes        No (Loop finished)                 │
# │                        /            \                               │
# │                       ▼              ▼                              │
# │              ┌─────────────┐  ┌─────────────┐                       │
# │              │   Continue  │  │ else:       │                       │
# │              │  (back to   │  │ Print("End")│                       │
# │              │   start)    │  └──────┬──────┘                       │
# │              └─────────────┘         │                              │
# │                                      ▼                              │
# │                                    END                              │
# └─────────────────────────────────────────────────────────────────────┘

# ── Example Code ──────────────────────────────────────────────────────

numbers = [1, 3]  # Iterator: 1, then 3

print("--- For loop with condition check ---")
for i in numbers:
    if i == 2:
        print("break")      # Won't execute (no 2 in list)
        break
    else:
        print(f"Print({i})")  # Prints: Print(1), then Print(3)
else:
    print('Print("End")')     # Prints after loop completes

# Output:
# Print(1)
# Print(3)
# Print("End")

# ── Another Example ────────────────────────────────────────────────────

numbers = [1, 2, 3, 4, 7]  # Iterator: 1, 2, 3, 4, 7

print("\n--- With break triggering ---")
for i in numbers:
    if i == 2:
        print("break")  # Executes when i == 2
        break
    else:
        print(f"Print({i})")  # Prints only for i = 1
else:
    print('Print("End")')  # Won't execute (break happened)

# Output:
# Print(1)
# break


# 3. Summary Table of Elements

#==========================================================================
# Summary Table
#==========================================================================

# ┌──────────┬────────────────────────────────┬─────────────────────────┐
# │ Element  │          Meaning               │      In Diagram         │
# ├──────────┼────────────────────────────────┼─────────────────────────┤
# │ Iterator │ Current item from list [1,3]   │  "for i in [1,3]"       │
# │ i == 2 ? │ Condition check                │   Decision diamond      │
# │ True     │ Condition met                  │   Leads to break        │
# │ False    │ Condition not met              │   Leads to Print(i)     │
# │ break    │ Exit loop immediately          │   Terminates loop       │
# │ else     │ Runs after natural completion  │   After all items       │
# │ Print(i) │ Display current item           │    Action block         │ 
# │ Start    │ Beginning of iteration         │    Loop entry point     │
# │ End      │ Program continues after loop   │    Exit point           │
# └──────────┴────────────────────────────────┴─────────────────────────┘


# 4. Check items for even numbers

#==========================================================================

# Check items for even numbers

items = [11, 33,29, 17,102, 97]

for item in items:
    if item % 2== 0:
        print(f"Even Number Found : {item}")
        break
    else:
        print(f"This Number Is ODD : {item}")


# 5. Real-time Scenario: Checking for missing names in a list

#==========================================================================
# Real Time Scenario || Checking for missing names in a list
#==========================================================================

names = ["Kungfu Panda", "White Panda", "Red Panda", "", "Black Panda"]

for name in names:
    if name is None or name == "":
        print("Name is missing")
    else:
        print(f"Available Name is : {name}")


# 6. Real-time Scenario: Checking all files are CSV

#==========================================================================
# Real Time Scenario || Checking all files are csv
#==========================================================================

files = ["data1.csv",
         "report.pdf",
         "report2.csv"]
for file in files:
    if file.endswith(".pdf"):
        print(f"Unknown File Found : {file}")
        break
    else:
        print(f"CSV file foung : {file}")


# Or We Can Do This :

files = ["data1.csv",
         "report.pdf",
         "report2.csv"]
for file in files:
    if not file.endswith(".csv"):
        print(f"{file} Unknown File Found")
        break
    else:
        print(f"All Files Are CSV: {file}")


# 7. TASK: Detect duplicates in file list (original version)

#________________________________________________________________
# TASK
#----------------------------------------------------------------

files = ["a.csv",
            'b.xlsx',
            'c.docx',
            'a.csv',
            'e.csv']
for file in files:
    if files.count(file) >= 2:              # if itirator.count(value) >= 2
        print("Duplicate found")
        break
    else:
        print("Unique")


# 8. Nested Loop Flowchart & Execution Trace

#==========================================================================
# Nested Loop
#==========================================================================

# ╔═════════════════════════════════════════════════════════════════════════╗
# ║                     NESTED LOOP FLOWCHART                              ║
# ║              Outer: [a, b]     Inner: [1, 2]                           ║
# ╚═════════════════════════════════════════════════════════════════════════╝
#
#                              ( START )
#                                  │
#                                  ▼
#                       ┌─────────────────────┐
#                       │     OUTER LOOP      │ ◄─────────────────────┐
#                       │  for x in [a, b]    │                       │
#                       └──────────┬──────────┘                       │
#                                  │                                  │
#                                  ▼                                  │
#                         ◇ Last item? (x) ◇                         │
#                        /                  \                         │
#                     True                False                       │
#                      /                     \                        │
#                     ▼                       ▼                       │
#                  ( END )           ┌─────────────────┐              │
#               (program done)       │   Get next x    │              │
#                                    │  current = a/b  │              │
#                                    └────────┬────────┘              │
#                                             │                       │
#                                             ▼                       │
#                                  ┌─────────────────────┐            │
#                                  │     INNER LOOP      │            │
#                                  │  for y in [1, 2]    │            │
#                                  └──────────┬──────────┘            │
#                                             │                       │
#                                             ▼                       │
#                                    ◇ Last item? (y) ◇              │
#                                   /                  \              │
#                                True                False            │
#                                /                      \             │
#                               ▼                        ▼            │
#                  ┌──────────────────────┐    ┌──────────────────┐   │
#                  │   Back to OUTER      │    │   Get next y     │   │
#                  │   (next x)           │    │  current = 1/2   │   │
#                  └──────────┬───────────┘    └────────┬─────────┘   │
#                             │                         │             │
#                             │                         ▼             │
#                             │                ┌─────────────────┐    │
#                             │                │   Print(x, y)   │    │
#                             │                │     action      │    │
#                             │                └────────┬────────┘    │
#                             │                         │             │
#                             │                         └─────────────┤
#                             │                    (loops back to     │
#                             │                     inner Last item?) │
#                             └─────────────────────────────────────►─┘
#                                          (loops back to outer Last item?)
#
# ─────────────────────────────────────────────────────────────────────────────
# EXECUTION TRACE:
#
#  Step │ x    │ y         │ Action
#  ─────┼──────┼───────────┼──────────────────────────────────
#   1   │  —   │  —        │ START
#   2   │  a   │  —        │ Enter outer (Last item? False)
#   3   │  a   │  1        │ Enter inner → Print(a, 1)
#   4   │  a   │  2        │ Next y     → Print(a, 2)
#   5   │  a   │  end      │ Inner done (Last item? True) → back to outer
#   6   │  b   │  —        │ Next outer (Last item? False)
#   7   │  b   │  1        │ Enter inner → Print(b, 1)
#   8   │  b   │  2        │ Next y     → Print(b, 2)
#   9   │  b   │  end      │ Inner done (Last item? True) → back to outer
#  10   │  end │  —        │ Last item? True → END
#
# ─────────────────────────────────────────────────────────────────────────────


# 9. Nested Loop Examples (simple & triple nested)

# ── Example code ──────────────────────────────────────────────────────────────

outer_list = ['a', 'b']
inner_list = [1, 2]

for x in outer_list:           # <── OUTER LOOP: Last item? False → get x
    for y in inner_list:       # <── INNER LOOP: Last item? False → get y
        print(f"Print({x},{y})")   # <── action → loops back to inner check
                               #     inner Last item? True → back to outer
                               #     outer Last item? True → END

# Output:
# Print(a,1)
# Print(a,2)
# Print(b,1)
# Print(b,2)

for x in range(3):
    for y in range(2):
        for z in range (3):
            print(f"({x}, {y}, {z})")


# 10. Nested Loop Use Cases (combinations & report generation)

#==========================================================================
# Nested Loop || Use Case
#==========================================================================


# Crossing Data

colors = ['Blue', 'Green', 'Red']
sizes = ['L', 'M', 'S']
for color in colors:
    for size in sizes:
        print(f"Combinations : {color} - size{size} ")

# Navigate Hierarchy

years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1, 29)

for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")


# 11. SQL-like NULL check generation pattern

# SELECT count(*) FROM Tables where id  IS NULL ;
tables = [
    "customers",
    "roducts",
    "orders",
    "prices"
]
columns = ['id', 'create_date']

for t in tables:
    for c in columns:
        print(f"SELECT count(*) FROM customers {t} WHERE {c} IS NULL")