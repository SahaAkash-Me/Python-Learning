# python
#==========================================================================
# Break Statement
#==========================================================================

# ┌─────────────────────────────────────────────────────┐
# │                       START                         │
# └───────────────────────┬─────────────────────────────┘
#                         │
#                         ▼
# ┌─────────────────────────────────────────────────────┐
# │           for item in sequence                      │  ◄─────────────────┐
# │           (last item reached?)                      │                    │
# └───────────────────────┬─────────────────────────────┘                    │
#                         │ No (not last item)                               │
#                         ▼                                                  │
#              ┌──────────────────────┐                                      │
#              │       i == 2 ?       │  ◄── decision                        │
#              └──────┬───────────────┘                                      │
#           False     │          True                                        │
#   ┌────────◄────────┘          └────────────────────────┐                  │
#   │                                                     │                  │
#   ▼                                                     ▼                  │
# ┌──────────────────┐                      ┌─────────────────────────────┐  │
# │    print(i)      │                      │   print("Found it!")        │  │
# └────────┬─────────┘                      └────────────┬────────────────┘  │
#          │                                             │                   │
#          │                                             ▼                   │
#          │                                   ┌──────────────────────┐      │
#          │                                   │        break         │      │
#          │                                   │  (exit loop now!)    │      │
#          │                                   └──────────┬───────────┘      │
#          │                                              │                  │
#          └──────────────────────────────────────────────┼──► next item ───►┘
#                                                         │   (only if no break)
#                  True (last item, loop exhausted)       │
#          ┌───────────────────────────────────────────── ┘
#          │
#          ▼
# ┌─────────────────────────────────────────────────────┐
# │                        END                          │
# └─────────────────────────────────────────────────────┘

# ── Example code ──────────────────────────────────────────────────────────────

sequence = [0, 1, 2, 3, 4]

for i in sequence:
    if i == 2:
        print("Found it!")  # executes when condition is True
        break               # immediately exits the loop
    print(i)                # only runs when i != 2

# Output:
# 0
# 1
# Found it!
# (3 and 4 are never reached because break exits early)

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == "":
        print("Empty value detected!")
        break
    print(f"Name = {name}")

#==========================================================================
# Continue Statement
#==========================================================================

# Iterator: [1] [2] [3]
#            ↑
#       (current item)
#
#                          ┌─────┐
#                          │  1  │  (current item fed into loop)
#                          └──┬──┘
#                             │
#                          ( Start )
#                             │
#              ┌──────────────▼──────────────┐
#              │                             │
#              │       ◇ Last item? ◇  ◄─── for
#              │      /              \
#              │   True              False
#              │    /                   \
#              │   /                    ▼
#              │  /            ◇ if  i == 2 ? ◇
#              │ /            /                 \
#              │/          True               False
#              │           /                     \
#              │          ▼                       ▼
#              │    [ Continue ]            [ Print(i) ]
#              │          │                       │
#              └──────────┘                       │
#              (skip rest, go                     │
#               back to loop)      ───────────────┘
#                                  (loops back to top)
#
#           ( End )   ◄── reached only when last item? == True
#
# ─────────────────────────────────────────────────────────────────────────────
# KEY DIFFERENCE — continue vs break:
#   continue → skips rest of THIS iteration, jumps back to loop top
#   break    → exits the loop entirely, jumps to End
# ─────────────────────────────────────────────────────────────────────────────

# ── Example code ──────────────────────────────────────────────────────────────

sequence = [1, 2, 3]

for i in sequence:          # <── LOOP GATE: last item?
    if i == 2:              # <── DECISION: i == 2?
        continue            # <── TRUE: skip print, jump back to loop top
    print(i)                # <── FALSE: print(i), then loop back

# Output:
# 1
# 3
# (2 is skipped — continue jumped over print(i) for that iteration)

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == "":
        print("Empty value detected!")
        continue
    print(f"Name = {name}")

#==========================================================================
# Pass Statement
#==========================================================================

