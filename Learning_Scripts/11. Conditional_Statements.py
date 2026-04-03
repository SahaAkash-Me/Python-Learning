# =============================================================================
# PYTHON LEARNING NOTES: Conditionals — if, elif, else, inline if, match-case
# =============================================================================
# Author: Akash
# Purpose: Understanding Python's conditional branching from basic to advanced
# Focus: if/elif/else, nested conditions, logical operators, ternary, match-case
# =============================================================================


# ┌──────────────────────────────────────────────────────────────────────────┐
# │  📑  INDEX / TABLE OF CONTENTS                                          │
# ├──────────────────────────────────────────────────────────────────────────┤
# │                                                                          │
# │   1. 🔵  if Statement                    → Line  40      │
# │   2. 🔵🔴  if-else Statement             → Line  67      │
# │   3. 🔵🟡🔴  elif + Nested if            → Line 106      │
# │   4. 🔗  elif + and (Logical Operator)   → Line 153      │
# │   5. 🔀  Independent if Statements       → Line 198      │
# │   6. ⚡  Inline if (Ternary Operator)    → Line 239      │
# │   7. 🃏  match-case Statement            → Line 304      │
# │                                                                          │
# └──────────────────────────────────────────────────────────────────────────┘


# ┌─────────────────────────────────────────────────────────────────────────┐
# │  📖  QUICK RULES — Keep these in mind for all sections below           │
# ├─────────────────────────────────────────────────────────────────────────┤
# │                                                                         │
# │  ✅  Only ONE if  between two statements — it starts the chain         │
# │  ✅  elif and else CANNOT stand alone — they need an if above them     │
# │  ✅  if CAN stand alone — no elif or else is required                  │
# │  ✅  Indentation defines the block — Python uses spaces, not { }       │
# │  ✅  Conditions are evaluated TOP to BOTTOM — first True wins          │
# │  ✅  Once a branch runs, the rest of the chain is skipped              │
# │                                                                         │
# └─────────────────────────────────────────────────────────────────────────┘


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔵  SECTION 1 — if Statement                                           ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS if?
#
# The simplest conditional — runs a block ONLY when the condition is True.
# If the condition is False, the block is silently skipped.
# No else, no fallback — just "do this IF this is true, otherwise do nothing."
#
# Syntax:
#   if <condition>:
#       <block>   ← indented 4 spaces — this IS the block
#
# 💡 Indentation in Python is not style — it is SYNTAX.
#    The whitespace at the start of a line defines which block it belongs to.
#    Mis-indent and Python either crashes or runs the wrong block.

#---------------------------------------------
# if statement
#---------------------------------------------

score = 50
if score >= 90:
    print("A")      # In Python, indentation is the whitespace at the start of a line that defines a block of code.


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔵🔴  SECTION 2 — if-else Statement                                   ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS else?
#
# else is the fallback — it runs when the if condition is False.
# Together, if-else guarantees that exactly ONE of the two blocks always runs.
# There is no scenario where both run, and no scenario where neither runs.
#
# Mental model:
#   if   →  "if this is true, do THIS"
#   else →  "otherwise, do THAT"
#
# 💡 else has no condition of its own — it catches everything the if missed.
# 💡 There can only be ONE else per if-elif-else chain.
#
# Example 2b below shows a real-world use:
#   A % 2 == 0  checks divisibility — remainder 0 means even, remainder 1 means odd.

#---------------------------------------------
# else statement
#---------------------------------------------

score = 100
if score >= 90:
    print("A")      # In Python, indentation is the whitespace at the start of a line that defines a block of code.
else:
    print("B")


A = int(input("Enter a number: "))

if A % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔵🟡🔴  SECTION 3 — elif Statement with Nested if                     ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS elif?
#
# elif = "else if" — adds more branches between the opening if and closing else.
# Python checks each condition in order. The FIRST one that is True runs.
# All remaining branches are skipped — even if they would also be True.
#
# Chain structure:
#   if      →  first check
#   elif    →  second check  (only reached if all above are False)
#   elif    →  third check   (only reached if all above are False)
#   else    →  catch-all     (only reached if everything above is False)
#
# 📖 NESTED if
#
# A nested if is an if statement INSIDE another if block.
# It only runs if the outer condition is already True.
# Here: score >= 90 must be True before Python even looks at submitted_project.
#
# When to nest vs when to use `and`:
#   Nested if  →  when the inner condition only makes sense if the outer is True
#   and        →  when both conditions are equally important and independent
#   (see Section 4 for the `and` version of this same logic)

#---------------------------------------------
# elif statement With Nested if
#---------------------------------------------

score = 85
submitted_project = True

if score >= 90:
    if submitted_project:       # 🔵 Inner if — only checked when score >= 90
        print("A+")
    else:                       # 🔴 Inner else — score >= 90 but no project
        print("A")
elif score >= 80:               # 🟡 Only reached if score < 90
    print("B")
elif score>= 70:                # 🟡 Only reached if score < 80
    print("C")
else:                           # 🔴 Catch-all — score < 70
    print("F")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔗  SECTION 4 — elif + and (Logical Operator)                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 THE `and` OPERATOR
#
# `and` combines two conditions into one — BOTH must be True for the branch to run.
#   True  and True  →  True   ✅ (branch runs)
#   True  and False →  False  ❌
#   False and True  →  False  ❌
#   False and False →  False  ❌
#
# This is the flattened version of Section 3's nested if.
# Instead of nesting, we express both conditions on a single line:
#
#   score >= 90 and submitted_project
#   →  score must be 90+ AND the project must be submitted
#
# 💡 Flatter code is generally easier to read — prefer `and` over nesting
#    when both conditions are about the same decision.
#
# Notice the full grade ladder here: A+ → A → B → C → D → F
# The order matters — Python stops at the FIRST True condition.

