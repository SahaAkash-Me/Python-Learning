# =============================================================================
#                            PYTHON WHILE LOOP GUIDE
# =============================================================================
# Author Notes:
# This section explains how Python while loops work using diagrams,
# flowcharts, examples, and comparisons with for loops.
#
# Topics Covered:
# 1. What is a While Loop
# 2. While Loop Flowchart
# 3. for loop vs while loop
# 4. While Loop Examples
# 5. Dynamic Input Loop
# 6. While True Pattern
# =============================================================================



# =============================================================================
# SECTION 1: WHILE LOOP INTRODUCTION
# =============================================================================

# ╔═════════════════════════════════════════════════════════════════════════╗
# ║                            While Loop                                   ║
# ║                                                                         ║
# ║              Repeats a block of code - over and over                    ║
# ║                    as long as condition is True!                        ║
# ╚═════════════════════════════════════════════════════════════════════════╝

# While : Two design available -->  While Condition ||  While True



# =============================================================================
# SECTION 2: WHILE LOOP FLOWCHART
# =============================================================================

# =============================================================================
# While Loop Flowchart (ASCII Art)
# =============================================================================
#
#                        ┌───────────────┐
#                        │     START     │
#                        └───────┬───────┘
#                                │
#                                ▼
#                      ┌─────────────────────────────┐
#                      │        CONDITION ?          │  ← Your Condition
#                      │     (while condition:)      │
#                      └───────────────┬─────────────┘
#                                      │
#                               ┌──────┴──────┐
#                      True     │             │     False
#                               ▼             ▼
#                   ┌────────────────┐   ┌─────────────┐
#                   │  Do Something  │   │    END      │
#                   │ (loop body)    │   └─────────────┘
#                   └────────┬───────┘
#                            │
#                            └────────────────────────────┐
#                                                         │
#                                      Risk! Unknown Times!  ← Infinite loop danger if condition never becomes False
#                                                         │
#                            ┌────────────────────────────┘
#                            │   (loop back)
#                            └────────────────────────────► (back to CONDITION)
#
# Key Warnings:
# - If condition never becomes False → infinite loop (Risk!)
# - Always ensure the body changes something that affects the condition
#
# =============================================================================



# =============================================================================
# SECTION 3: DIFFERENCE BETWEEN FOR LOOP AND WHILE LOOP
# =============================================================================

# =============================================================================
# DIFFERENCE BETWEEN for loop vs while loop (ASCII Flowchart Comparison)
# =============================================================================
#
#   FOR LOOP: Known / Predetermined number of iterations
#   ────────────────────────────────────────────────────────────────
#
#           Predetermined Sequence
#                [1, 2, 3]
#                   │
#                   ▼
#             ┌───────────────┐
#             │    Iterator   │  ← for i in [1,2,3]:
#             └───────┬───────┘
#                     │
#                     ▼
#           ┌─────────────────────┐
#           │   Last item ?       │  ← Hidden check: "Is there next?"
#           └──────────┬──────────┘
#                      │
#             ┌────────┴────────┐
#      True   │                 │  False
#             ▼                 ▼
#         ┌─────────────┐   ┌─────────────────┐
#         │    END      │   │  Do Something   │  ← print(i) / body
#         └─────────────┘   └────────┬────────┘
#                                     │
#                                     └──────────────────────┐
#                                                            │
#                                               (Next item? → back to Last item?)
#
#   Key FOR characteristics:
#   - Known / fixed number of iterations (#1: predefined sequence)
#   - Iteration managed automatically (next(), StopIteration)
#   - No "Risk!" of infinite loop (unless iterable is infinite)
#   - Natural fit: looping over lists, ranges, files, etc.
#
#
#   WHILE LOOP: Condition-based, Unknown number of iterations
#   ────────────────────────────────────────────────────────────────
#
#                        START
#                          │
#                          ▼
#               ┌─────────────────────────────┐
#               │      CONDITION ?            │  ← while condition:
#               │   (Your custom check)       │
#               └───────────────┬─────────────┘
#                               │
#                      ┌────────┴────────┐
#               True   │                 │  False
#                      ▼                 ▼
#           ┌─────────────────┐     ┌─────────────┐
#           │  Do Something   │     │    END      │
#           │  (loop body)    │     └─────────────┘
#           └────────┬────────┘
#                    │
#                    └──────────────────────────────┐
#                                                   │
#                                        Risk! Unknown Times!
#                                        (Infinite loop possible
#                                         if condition never False)
#                                                   │
#                                    (loop back to CONDITION)
#
#   Key WHILE characteristics:
#   - Unknown / variable number of iterations
#   - You must manually update variables inside body
#     so condition eventually becomes False
#   - High risk of infinite loops (forgotten counter increment, etc.)
#   - Natural fit: user input until 'quit', waiting for event, retry logic
#
# =============================================================================