# --- Python Pass Statement Logic ---
# It is a placeholder where nothing happens
# For now.. Just keep going
# Do nothing...

# if condition:
#     pass  # 'pass' tells Python to ignore this block for now and move to the next line

# ─────────────────────────────────────────────
# FLOW OF A FOR LOOP WITH "pass"
# ─────────────────────────────────────────────
#
#                (Start)
#                   │
#                   ▼
#     ┌─────────────────────────────┐
#  ┌─►│     for i in sequence       │
#  │  │     (Next item?)            │
#  │  └──────────┬──────────────────┘
#  │             │ Yes               No
#  │             │                    │
#  │             ▼                    ▼
#  │       ◇ i == 2 ? ◇            (End)
#  │      /            \
#  │   True            False
#  │    │                │
#  │    ▼                ▼
#  │ [ pass ]       (nothing)
#  │ (do nothing)
#  │    │                │
#  │    └──────┬─────────┘
#  │           │
#  │           ▼
#  │      [ print(i) ]    ◄── always runs (outside if block)
#  │           │
#  └───────────┘
#    (back to next iteration)
#
# ─────────────────────────────────────────────
# INDENTATION IS THE KEY:
#
#   for i in sequence:
#       if i == 2:
#           pass        ← indented inside if  (only runs when i==2)
#       print(i)        ← indented inside for (ALWAYS runs)
#
# ─────────────────────────────────────────────
# TRACE:
#   i=1 → if False → print(1) → loop back
#   i=2 → if True  → pass → print(2) → loop back
#   i=3 → if False → print(3) → loop back
#   done → End
# ─────────────────────────────────────────────
# OUTPUT:  1
#          2   ← 2 also prints! pass did nothing
#          3
# ─────────────────────────────────────────────

sequence = [1, 2, 3]

for i in sequence:
    if i == 2:
        pass        # does nothing — falls through to print below
    print(i)        # always runs for every item

# Output:
# 1
# 2
# 3

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == "":
        pass  # TODO: Handle Empty Value Later {Discuss with team on what to do with the empty value} Example below
    print(f"Name = {name}")

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == "":
        name = "unknown"  # Replaced replace() with direct assignment
    print(f"Name = {name}")

#==========================================================================
# Task: Working Days Printer
#==========================================================================

# Loop through a list of days and print only the working days, skipping the weekends

Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
Weekends = ["Saturday", "Sunday"]

print("\n--- Working Days ---")
for day in Days:
    if day in Weekends:
        continue  # Skip weekends
    print(f"Workday: {day}")

# Alternative approach using else with loop
print("\n--- Working Days (with for-else) ---")
for day in Days:
    if day in Weekends:
        continue
    print(f"Workday: {day}")
else:
    print("All working days printed successfully!")

#==========================================================================
# Summary Table
#==========================================================================

# ┌───────────┬─────────────────────────────────────┬─────────────────────────┐
# │ Statement │              Effect                  │      Use Case           │
# ├───────────┼─────────────────────────────────────┼─────────────────────────┤
# │  break    │ Exits the loop immediately          │ Found what you needed   │
# │  continue │ Skips to next iteration             │ Skip invalid items      │
# │  pass     │ Does nothing (placeholder)          │ TODO / stub code        │
# │  else     │ Runs after loop if no break occurred│ Confirm loop completion │
# └───────────┴─────────────────────────────────────┴─────────────────────────┘

#==========================================================================


#                       TASK BELOW
# Scan emails to block unsafe data from entering your system

    emails = [
        'john.doe@yahoo.com',
        'sarah.smith@hotmail.co.uk',
        "'; DELETE FROM customers; --",
        'mike.wilson@outlook.com',
        'anna.jones@aol.com',
        'Robert"); DROP TABLE Students;--',
        'peter.parker@protonmail.com',
        'lisa.brown@icloud.com',
        '1; DROP TABLE Users;',
        'david.miller@gmx.de'
    ]
    for email in emails:
        if ';'in email:
            print("SQL Injection : Hacker Attack")
            break
        print(f"Processing Emails: {email}")
