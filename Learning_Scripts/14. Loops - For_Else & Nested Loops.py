# =============================================================================
# PYTHON LEARNING NOTES: for-else, break, nested loops & practical patterns
# =============================================================================
# Author: Akash
# Purpose: Understanding loop control flow (for-else, break) and nested iterations
# Focus: Real-world scenarios in data validation, file checking, duplicate detection
# Last Updated: March 2026
# =============================================================================


# ┌──────────────────────────────────────────────────────────────────────────┐
# │  📑  INDEX / TABLE OF CONTENTS                                          │
# ├──────────────────────────────────────────────────────────────────────────┤
# │                                                                          │
# │   1. 🔁  Basic for-else Explanation & Flow Diagram      → Line  33      │
# │   2. 🔂  Simple for-else Examples                       → Line 136      │
# │          (normal completion & with break)                                │
# │   3. 📊  Summary Table of Elements                      → Line 248      │
# │   4. 🔢  Check Items for Even Numbers                   → Line 275      │
# │   5. 👤  Real-time Scenario: Missing Names Check        → Line 308      │
# │   6. 📂  Real-time Scenario: Checking All Files Are CSV → Line 337      │
# │   7. 🔍  TASK: Detect Duplicates in File List           → Line 386      │
# │   8. 🗺️  Nested Loop Flowchart & Execution Trace        → Line 422      │
# │   9. 🔁  Nested Loop Examples (simple & triple nested)  → Line 520      │
# │  10. 🎨  Nested Loop Use Cases                          → Line 556      │
# │          (combinations & report generation)                              │
# │  11. 🗄️  SQL-like NULL Check Generation Pattern         → Line 600      │
# │                                                                          │
# └──────────────────────────────────────────────────────────────────────────┘


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔁  SECTION 1 — Basic for-else Explanation & Flow Diagram             ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS for-else?
#
# Python's for-else is a unique feature you won't find in most languages.
# The `else` block is attached to the FOR loop itself — NOT to an if statement.
#
#   for item in collection:
#       # do something
#   else:
#       # this runs when the loop finishes WITHOUT hitting a break
#
# 💡 Think of `else` here as meaning: "if the loop was never interrupted."
#
# Two outcomes:
#   ✅  Loop ran through every item  →  else block RUNS
#   🛑  break was hit mid-loop       →  else block is SKIPPED
#
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


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔂  SECTION 2 — Simple for-else Examples                               ║
# ║       (normal completion & with break)                                  ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 TWO SCENARIOS SIDE BY SIDE
#
#   Scenario A — No break triggered  →  else RUNS
#   Scenario B — break triggered     →  else SKIPPED
#
# This is the most important thing to internalize about for-else.
# The else is not about the last item — it's about whether break fired.

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


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  📊  SECTION 3 — Summary Table of Elements                              ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 QUICK REFERENCE
# Use this table as a cheat sheet whenever the for-else logic feels confusing.
# Each row maps a concept in the code to its role in the flow diagram above.

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


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔢  SECTION 4 — Check Items for Even Numbers                           ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 PATTERN: SEARCH AND STOP
#
# A classic for-else use case: scan a list looking for the FIRST item
# that satisfies a condition. Stop as soon as you find it.
#
# Why for-else fits perfectly here:
#   • Each item is checked with if / else
#   • The moment an even number is found → break fires → loop stops
#   • If NO even number exists in the list, the loop finishes naturally
#     and you could attach an else block to handle "none found"
#
# 💡 The % (modulo) operator returns the REMAINDER of a division.
#    item % 2 == 0  →  no remainder  →  even number
#    item % 2 != 0  →  remainder = 1  →  odd number

#==========================================================================

# Check items for even numbers

items = [11, 33,29, 17,102, 97]

for item in items:
    if item % 2== 0:
        print(f"Even Number Found : {item}")
        break
    else:
        print(f"This Number Is ODD : {item}")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  👤  SECTION 5 — Real-time Scenario: Missing Names Check               ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 REAL WORLD: DATA VALIDATION
#
# In data work, lists often come from user input, forms, or databases.
# Empty strings ("") and None values mean missing data — they must be caught.
#
# Two ways a name can be "missing":
#   • None  →  the field was never set (null in a database)
#   • ""    →  the field was set but left blank (empty string)
#
# Both are falsy in Python, so we check for both explicitly.
# This pattern appears constantly in data cleaning pipelines.