# =============================================================================
# SECTION 4: QUICK SUMMARY TABLE
# =============================================================================

# =============================================================================
# Quick Summary Table
# ┌───────────────┬───────────────────────────────┬────────────────────────────┐
# │ Aspect        │ for loop                      │ while loop                 │
# ├───────────────┼───────────────────────────────┼────────────────────────────┤
# │ Iterations    │ Known / fixed                 │ Unknown / dynamic          │
# │ Control       │ Automatic (iterator)          │ Manual (you change vars)   │
# │ Risk          │ Low (ends when iterable done) │ High (infinite loop risk)  │
# │ Best for      │ Lists, ranges, files, strings │ Until condition met (input,│
# │               │                               │  retry, game loops)        │
# └───────────────┴───────────────────────────────┴────────────────────────────┘
#
# =============================================================================



# =============================================================================
# SECTION 5: BASIC WHILE LOOP EXAMPLES
# =============================================================================

# While Loop Flow (compact from drawing)
#
#   i = 1                     ← # Initialization
#      │
#      ▼
# while i < 4:                ← # Condition
#    │
#    ▼
# print(i)                    ← # Body
#    │
#    ▼
# i += 1                      ← # Update
#    │
#    └─────── loop back ──────┘
#
# When condition False → End


i = 1
while i < 4:
    print(i)
    i += 1


count = 1

while count <= 5:
    print(count)
    count += 1



# =============================================================================
# SECTION 6: WHILE LOOP WITH USER INPUT
# =============================================================================

# While Loop With Dynamic Value

answer = ""

while answer != "yes":
    answer = input("Do You Agree? (Yes / No): ")
    print("Thanks")



# =============================================================================
# SECTION 7: INPUT SANITIZATION VERSION
# =============================================================================

# Modified Version

answer = ""

while answer.strip().upper() != "YES":
    answer = input("Do You Agree? (Yes / No): ")
    print("Thanks")



# =============================================================================
# SECTION 8: WHILE TRUE PATTERN
# =============================================================================

# While True loop runs forever unless break is used.
# This is useful when we don't know how many iterations are needed.

while True:
    answer = input('Agree ? : ')
    if answer.strip().lower() == "yes":
        break
    print("Thanks")



# =============================================================================
# SECTION 9: VISUAL FLOW EXPLANATIONS
# =============================================================================

# ===============================
# WHILE CONDITION LOOP
# ===============================

# i = 1
# while i < 4:
#     print(i)
#     i += 1

# Flow:

#      ┌─────────────┐
#      │  Check i<4  │
#      └──────┬──────┘
#             │
#        True │
#             ▼
#        print(i)
#             │
#          i = i + 1
#             │
#             └───────────↺ (repeat)
#
# If condition becomes False
#             ▼
#            End

# Notes:
# - Loop exits automatically when condition becomes False
# - Safer and easier to read
# - Mostly used with counters or limited retries



# ===============================
# WHILE TRUE LOOP
# ===============================

# while True:
#     x = input("Type something: ")
#
#     if x == "stop":
#         break

# Flow:

#      ┌─────────────┐
#      │ while True  │
#      └──────┬──────┘
#             │
#             ▼
#       x = input()
#             │
#             ▼
#      ┌─────────────┐
#      │ x == "stop"?│
#      └──────┬──────┘
#             │
#        No   │   Yes
#             │
#             ▼
#        Repeat Loop
#             │
#             ▼
#           break
#             │
#            End

# Notes:
# - Runs forever unless break is used
# - More flexible
# - Risk of infinite loop
# - Used for:
#   • waiting for user input
#   • server processes
#   • APIs / streams