#---------------------------------------------
# elif statement || and
#---------------------------------------------

score = 85
submitted_project = True

if score >= 90 and submitted_project:   # 🔗 Both must be True → A+
    print("A+")
elif score >= 90:                       # 🟡 Score 90+ but no project → A
    print("A")
elif score >= 80:                       # 🟡 Score 80–89 → B
    print("B")
elif score>= 70:                        # 🟡 Score 70–79 → C
    print("C")
elif score>= 60:                        # 🟡 Score 60–69 → D
    print("D")
else:                                   # 🔴 Below 60 → F
    print("F")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🔀  SECTION 5 — Independent if Statements                              ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 CHAINED vs INDEPENDENT
#
# Two completely separate if-else blocks check TWO unrelated things.
# They are NOT connected — both always run regardless of the other's result.
#
# Chained (if-elif-else):
#   Only ONE branch runs — Python stops after the first True
#
# Independent (if ... if ...):
#   BOTH blocks run — each makes its own decision independently
#
# When to use independent ifs:
#   ✅  The two checks are about different aspects (score vs project)
#   ✅  You want BOTH results printed, not just one
#   ✅  One outcome should not prevent the other from being evaluated
#
# 💡 The divider comment (# ------- -------) visually separates the two
#    independent blocks — a good documentation habit.

#---------------------------------------------
# Independent if statements
#---------------------------------------------

score = 90
submitted_project = False

if score >=90:                      # 🔵 Block 1: evaluates score
    print("High Score")
else:
    print("Low Score")
# -------     -------
if submitted_project:               # 🔵 Block 2: evaluates project — always runs
    print("Project Submitted")
else:
    print("Project is not submitted")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  ⚡  SECTION 6 — Inline if (Ternary Operator)                           ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS THE TERNARY OPERATOR?
#
# The inline if (also called ternary operator) squashes an if-else into one line.
# It is an EXPRESSION — it produces a value, not a statement.
#
# Syntax:
#   <value_if_true>  if  <condition>  else  <value_if_false>
#
# Full if-else version:           Inline version:
#   if score >= 90:               "High Score" if score >= 90 else "Low Score"
#       result = "High Score"
#   else:
#       result = "Low Score"
#
# ⚠️  Important notes:
#   • Writing the expression alone (without assigning) evaluates it but
#     does NOT print it — you need print() or assignment to see the result
#   • Use inline if for SIMPLE, quick checks only
#   • For complex logic (3+ conditions, nested) — stick to classical if-elif-else
#
# Chaining ternaries (shown below):
#   A if cond1 else B if cond2 else C
#   →  reads left-to-right: cond1? → A. cond2? → B. otherwise → C

#---------------------------------------------
#                   Inline If & Match Case 
# inline if staement is also known as ternary operator
# inline if staement is only for quick checks & not for complex conditions
#---------------------------------------------

score = 90
submitted_project = False

#if score >=90:
 #   print("High Score")
#else:
#    print("Low Score")

"High Score" if score >=90 else "Low Score"         # ⚡ Ternary — evaluates but not printed (no assignment)

# grade = "High Score" if score >=90 else "Low Score"
#print("grade")

#-------        -------            -------

score = 90
submitted_project = False

#if score >=90:
 #   print("High Score")
#elif score >= 70:
    #print("Average Score")
#else:
#    print("Low Score")

"High Score" if score >=90 else "Average Score" if score>=70 else "Low Score"   # ⚡ Chained ternary — 3 outcomes in one line

# grade = "High Score" if score >=90 else "Average Score" if score>=70 else "Low Score"
#print("grade")


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  🃏  SECTION 7 — match-case Statement                                   ║
# ╚══════════════════════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS match-case?
#
# match-case is Python's pattern matching — introduced in Python 3.10.
# It is the Pythonic equivalent of a switch-case from other languages.
#
# When to use match-case vs if-elif:
#   match-case  →  matching a single variable against fixed values (clean & fast)
#   if-elif     →  complex logical conditions (ranges, multiple variables, `and`/`or`)
#
# Syntax:
#   match <variable>:
#       case <value>:      →  runs if variable == value
#       case <a> | <b>:    →  pipe | means OR — matches either value
#       case _:            →  wildcard — the catch-all (equivalent to else)
#
# 💡 case _ is the default — always put it last, like else.
# 💡 | (pipe) lets one case match multiple values — no need for separate cases.
# ⚠️  Only works with Python 3.10+ — will SyntaxError on older versions.
#
# The commented-out if-elif block above the match shows exactly what
# match-case replaces — same logic, much cleaner syntax.

#---------------------------------------------
#           Case Match
# Can be used for matching case only || Works with Python V3.10+
# For complex logical we have to use the classical if_else statement
#---------------------------------------------
 
#country = "India"
#if country == "United States":
#    print("US")
#elif country == "India":
#    print("IN")
#elif country == "Egypt":
#    print("EG")
#elif country == "Germany":
#    print("DE")
#else:
#    print("Unknown Country")


match country:
    case "United States" | "USA":
        print("US")
    case "India" | "INDIA": # If we neeed to check muultiple values
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:                 # 🃏 Wildcard — catches any value not matched above
        print("Unknown Country")