#==========================================================================
# Real Time Scenario || Checking for missing names in a list
#==========================================================================

names = ["Kungfu Panda", "White Panda", "Red Panda", "", "Black Panda"]

for name in names:
    if name is None or name == "":
        print("Name is missing")
    else:
        print(f"Available Name is : {name}")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  📂  SECTION 6 — Real-time Scenario: Checking All Files Are CSV        ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 REAL WORLD: FILE PIPELINE VALIDATION
#
# Before running a data pipeline, you often need to verify ALL input files
# are the correct format. Finding even ONE wrong file type should stop
# processing immediately — you don't want to waste time or corrupt results.
#
# Two approaches shown below:
#
#   Approach A → check IF the bad extension is present (.pdf check)
#   Approach B → check IF the expected extension is NOT present (not .csv)
#
# Both achieve the same result. Approach B is more flexible — it generalises
# to any unexpected file type, not just one specific one.
#
# .endswith()  →  string method, returns True if string ends with given suffix
# not          →  negation — flips True to False and vice versa

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


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔍  SECTION 7 — TASK: Detect Duplicates in File List                  ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 REAL WORLD: DUPLICATE DETECTION
#
# Duplicate files in a pipeline can cause silent overwriting, incorrect
# row counts, or failed merges. Catching them early is critical.
#
# Technique used here:
#   list.count(value)  →  counts how many times that value appears in the list
#   If count >= 2       →  it's a duplicate → break immediately
#
# 💡 This is an O(n²) approach — fine for small lists, but for large datasets
#    a set-based approach would be much faster.
#
# 💡 Notice: the else inside the for loop here is per-item ("this item is unique"),
#    NOT the for-else — that would appear after the for block ends.

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


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🗺️  SECTION 8 — Nested Loop Flowchart & Execution Trace               ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS A NESTED LOOP?
#
# A nested loop is a loop INSIDE another loop.
# For every single iteration of the OUTER loop, the INNER loop
# runs ALL the way through from start to finish.
#
# Mental model:
#   Outer loop = turning the page of a book
#   Inner loop = reading every line on that page
#
#   If outer has 2 items and inner has 3 items:
#   → total iterations = 2 × 3 = 6 prints
#
# Variable naming convention:
#   Outer → x   (or i, row, color, year...)
#   Inner → y   (or j, col, size, month...)
#   Third → z   (or k, day...)

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


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔁  SECTION 9 — Nested Loop Examples (simple & triple nested)         ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 FROM 2-LEVEL TO 3-LEVEL NESTING
#
# Example 1 — Two loops: produces a grid of (outer × inner) pairs
# Example 2 — Three loops: produces a cube of (x, y, z) coordinate triples
#
# Reading tip:
#   The DEEPEST indentation = the line that runs the MOST times.
#   range(3) × range(2) × range(3) = 3 × 2 × 3 = 18 total prints.

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


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🎨  SECTION 10 — Nested Loop Use Cases                                 ║
# ║       (combinations & report generation)                                ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 REAL WORLD APPLICATIONS
#
# Use Case A — Crossing Data (Cartesian Product)
#   Every color paired with every size → generates ALL combinations.
#   In e-commerce this creates the product variant matrix
#   (Blue-L, Blue-M, Blue-S, Green-L, Green-M, ...).
#   3 colors × 3 sizes = 9 combinations total.
#
# Use Case B — Navigating a Hierarchy (Report Generation)
#   3 levels of nesting mirror a real date hierarchy: year → month → day.
#   2 years × 2 months × 28 days = 112 filenames generated automatically.
#   This kind of pattern is used to batch-create file paths, API requests,
#   or SQL queries without writing each one by hand.

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


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🗄️  SECTION 11 — SQL-like NULL Check Generation Pattern               ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 REAL WORLD: AUTOMATED SQL AUDIT QUERIES
#
# In data engineering, you often need to check EVERY column across EVERY table
# for NULL values. Writing these queries by hand is slow and error-prone.
#
# This nested loop auto-generates one SQL query per (table, column) combination.
# 4 tables × 2 columns = 8 queries printed automatically.
#
# Pattern:
#   Outer loop  →  iterates tables
#   Inner loop  →  iterates columns
#   f-string    →  assembles the SQL query string dynamically
#
# This is a lightweight version of what tools like dbt or Great Expectations
# do under the hood for data quality checks.

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