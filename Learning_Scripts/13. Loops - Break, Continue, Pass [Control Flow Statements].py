# =============================================================================
# PYTHON LEARNING NOTES: break, continue, pass & loop control flow
# =============================================================================
# Author: Akash
# Purpose: Understanding the three loop control statements and when to use each
# Focus: Flow diagrams, real-world scenarios, SQL injection defence, working days
# =============================================================================


# ┌──────────────────────────────────────────────────────────────────────────┐
# │  📑  INDEX / TABLE OF CONTENTS                                          │
# ├──────────────────────────────────────────────────────────────────────────┤
# │                                                                          │
# │   1. 🛑  Break Statement                    → Line  25      │
# │   2. ⏭️  Continue Statement                 → Line 119      │
# │   3. 🤫  Pass Statement                     → Line 205      │
# │   4. 📅  Task: Working Days Printer         → Line 324      │
# │   5. 📊  Summary Table                      → Line 370      │
# │   6. 🔐  Task: SQL Injection Scanner        → Line 399      │
# │                                                                          │
# └──────────────────────────────────────────────────────────────────────────┘


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🛑  SECTION 1 — Break Statement                                        ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS break?
#
# `break` is a loop control statement that immediately terminates the loop
# the moment it is executed — no more iterations, no matter how many items
# are left in the sequence.
#
# Think of it as a fire exit:
#   🔥  You find what you were looking for (or something dangerous)
#   🚪  break = exit immediately, don't check the remaining items
#
# When does break make sense?
#   ✅  You're searching for ONE specific item — stop once found
#   ✅  You hit an error/invalid value — stop processing immediately
#   ✅  First match is enough — no need to scan the rest
#
# 💡 Key behaviour:
#   • The else block (if any) is SKIPPED when break fires
#   • Code after the loop resumes normally
#   • Items after the break point are NEVER visited

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

# ── Real-world use: empty value detection ─────────────────────────────────────
# 💡 Stop processing as soon as a blank name is found — don't continue
#    with potentially corrupt data downstream.

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == "":
        print("Empty value detected!")
        break
    print(f"Name = {name}")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  ⏭️  SECTION 2 — Continue Statement                                     ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS continue?
#
# `continue` skips the REST of the current iteration and jumps back to the
# top of the loop to begin the next one. The loop itself does NOT stop —
# only the current pass through is cut short.
#
# Think of it as skipping a bad track on a playlist:
#   🎵  Hit a song you don't want → skip it → next song plays normally
#   (The playlist keeps going — you didn't turn it off)
#
# continue vs break — the critical difference:
#   continue  →  skip THIS item, keep looping  🔄
#   break     →  exit the loop entirely         🛑
#
# When does continue make sense?
#   ✅  Filter out invalid/empty/unwanted values mid-loop
#   ✅  Skip rows that fail a validation check
#   ✅  Process only items that meet a condition, ignore the rest

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

# ── Real-world use: skip empty names, keep processing ─────────────────────────
# 💡 Unlike break (which would stop everything), continue lets us
#    flag the problem AND keep going through the rest of the list.

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == "":
        print("Empty value detected!")
        continue
    print(f"Name = {name}")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🤫  SECTION 3 — Pass Statement                                         ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS pass?
#
# `pass` is a no-operation placeholder. It does literally nothing —
# Python reads it, nods, and moves on to the next line.
#
# Why does it exist?
# Python requires at least one statement inside any block (if, for, def, class).
# If you have nothing to put there yet, pass fills the syntactic requirement
# without actually doing anything.
#
# Three common use cases:
#   🧪  TODO stub    →  mark code to be written later
#   🏗️  Empty class  →  define a class structure before filling it in
#   🔕  Silence       →  intentionally ignore a condition without acting on it
#
# ⚠️  Critical difference from continue:
#   pass     →  does nothing, then continues to the NEXT LINE in the same block
#   continue →  skips the rest of the block and jumps BACK TO THE LOOP TOP
#
# ⚠️  Indentation determines scope — see trace below.

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

# ── Example code ──────────────────────────────────────────────────────────────

sequence = [1, 2, 3]

for i in sequence:
    if i == 2:
        pass        # does nothing — falls through to print below
    print(i)        # always runs for every item

# Output:
# 1
# 2
# 3

# ── Real-world use: TODO placeholder ──────────────────────────────────────────
# 💡 pass lets you note that empty values need handling later
#    without breaking the loop or crashing the program.
#    Replace pass with real logic once the team decides what to do.

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == "":
        pass  # TODO: Handle Empty Value Later {Discuss with team on what to do with the empty value} Example below
    print(f"Name = {name}")

# ── Evolved version: replace empty with default ────────────────────────────────
# 💡 Once the team decides, the pass block becomes real logic.
#    Here: blank names are replaced with "unknown" before printing.

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == "":
        name = "unknown"  # Replaced replace() with direct assignment
    print(f"Name = {name}")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  📅  SECTION 4 — Task: Working Days Printer                             ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 TASK BREAKDOWN
#
# Goal: Print only working days from a full week list — skip weekends.
#
# Why continue is the right tool here (not break, not pass):
#   break  →  would stop the loop the first time Saturday is hit
#             — we'd never see Sunday, and we'd miss any weekdays after it
#   pass   →  would fall through and STILL print the weekend day
#   continue → skips Saturday and Sunday entirely and moves to next day ✅
#
# Two approaches shown:
#   Approach A — plain continue
#   Approach B — continue + for-else (confirms ALL days were processed)
#
# 💡 `day in Weekends` uses Python's `in` operator to check membership.
#    It returns True if day matches any item in the Weekends list.

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


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  📊  SECTION 5 — Summary Table                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 QUICK REFERENCE — ALL THREE STATEMENTS SIDE BY SIDE
#
# Use this table to decide which tool to reach for:
#
#   Need to STOP everything the moment a condition hits?  →  break
#   Need to SKIP one bad item and keep going?             →  continue
#   Need a PLACEHOLDER for logic not yet written?         →  pass
#   Need to CONFIRM the loop ran without interruption?    →  else (on the for)

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


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔐  SECTION 6 — Task: SQL Injection Scanner                            ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 REAL WORLD: SECURITY — INPUT VALIDATION
#
# SQL injection is one of the most common attack vectors in web applications.
# An attacker embeds raw SQL commands inside a field (like an email address)
# hoping it gets executed against your database.
#
# Classic examples of malicious payloads:
#   "'; DELETE FROM customers; --"   →  drops/empties a table
#   'Robert"); DROP TABLE Students;--'  →  the famous "Bobby Tables" attack
#   '1; DROP TABLE Users;'           →  drops the Users table
#
# Detection strategy used here:
#   • Scan each email for the ';' character — a tell-tale sign of SQL injection
#   • The moment one is found → break immediately (stop accepting ANY more input)
#   • Safe emails are processed normally until the threat is detected
#
# Why break and NOT continue here:
#   continue  →  would skip the bad email and keep going — dangerous!
#               an attacker could send multiple payloads in one batch
#   break     →  halts ALL processing the instant a threat is found ✅
#               treat the entire batch as compromised

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