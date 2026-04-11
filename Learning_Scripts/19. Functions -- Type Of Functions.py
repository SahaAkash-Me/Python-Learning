# ==============================================================================
# 🐍 PYTHON FUNCTIONS — COMPLETE GUIDE (Every Example from the Tutorial)
# ==============================================================================
#
# 📌 A function is a small REUSABLE block of code that does ONE specific job.
# 💡 Think of it like a machine: it can take an input and return something back.
#
# ❓ WHY DO WE NEED FUNCTIONS?
# ─────────────────────────────
# 😓 As you code, you write logic to solve small problems.
# 🔁 Over time you face similar problems → you copy-paste the same logic.
# 💥 This causes CHAOS because:
#   • 🐛 If you find a bug, you must fix it in EVERY place you pasted it
#   • ❌ You will miss at least one — guaranteed in a large project
#   • ⚠️  Some parts run new logic, others run old logic → inaccurate results
#   • 📦 Code becomes massive, risky to touch, hard to read
#
# ✅ SOLUTION → Put the logic ONCE inside a function and just CALL it.
# 🏆 Benefits:
#   ✔ 🔧 Fix a bug once → every caller gets the fix automatically
#   ✔ 📖 Code is smaller (no repetition) → easier to read and understand
#   ✔ 🛡️  Safer to change — you touch one isolated piece, not many
#   ✔ 🤝 Better team collaboration — split work, one person per function
#   ✔ ⚡ Faster projects — reuse existing functions, don't reinvent the wheel
#   ✔ 🧩 Modularity — break big complex problems into smaller manageable pieces
#      (divide and conquer — this is how you think like a developer)
# ==============================================================================


# ==============================================================================
# 📋 INDEX — FIND ANY TOPIC BY LINE NUMBER
# ==============================================================================
#
#   SECTION  1 │ Basic Function Definition & Call .............. Line  88
#   SECTION  2 │ Why Functions (Morning Routine) ............... Line 113
#   SECTION  3 │ Three Sources of Functions .................... Line 186
#   SECTION  4 │ Parameters & Arguments ........................ Line 231
#   SECTION  5 │ clean_name — Evolution (Static → Parameter) ... Line 257
#   SECTION  6 │ Three Types of Variables (Scope & Lifetime) ... Line 315
#   SECTION  7 │ Multiple Parameters ........................... Line 381
#   SECTION  8 │ Positional vs Keyword vs Mixed Arguments ....... Line 418
#   SECTION  9 │ Default Parameters ............................ Line 457
#   SECTION 10 │ *args — Variable Positional Arguments ......... Line 500
#   SECTION 11 │ **kwargs — Variable Keyword Arguments ......... Line 561
#   SECTION 12 │ Return Values ................................. Line 609
#   SECTION 13 │ Return in clean_name (Practical Example) ...... Line 651
#   SECTION 14 │ Returning Multiple Values ..................... Line 702
#   SECTION 15A│ Function Types — Action Functions ............. Line 759
#   SECTION 15B│ Function Types — Transformation Functions ..... Line 800
#   SECTION 15C│ Function Types — Validation Functions ......... Line 857
#   SECTION 15D│ Function Types — Orchestrator Functions ........ Line 913
#   SECTION 16 │ Clean Code Rules (PEP 8 + Professional) ....... Line 996
#   SECTION 17 │ Complete Summary ............................. Line 1189
#
# ==============================================================================


import os
import math

# 🗂️ Safe log path — works in ALL VS Code run modes:
#   Run button (▶), Terminal, F5 Debugger, Interactive Window
# ⚠️  __file__ can fail in the Interactive Window, so we fall back to os.getcwd()
try:
    LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.log")
except NameError:
    LOG_PATH = os.path.join(os.getcwd(), "app.log")


# ==============================================================================
# 🔷 SECTION 1: FUNCTION DEFINITION & CALL — THE TWO PARTS          (Line 57)
# ==============================================================================
#
# 📝 SYNTAX:
#   def function_name():       ← DEFINITION  (describes what to do)
#       # body code            ← indented 4 spaces — belongs to the function
#
# 🔑 TWO PARTS:
#   1️⃣  Definition (declaration) — Python creates an object in memory with the
#       function name, body, and parameters. NOTHING RUNS YET.
#   2️⃣  Call — Python sees the name, finds it in memory, executes body top→bottom.
#       After it finishes, Python returns to where it left off in your code.

print("=" * 60)
print("SECTION 1: Basic Function Definition & Call")
print("=" * 60)

def greet():
    # 💬 This body only runs when the function is CALLED — not when defined
    print("Hello")

# 🔍 Python executes top to bottom:
# 1. Sees def greet → stores function object in memory (does NOT run the body)
# 2. Sees print("start") → runs it immediately
# 3. Sees greet() → finds it in memory → jumps into body → prints "Hello"
# 4. Exits function → returns to next line → prints "end"
print("start")
greet()      # ← CALL — this is what actually runs the body
print("end")
# 🖥️  Output: start → Hello → end


# ==============================================================================
# 🔷 SECTION 2: WHY FUNCTIONS — THE PROBLEM FIRST (Morning Routine) (Line 88)
# ==============================================================================
#
# 😓 First let's see the PROBLEM — copy-pasted code with no function.
# 🔁 The same logic written twice. If you want to add "Add milk", you must
#    add it in BOTH places — and in a real project you WILL miss at least one.

print("\n" + "=" * 60)
print("SECTION 2: Why Functions — the Problem vs the Solution")
print("=" * 60)

print("\n--- WITHOUT a function (bad — copy-paste problem) ---")

# ☕ First cup of coffee
print("Start the coffee machine")
print("Make the coffee")
print("Enjoy it")
print("Working for a while...")
# 😩 Need a second cup? Copy-paste everything again:
print("Start the coffee machine")   # ⚠️  same logic repeated
print("Make the coffee")             # 🐛 if there's a bug here we must fix it
print("Enjoy it")                    # ❌ in BOTH places (and might miss one)

# 💡 Imagine now we want to add "Add milk" — we'd have to add it in BOTH places.
# In a real project you might have it in 20 places. You WILL miss at least one.

print("\n--- WITH a function (solution) ---")

# ✅ Now the fix: put the logic ONCE inside a function
def make_cafe():
    # 🔧 ALL steps live in ONE place — fix here once, fixed everywhere
    print("Start the coffee mashine")  # 🐛 intentional typo to demo fix below
    print("Make the coffee")
    print("Add milk")       # ✅ added milk — only had to add it ONCE
    print("Enjoy the cafe")

print("Wake up at 5")
make_cafe()                  # ☕ first cup
print("Working for a while...")
make_cafe()                  # ☕ second cup — one line, no copy-paste!
print("Having lunch...")
make_cafe()                  # ☕ third cup — still just one line

# 🔧 Demo: fix the typo "mashine" → "machine" — ONE change, EVERY call benefits.
# (In the real file the typo is already fixed below — shown here for teaching)


# ==============================================================================
# 🔷 SECTION 3: THREE SOURCES OF FUNCTIONS IN PYTHON               (Line 134)
# ==============================================================================
#
# 📚 Already learned about functions like print(), len(), type(), int(), str() —
#    those are BUILT-IN. Now we learn about functions WE CREATE from scratch.
#
# 🏷️  SOURCE 1 — Built-in functions
#   • Come directly with Python. Always there. No install or import needed.
#   • Examples: print(), len(), type(), int(), str(), input(), sum()
#
# 🏷️  SOURCE 2 — Library functions (two types):
#   a) 📦 Python Standard Library — written by the Python team. Very specific,
#      not needed all the time. Must IMPORT before use. Already installed.
#      Examples: math, datetime, random
#   b) 🌍 External Libraries — written by the community / companies. Must INSTALL
#      first, then IMPORT, then use.
#      Examples: pandas (data analysis), matplotlib (charts),
#                numpy (arrays/numbers), requests (APIs)
#   🌟 Python's biggest strength: thousands of libraries — plug and play!
#
# 🏷️  SOURCE 3 — User-Defined Functions
#   • You write them from scratch for your specific project logic.
#   • No install or import — you define them yourself.
#
# 🥇 GOLDEN RULE (think like a professional):
#   BEFORE writing any function from scratch, always check:
#   1️⃣  Does a built-in function already do this? (fastest — always available)
#   2️⃣  Does the Python standard library have it? (just import and use)
#   3️⃣  Does an external library have it? (install, import, use)
#   4️⃣  Did a teammate already write this? (check the project first!)
#   5️⃣  ONLY THEN write it from scratch — don't reinvent the wheel.

print("\n" + "=" * 60)
print("SECTION 3: Three Sources of Functions")
print("=" * 60)

# 🔹 SOURCE 1: Built-in — no import needed, just use it
print("\n--- Built-in function ---")
word = "Python"
print(len(word))           # len() is built-in — always available

# 🔹 SOURCE 2a: Standard library — must IMPORT first
print("\n--- Standard library function (math module) ---")
# ⚠️  Without importing: math.ceil would cause a NameError (Python won't know it)
# import math   ← already imported at top of file
number = 4.2
print(math.ceil(number))   # math.ceil() rounds UP — module.function() syntax

# 🔹 SOURCE 3: User-defined — you write the definition yourself
print("\n--- User-defined function ---")

def greet_custom():
    """Say hello — user-defined, no install or import needed."""
    print("Hello!")

greet_custom()    # 📌 define first, then call


# ==============================================================================
# 🔷 SECTION 4: PARAMETERS & ARGUMENTS — HOW DATA FLOWS IN         (Line 182)
# ==============================================================================
#
# 🔀 NOT all functions work the same way. Different shapes:
#
#   Shape 1️⃣ : No input, no output    → just runs a block of code
#   Shape 2️⃣ : Input only             → takes data in, does something, stops
#   Shape 3️⃣ : Input + Output         → takes data in, transforms it, returns result
#   Shape 4️⃣ : Multiple inputs/outputs → multiple data goes in, multiple comes out
#
# 📖 TERMINOLOGY:
#   📥 Parameters = names in the DEFINITION  — describe what the function EXPECTS
#                   They are PLACEHOLDERS — empty, no value yet
#   📨 Arguments  = values in the CALL       — the ACTUAL DATA passed when calling
#                   Python takes the argument value and assigns it to the parameter
#                   (just like a variable assignment: parameter = argument)
#   🗑️  After the function ends → parameter value is DESTROYED (temporary)

print("\n" + "=" * 60)
print("SECTION 4: Parameters & Arguments")
print("=" * 60)

# 🔢 Simple example: a function that multiplies any value by two
def times_two(x):      # x = PARAMETER (placeholder, no value yet)
    print(x * 2)

# ▶️  When called: Python assigns argument → parameter (x = 3), executes, destroys x
times_two(3)           # 3 = ARGUMENT (real value that fills the placeholder)
times_two(10)          # 10 = ARGUMENT — same function, different data

# 📊 Quick comparison:
#   📥 Parameters → in the DEFINITION → placeholders
#   📨 Arguments  → in the CALL       → real values
#   📥 Parameter defines what the function EXPECTS
#   📨 Argument  provides the ACTUAL DATA


# ==============================================================================
# 🔷 SECTION 5: CLEAN NAME — EVOLUTION (Static → Parameter)        (Line 218)
# ==============================================================================
#
# 🔄 First let's see the problem: a function with a hardcoded (static) value.
# Then we evolve it to accept a parameter — making it flexible and reusable.

print("\n" + "=" * 60)
print("SECTION 5: clean_name — Evolution")
print("=" * 60)

print("\n--- Step 1: Static value inside function (not flexible) ---")

# ❌ Problem: always cleans the SAME name — can't reuse for different names
def clean_name_static():
    name = "  Maria  "         # 🔒 hardcoded — can't change from outside
    clean = name.strip().lower()
    print(clean)

clean_name_static()    # always "maria" — no way to pass a different name
clean_name_static()    # still "maria" — useless for other names

print("\n--- Step 2: Add a parameter (flexible!) ---")

# ✅ Solution: remove the hardcoded value and accept it as a parameter instead
def clean_name(name):          # name = parameter (raw input from outside)
    # 📥 name  = parameter   → holds the raw data, arrives from the caller
    # 🗃️  clean = local variable → holds the processed result
    clean = name.strip().lower()
    print(clean)

clean_name("  Maria  ")        # argument: Maria with spaces → cleaned: maria
clean_name("  KUMAR  ")        # argument: KUMAR messy → cleaned: kumar
# 🎉 Now we can pass ANY name — the function is generic and reusable!

# ⚠️  What happens if you call without argument?
# clean_name()  ← TypeError: missing required argument 'name'
# You can pass empty string though:
clean_name("")                 # prints nothing (empty) — no error


# ==============================================================================
# 🔷 SECTION 6: THREE TYPES OF VARIABLES — SCOPE & LIFETIME        (Line 261)
# ==============================================================================
#
# 📦 Three kinds of variables in Python:
#
#   1️⃣  PARAMETER     — defined in function definition parentheses
#                       Lives: only during function execution
#                       Accessible: ONLY inside the function
#
#   2️⃣  LOCAL VARIABLE — created with = inside the function body
#                        Lives: only during function execution → destroyed after
#                        Accessible: ONLY inside the function
#
#   3️⃣  GLOBAL VARIABLE — created OUTSIDE all functions
#                         Lives: entire program run → destroyed when program ends
#                         Accessible: EVERYWHERE (inside and outside functions)
#
# 💡 KEY INSIGHT:
#   🌍 Global variables: long life, accessible everywhere
#   ⏳ Local variables & parameters: short life, only inside the function
#   🗑️  When function ends → local variable AND its value are DESTROYED completely
#   🗑️  When function ends → parameter VALUE is removed (placeholder stays empty)

print("\n" + "=" * 60)
print("SECTION 6: Three Types of Variables — Scope & Lifetime")
print("=" * 60)

# ── 🧪 EXAMPLE 1: multiply_by_factor showing all three variable types ──

f = 2   # ← 🌍 GLOBAL VARIABLE: lives entire program, accessible everywhere

def multiply_by_factor(x):
    # 📥 x = PARAMETER        — placeholder, filled when called with argument
    # 🌍 f = GLOBAL VARIABLE  — accessed from inside the function (totally fine)
    # 🗃️  y = LOCAL VARIABLE   — created INSIDE, destroyed when function ends
    y = x * f    # y is local — only exists while this function runs
    print(y)
    # 🗑️  After this line: Python destroys y, removes value from x (x stays empty)

multiply_by_factor(3)    # x gets 3 → y = 3*2 = 6 → prints 6 → y destroyed
multiply_by_factor(5)    # x gets 5 → y = 5*2 = 10 → prints 10 → y destroyed

# ✅ Proof that local variable y does NOT exist outside the function:
# print(y)   ← NameError: name 'y' is not defined (y was destroyed)
# print(x)   ← NameError: name 'x' is not defined (x is parameter, only inside)
print(f"Global f is accessible anywhere: {f}")   # f is global → works fine

# ── 🧪 EXAMPLE 2: clean_name_advanced using a global control variable ──

print("\n--- Global variable controlling function behaviour ---")

# 🌍 Global variable acts as a "setting" that controls what the function does
case_rule = "lower"     # ← GLOBAL: accessible inside the function too

def clean_name_advanced(name):
    # 📥 name  = parameter
    # 🗃️  clean = local variable (holds processed result)
    # 🌍 case_rule = global variable (read from inside the function — allowed)
    clean = name.strip()

    # 🔍 Accessing the global variable case_rule inside the function
    if case_rule == "lower":
        clean = clean.lower()    # apply lower only when rule says so

    print(f"Raw: {name}")
    print(f"Clean: {clean}")

clean_name_advanced("  Maria  ")     # case_rule = "lower" → applies .lower()

# 🔄 Change the global variable → behaviour changes for ALL future calls
case_rule = "na"                     # now: do not apply lowercase
clean_name_advanced("  Maria  ")     # case_rule = "na" → does NOT apply .lower()

# ✅ Proof: you can access case_rule (global) outside the function too:
print(f"The rule is: {case_rule}")   # works — global is accessible everywhere

# ❌ But local variables and parameters are ONLY inside the function:
# print(clean)   ← NameError — local variable 'clean' doesn't exist here
# print(name)    ← NameError — parameter 'name' doesn't exist outside


# ==============================================================================
# 🔷 SECTION 7: MULTIPLE PARAMETERS                                 (Line 334)
# ==============================================================================
#
# 📥 A function can accept as many parameters as needed.
# 📌 Each parameter name must be unique inside the function.
# ⚠️  The call must pass a matching argument for EACH parameter.

print("\n" + "=" * 60)
print("SECTION 7: Multiple Parameters")
print("=" * 60)

def clean_name_full(first_name, last_name, country):
    """Accepts three inputs, cleans names, prints full name with country."""
    # 🗃️  Three parameters → three local variables
    first     = first_name.strip().lower()   # process first name
    last      = last_name.strip().lower()    # process last name
    full_name = first + " " + last           # combine into full name
    print(full_name + " from " + country)

clean_name_full("  Maria  ", "  Smith  ", "DE")   # three arguments


# ==============================================================================
# 🔷 SECTION 8: POSITIONAL vs KEYWORD vs MIXED ARGUMENTS           (Line 358)
# ==============================================================================
#
# 📨 Two ways to pass arguments to a function:
#
# 1️⃣  POSITIONAL ARGUMENTS:
#   Values matched by ORDER — first arg → first param, second → second, etc.
#   ⚠️  Risk: wrong order = wrong data (no error, but incorrect results!)
#
# 2️⃣  KEYWORD ARGUMENTS:
#   Values matched by PARAMETER NAME — order doesn't matter
#   Syntax: parameter_name=value in the CALL
#   ✅ Safer for functions with many parameters
#   ✅ More readable — you can see exactly which value goes where
#   ⚠️  Downside: more effort to write; renaming a parameter breaks all calls
#
# 3️⃣  MIXED ARGUMENTS:
#   You can mix both — but POSITIONAL MUST ALWAYS COME BEFORE KEYWORD
#   ❌ You cannot alternate between them
#
# 📏 RULE OF THUMB:
#   1–2 parameters  → positional is fine (easy to manage)
#   3+ parameters   → use keyword arguments (safer, avoids mistakes)

print("\n" + "=" * 60)
print("SECTION 8: Positional vs Keyword vs Mixed Arguments")
print("=" * 60)

print("\n--- Positional arguments (order matters!) ---")
clean_name_full("Maria", "Smith", "DE")      # correct order → correct result

# ⚠️  DANGER: wrong order → no error but nonsense output
# Python blindly maps: first arg → first_name, second → last_name, third → country
clean_name_full("DE", "Maria", "Smith")      # "de maria from smith" — messed up!
# 😬 Python doesn't care if the data makes sense — it trusts YOUR order.

print("\n--- Keyword arguments (order does NOT matter) ---")
# ✅ Using parameter names → Python knows exactly which value goes where
clean_name_full(country="DE", first_name="Maria", last_name="Smith")
clean_name_full(last_name="Smith", country="DE", first_name="Maria")  # same result

print("\n--- Mixed arguments (positional first, then keyword) ---")
# ✅ Positional MUST come before keyword — this is a strict Python rule
clean_name_full("  Maria  ", last_name="Smith", country="DE")    # OK
# clean_name_full(first_name="Maria", "Smith", "DE")  ← SyntaxError!
# ❌ Reason: "positional argument follows keyword argument"


# ==============================================================================
# 🔷 SECTION 9: DEFAULT PARAMETERS                                  (Line 409)
# ==============================================================================
#
# 🛡️  A default parameter has a VALUE assigned in the definition.
# 💡 If no argument is passed for it → Python uses the default value.
# ✅ This makes the parameter OPTIONAL in the function call.
#
# ⚠️  CRITICAL RULE: Parameters WITHOUT a default MUST come BEFORE those WITH defaults.
#   def func(a, b, c="default"):    ✓ correct order
#   def func(a, b="x", c):         ✗ SyntaxError — non-default follows default

print("\n" + "=" * 60)
print("SECTION 9: Default Parameters")
print("=" * 60)

def clean_name_default(first_name, last_name, country="N/A"):
    # ✅ country has a default → it is OPTIONAL in the call
    # ⚠️  first_name and last_name have NO default → they are REQUIRED
    first     = first_name.strip().lower()
    last      = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name + " from " + country)

clean_name_default("Maria", "Smith", "DE")   # country provided → uses "DE"
clean_name_default("Kumar", "Surish")        # country NOT provided → uses "N/A"

# 🔄 Adding default for last_name too (both last_name and country become optional):
def clean_name_all_defaults(first_name, last_name="N/A", country="N/A"):
    first = first_name.strip().lower()
    last  = last_name.strip().lower() if last_name != "N/A" else "N/A"
    print(first + " " + last + " from " + country)

clean_name_all_defaults("Kumar", "Surish")         # country uses default
clean_name_all_defaults("Kumar")                   # both last_name and country use defaults

# ❌ What BREAKS: non-default after default
# def broken(first_name, last_name="N/A", country):  ← SyntaxError!
# "SyntaxError: parameter without a default follows a parameter with a default"


# ==============================================================================
# 🔷 SECTION 10: *args — VARIABLE NUMBER OF POSITIONAL ARGUMENTS   (Line 451)
# ==============================================================================
#
# ❓ Problem: What if you don't know how many values will be passed?
# 😩 Naive solution: add more and more parameters → messy and fragile
# ✅ Real solution: use *args
#
# 📦 *args:
#   • Allows function to accept ANY number of positional arguments
#   • Python collects all positional arguments into a TUPLE
#   • Use when all values are the SAME kind of information (all numbers, etc.)
#   • The name "args" is just a convention — *values or *numbers also works

print("\n" + "=" * 60)
print("SECTION 10: *args — Variable Positional Arguments")
print("=" * 60)

print("\n--- BAD approach: fixed parameters (shows the problem) ---")

# ❌ Adding parameters one by one — fragile and doesn't scale
def total_bad(a, b):
    print(a + b)

total_bad(1, 2)    # works

# 😩 Need 3 values? Must rewrite the function AND add defaults to avoid breaking calls:
def total_with_defaults(a=0, b=0, c=0):
    print(a + b + c)

total_with_defaults(1, 2)        # works (c defaults to 0)
total_with_defaults(1, 2, 3)     # works
# total_with_defaults(1, 2, 3, 4)  ← TypeError: too many arguments
# 😩 We'd have to keep adding parameters forever — this is not smart!

print("\n--- GOOD approach: *args (the real solution) ---")

def total(*args):
    """
    Calculates the sum of any number of values.

    Args:
        *args (tuple): Any number of numeric values — as many as needed.

    Returns:
        None (prints the result)
    """
    # 📦 args is a TUPLE — Python collects all positional arguments into it
    print(type(args))    # <class 'tuple'> — confirms args is a tuple
    print(sum(args))     # sum() works directly on tuples

total(1, 2)              # tuple: (1, 2)
total(1, 2, 3)           # tuple: (1, 2, 3)
total(1, 2, 3, 4, 5, 6)  # tuple: (1, 2, 3, 4, 5, 6) — totally flexible!

# 📏 WHEN TO USE *args:
# → When passing SAME TYPE of information (list of numbers, list of names, etc.)
# → When the count of values is unknown at design time


# ==============================================================================
# 🔷 SECTION 11: **kwargs — VARIABLE NUMBER OF KEYWORD ARGUMENTS   (Line 511)
# ==============================================================================
#
# 📖 Use **kwargs when:
#   • You don't know how many values will be passed
#   • The values are DIFFERENT types of information (name, age, country, etc.)
#   • You need to pass key-value pairs
#
# 📚 **kwargs:
#   • Accepts any number of KEYWORD arguments
#   • Python collects them into a DICTIONARY (key = param name, value = arg value)
#   • Use when passing MIXED type information (different pieces about one thing)
#   • ⚠️  ONLY works with keyword arguments — positional args will cause an error

print("\n" + "=" * 60)
print("SECTION 11: **kwargs — Variable Keyword Arguments")
print("=" * 60)

def create_user(**kwargs):
    """
    Creates a user profile from any number of keyword arguments.

    Args:
        **kwargs (dict): Any key-value pairs describing the user.
    """
    # 📚 kwargs is a DICTIONARY — stores key=value pairs from the call
    print(type(kwargs))    # <class 'dict'> — confirms kwargs is a dict
    print(kwargs)

# 🎉 Each call can have COMPLETELY different keys — totally flexible
create_user(first_name="Mo", last_name="Salah", age=33, country="Egypt")
create_user(name="Ronaldo", country="Portugal")    # different fields, no age/last_name

# ⚠️  RULE: **kwargs requires KEYWORD arguments only
# create_user("Mo")   ← TypeError: takes 0 positional arguments but 1 was given

# 📊 COMPARISON SUMMARY:
#   *args    → collects positional args → TUPLE   → same type of info (numbers, etc.)
#   **kwargs → collects keyword args   → DICT    → mixed type info (profile, config)


# ==============================================================================
# 🔷 SECTION 12: RETURN VALUES — SENDING DATA OUT OF A FUNCTION    (Line 557)
# ==============================================================================
#
# 💡 So far functions print results — but PROGRAMS don't work with printed output.
# ✅ To REUSE a function's result later in the program → use RETURN.
#
# 📏 KEY RULE:
#   🖨️  Use PRINT  → when YOU (a human) want to see the output on screen
#   📤 Use RETURN → when the PROGRAM needs to use the result in later steps
#   ✅ You can use BOTH if needed
#
# 🔍 HOW RETURN WORKS:
#   1. Python executes the function body
#   2. Hits "return <value>" → grabs the value
#   3. Sends it back to the CALLER
#   4. Destroys all local variables
#   5. The caller stores the returned value in a variable
#
# ⚠️  IF NO RETURN: Python automatically returns NONE (not a real value — means nothing)

print("\n" + "=" * 60)
print("SECTION 12: Return Values")
print("=" * 60)

# 🔁 EXAMPLE: multiply_by_factor — now with RETURN instead of PRINT

f = 2    # global variable (already defined above, showing it again for clarity)

def multiply_by_factor_return(x):
    """
    Multiplies x by the global factor f.

    Args:
        x (float): Value to multiply.

    Returns:
        float: Result of x multiplied by f.
    """
    # 📥 x = parameter, 🗃️  y = local variable
    y = x * f      # calculate result, store in local variable y
    return y       # 📤 send y BACK to the caller — then y is destroyed

# ✅ The caller CAPTURES the returned value in a global variable
z = multiply_by_factor_return(3)   # z = returned value (6)
print(z)                           # now we can reuse z anywhere!

# ❌ WITHOUT return — everything returned is lost, can't reuse it
def multiply_no_return(x):
    y = x * f
    # no return — nothing comes back

result = multiply_no_return(3)
print(result)     # None — Python sends None when there's no return statement


# ==============================================================================
# 🔷 SECTION 13: RETURN — PRACTICAL EXAMPLE (clean_name)           (Line 608)
# ==============================================================================
#
# 🏗️  Real projects: we clean data to USE it later — not just to print it.
# 🖨️  Printing = for humans.   📤 Returning = for the program to keep working.

print("\n" + "=" * 60)
print("SECTION 13: Return in clean_name")
print("=" * 60)

print("\n--- Version 1: using print (output lost after function) ---")

def clean_name_print(name):
    cleaned = name.strip().lower()
    print(cleaned)    # 👁️  visible to human, but program can't reuse this value

clean_name_print("  Maria  ")   # program gets nothing back — output is lost

print("\n--- Version 2: using return (program can reuse the result) ---")

def clean_name_r(name):
    """
    Cleans a name string.

    Args:
        name (str): Raw name input.

    Returns:
        str: Cleaned lowercase name, or None if empty.
    """
    # 🛡️  Handle empty string — return None (cleaner to handle than empty string)
    if not name:       # "not name" is True for empty string, None, 0, etc.
        return None    # 1️⃣  first return: exit early with None

    # ✅ If we reach here, name has a real value — clean and return it
    cleaned = name.strip().lower()
    return cleaned     # 2️⃣  second return: exit with the processed value

# ✅ Capture the returned value — now the program can reuse it
clean_name_result = clean_name_r("  Maria  ")
print(clean_name_result)           # "maria" — stored in memory, reusable

print(clean_name_r(""))            # None — empty string → early return None
print(clean_name_r("  KUMAR  "))   # "kumar" — works with any name

# 📌 IMPORTANT: a function CAN have multiple return statements
# Python executes only the FIRST one it reaches (if/else controls which one)


# ==============================================================================
# 🔷 SECTION 14: RETURNING MULTIPLE VALUES                         (Line 657)
# ==============================================================================
#
# 🎁 A function can return MORE THAN ONE value using commas.
# 📦 Python packages them as a TUPLE.
# 🔓 The caller can UNPACK them into separate variables.

print("\n" + "=" * 60)
print("SECTION 14: Multiple Return Values")
print("=" * 60)

def clean_name_both_cases(name):
    """
    Cleans name and returns both lowercase and uppercase versions.

    Args:
        name (str): Raw name input.

    Returns:
        tuple: (lowercase_name, uppercase_name)
    """
    low_clean = name.strip().lower()       # lowercase version
    up_clean  = low_clean.upper()          # uppercase version (derived from low)
    return low_clean, up_clean             # 📦 returns a TUPLE: (low, up)

# 📦 Option 1: capture as a tuple
result_tuple = clean_name_both_cases("  Maria  ")
print(result_tuple)          # ('maria', 'MARIA') — tuple
print(type(result_tuple))    # <class 'tuple'>

# 🔓 Option 2: UNPACK into two separate variables (much cleaner)
low_name, up_name = clean_name_both_cases("  Maria  ")
print(low_name)    # maria
print(up_name)     # MARIA


# ==============================================================================
# 🔷 SECTION 15: FUNCTION TYPES BY PURPOSE
# ==============================================================================
#
# 🏗️  In real projects, functions are classified by WHAT THEY DO (their purpose).
# 💡 Understanding these patterns helps you design and read code like a professional.
#
# 4️⃣  MAIN TYPES:
#   1️⃣  Action functions        — do something in the system (side effects)
#   2️⃣  Transformation functions — take data in, change its shape, return result
#   3️⃣  Validation functions    — check rules, return True/False
#   4️⃣  Orchestrator functions  — call other functions in the correct order
# ==============================================================================


# ──────────────────────────────────────────────────────────────────────────────
# 🟠 SECTION 15A: ACTION FUNCTIONS                                  (Line 700)
# ──────────────────────────────────────────────────────────────────────────────
#
# 💥 Focuses on SIDE EFFECTS — doing something outside the function:
#   📁 Writing to a file
#   🗄️  Saving to a database
#   📧 Sending emails / notifications
#   🌐 Calling an external API
#   🖨️  Printing to screen
# ⚠️  Does NOT return a meaningful value — the job IS the action.
# 🏷️  Also called: side effect function, command function, handler, service function.

print("\n" + "=" * 60)
print("SECTION 15A: Action Functions")
print("=" * 60)

def write_log(message):
    """
    Appends a log message to the app.log file.
    Typical action function — the job IS the file write (side effect).

    Args:
        message (str): The log message to store.
    """
    # 📂 'with open' → opens the file, uses it, and AUTOMATICALLY closes/saves it
    # 📝 'a' mode = APPEND — adds to end of file, never deletes existing content
    # 🔤 encoding="utf-8" → supports all characters safely
    with open(r"D:\Python\Z app log\log.txt", "a", encoding="utf-8") as file:
         file.write(f"{message}\n")    # \n = new line — each message on its own line

# 📝 Each call stores a message in the file
write_log("App started")
write_log("User logged in")
write_log("App stopped")
# ℹ️  NOTE: The log is written to your custom Windows path below.
#   Change this path to wherever your log file lives on your machine.
WRITE_PATH = r"D:\Python\Z app log\log.txt"
print(f"Log written to: {WRITE_PATH}")

# 🔍 To verify, read and print the log content
with open(WRITE_PATH, "r", encoding="utf-8") as file:
    print("Log contents:")
    print(file.read())


# ──────────────────────────────────────────────────────────────────────────────
# 🟡 SECTION 15B: TRANSFORMATION FUNCTIONS                          (Line 749)
# ──────────────────────────────────────────────────────────────────────────────
#
# 🔄 Takes RAW DATA in → does calculations/manipulations → returns NEW SHAPE of data.
# 🏆 Most important type in DATA ENGINEERING and analytics.
# 🧠 Contains the CORE BUSINESS LOGIC that manipulates data.
# 🔧 Transformations include: calculate new values, convert format, extract info,
#    reshape data, clean data, normalize data.
# 🏷️  Also called: data function, calculation, utility, mapper.

print("\n" + "=" * 60)
print("SECTION 15B: Transformation Functions")
print("=" * 60)

def clean_and_split_email(email):
    """
    Cleans an email address and splits it into structured data.
    Classic transformation: raw string → structured dictionary.

    Args:
        email (str): Raw email address (may have spaces, wrong case, etc.)

    Returns:
        dict: {'username': ..., 'domain': ...}
    """
    # 🧹 Step 1: Clean the raw input (strip whitespace, normalize to lowercase)
    cleaned = email.strip().lower()

    # ✂️  Step 2: Split at '@' → split() returns a list: [username, domain]
    # Directly unpack the list into two variables
    username, domain = cleaned.split("@")

    # 📦 Step 3: Return as a structured dictionary (organised data)
    return {
        "username": username,
        "domain":   domain
    }

# ✅ Test with clean data
print(clean_and_split_email("sara@gmail.com"))

# ✅ Test with messy data — transformation handles it all
print(clean_and_split_email("  SARA@GMAIL.COM  "))    # spaces + uppercase → cleaned

# ✅ Test with another messy input
print(clean_and_split_email("  JOHN@YAHOO.COM  "))


# ──────────────────────────────────────────────────────────────────────────────
# 🟢 SECTION 15C: VALIDATION FUNCTIONS                              (Line 800)
# ──────────────────────────────────────────────────────────────────────────────
#
# ✅ Checks whether something is VALID or meets rules.
# ✅/❌ Returns a BOOLEAN (True / False) — answers a YES / NO question.
# 🚫 Does NOT change data. Does NOT interact with system.
# ❓ Just answers: "is this correct / allowed?"
#
# 🏗️  Uses in real projects:
#   🛡️  Validating user input before storing it
#   📋 Checking business rules
#   🗄️  Verifying data quality before inserting into a database
#   🔑 Checking user permissions
#
# 🏗️  DATA ENGINEERING: heavily used to protect pipelines from bad data.
# 📝 Naming convention: start with "is_" or "has_" to make it read like a question.
# 🏷️  Also called: checker function.

print("\n" + "=" * 60)
print("SECTION 15C: Validation Functions")
print("=" * 60)

def is_valid_password(password):
    """
    Checks if password meets the minimum length requirement of 8 characters.
    Does NOT change the password — just answers: is it valid?

    Args:
        password (str): The password to check.

    Returns:
        bool: True if length >= 8, False otherwise.
    """
    # 🔢 len() counts characters. The expression returns True or False directly.
    return len(password) >= 8

print(is_valid_password("123456"))      # ❌ False — 6 chars, below minimum
print(is_valid_password("12345678"))    # ✅ True  — exactly 8 chars
print(is_valid_password("supersecret")) # ✅ True  — more than 8 chars


def is_valid_email(email):
    """
    Checks if an email address has a basic valid format.
    Basic check: must contain '@' AND '.'.
    Does NOT change the email — just answers: is it valid?

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if both '@' and '.' are present, False otherwise.
    """
    # 🔍 'in' operator checks if a substring exists in the string
    # ⚙️  Both conditions must be True → use 'and' operator
    return "@" in email and "." in email

print(is_valid_email("saragmail.com"))    # ❌ False — missing @
print(is_valid_email("sara@gmail.com"))   # ✅ True  — has both @ and .
print(is_valid_email("sara@gmailcom"))    # ❌ False — missing .
print(is_valid_email("saragmailcom"))     # ❌ False — missing both


# ──────────────────────────────────────────────────────────────────────────────
# 🔵 SECTION 15D: ORCHESTRATOR FUNCTIONS                            (Line 855)
# ──────────────────────────────────────────────────────────────────────────────
#
# 🎯 Controls the FLOW of your program by calling other functions in correct order.
# 🚫 Does NOT contain complex logic — its job is COORDINATION.
# 🧩 Connects mini-functions like puzzle pieces into a complete workflow.
# 👀 Makes the program's big picture easy to understand at a glance.
# 💡 When you enter a new Python project → look for orchestrators first!
# 🏷️  Also called: workflow function, controller, pipeline, coordinator.

print("\n" + "=" * 60)
print("SECTION 15D: Orchestrator Function — Building a Mini Project")
print("=" * 60)

# 📋 REQUIREMENT:
# 1️⃣  Receive an email from the user
# 2️⃣  Check if it's valid — if not: log the problem
# 3️⃣  If valid: clean it and store it in a data structure
# 4️⃣  Log each step of the program

# 🔍 First, let's see the workflow as INLINE CODE (before wrapping in orchestrator):
print("\n--- Step 1: Inline workflow (before orchestrator) ---")

raw_email = input("Please enter your Email: ")   # simulating user input

write_log("Application started")

is_valid = is_valid_email(raw_email)

if not is_valid:
    # ❌ Email is bad → log the problem
    write_log("Invalid email received: " + raw_email)
else:
    # ✅ Email is good → clean and split it
    clean_email_data = clean_and_split_email(raw_email)
    write_log("Processed email: " + str(clean_email_data))
    print("Processed:", clean_email_data)

write_log("Application stopped")

# 🎯 Now let's WRAP this whole workflow inside an orchestrator function:
print("\n--- Step 2: Same logic wrapped in an Orchestrator function ---")

def process_user_email(email):
    """
    Orchestrates the full email processing workflow.
    Calls other functions in the correct order — does NOT contain logic itself.
    Just connects: validate → transform or log → log result.

    Args:
        email (str): Raw email address from the user.
    """
    # 🎯 Each line is a call to another specialized function
    # ⏱️  The orchestrator controls WHEN and in WHAT ORDER they run

    write_log("Application started")    # 🟠 action function

    if not is_valid_email(email):       # 🟢 validation function — controls flow
        write_log("Invalid email received: " + email)   # 🟠 action function
    else:
        clean_email = clean_and_split_email(email)       # 🟡 transformation function
        write_log("Processed email: " + str(clean_email))  # 🟠 action function
        print("Processed:", clean_email)

    write_log("Application stopped")   # 🟠 action function

# ✅ Now the MAIN program is just 2 lines:
email_from_user = "  SARA@GMAIL.COM  "    # simulate user input
process_user_email(email_from_user)       # one call does everything

# ❌ Test with invalid email:
process_user_email("invalidemail.com")    # missing @ → logs the problem

# 🧠 MINDSET IN REAL PROJECTS:
# 1️⃣  Write transformation functions  → manipulate/clean/reshape your data
# 2️⃣  Write validation functions      → check rules and data quality
# 3️⃣  Write action functions          → interact with files, APIs, DB, etc.
# 4️⃣  Connect them all in an orchestrator → complete readable workflow


# ==============================================================================
# 🔷 SECTION 16: CLEAN CODE RULES — WRITING PROFESSIONAL FUNCTIONS (Line 951)
# ==============================================================================
#
# 📖 These rules come from PEP 8 (Python's official style guide — google it!)
#    plus common professional standards used in real projects.
#
# ⚠️  If you ignore these, your pull request WILL be rejected in code review.
#
# 🏆 TWO LEVELS OF RULES:
#   ★  MUST RULES  (6) — ignore these and your PR gets rejected
#   ✦  LUXURY RULES (2) — not in PEP 8 but used by professionals at companies

print("\n" + "=" * 60)
print("SECTION 16: Clean Code Rules — Before & After Refactoring")
print("=" * 60)

# ── ❌ BAD FUNCTION (before refactoring — everything wrong) ──────────────────

# def DiskPrint(p, r):      # ✗ not snake_case, no verb, not descriptive
#     print(p)              # ✗ printing inside function — program can't reuse result
#     print(p - p*r/100)    # ✗ modifies parameter p directly — original value lost


# ── 🛠️  STEP-BY-STEP REFACTORING ─────────────────────────────────────────────

# ★ MUST RULE 1️⃣ : Use snake_case naming convention
#   Lowercase letters, words separated by underscores (official PEP 8 standard)
#   calculate_discount  ✓     DiskPrint  ✗     diskprint  ✗

# ★ MUST RULE 2️⃣ : Function name must start with a VERB and clearly describe the job
#   Avoid abbreviations — they mean nothing to others reading your code
#   calculate_discount  ✓     DiskPrint  ✗     discount  ✗ (no verb)
#   By just reading the name you must immediately know: "what does this do?"

# ★ MUST RULE 3️⃣ : Parameter names must clearly describe what value they hold
#   Never use single letters or abbreviations — full descriptive names only
#   price, rate  ✓     p, r  ✗     (what is p? what is r? nobody knows)

# ★ MUST RULE 4️⃣ : Always write a DOCSTRING
#   ❓ WHY A DOCSTRING AND NOT A # COMMENT?
#   → 🚫 When Python sees #, it treats it as a COMMENT and completely IGNORES it.
#     The comment is thrown away — your program knows nothing about it.
#   → ✅ When Python sees a triple-quoted string at the first line of a function,
#     it STORES it inside the function as documentation. It is NOT ignored.
#     You can retrieve it anytime using help(function_name).
#   Let's PROVE this with code:

print("\n--- Proof: # comment vs docstring ---")

def calculate_discount_comments(p, r):
    # Calculates the final price after discount
    # p = price, r = rate
    return p - p * r / 100

# 🔍 Calling help() on a function with ONLY # comments:
help(calculate_discount_comments)
# 🖥️  Output: no documentation found — Python ignored the # comments completely!
# You'd have to open the source code just to understand what this function does.

# ✅ Now the CORRECT version with a proper docstring — Python stores and shows it:
def calculate_discount_docstring(price, rate):
    """Calculates the final price after applying a discount."""
    return price - price * rate / 100

help(calculate_discount_docstring)
# 🖥️  Output: shows the docstring — instantly readable without opening source code!

# ★ MUST RULE 5️⃣ : Use RETURN not PRINT inside functions
#   Programs work with RETURNED values — print() is only for human eyes.
#   If you use print(), the result disappears after display — program can't reuse it.
#   ✅ Exception: action functions (write_log, send_email) whose whole JOB is output.
#     ❌ BAD:  def calc(price, rate): print(price - price * rate / 100)
#     ✅ GOOD: def calc(price, rate): return price - price * rate / 100

# ★ MUST RULE 6️⃣ : Never modify the parameter — use a local variable instead
#   The parameter holds the ORIGINAL (raw) input — keep it untouched.
#   Store the result in a NEW local variable so both versions are available.
#     ❌ BAD:  price = price - price * rate / 100   # original price is LOST forever
#     ✅ GOOD: final_price = price - price * rate / 100  # original price preserved


# ── ✅ FULL REFACTORED FUNCTION — ALL MUST RULES APPLIED ─────────────────────

def calculate_discount(price, rate):
    """Calculates the final price after applying a percentage discount."""
    # 📥 price = parameter     → ORIGINAL value, never modified
    # 🗃️  final_price = local variable → holds the NEW calculated value
    final_price = price - price * rate / 100   # rule 6️⃣ : new local var, not modifying price
    return final_price                          # rule 5️⃣ : return not print

discounted = calculate_discount(100, 20)
print(f"\nFinal price after 20% discount: {discounted}")   # 🖨️  print in MAIN code, not inside

# 💡 OPTIONAL SIMPLIFICATION (not a rule, just a style option):
# If the function has only ONE line of logic with no extra steps,
# you can skip the local variable and put the expression directly in return:
def calculate_discount_oneliner(price, rate):
    """Calculates the final price after applying a percentage discount."""
    return price - price * rate / 100     # expression goes directly into return

# ✅ Both versions are correct — use whichever is clearer for your situation.
# With more steps → local variable is clearer. One calculation → one-liner is fine.
print(f"One-liner version: {calculate_discount_oneliner(100, 20)}")


# ✦ LUXURY RULE 7️⃣ : Type Hints ─────────────────────────────────────────────
# 🏢 Not in PEP 8 but used by professionals at companies.
# 🐛 Most bugs in real projects come from WRONG DATA TYPES being passed.
# 💡 Type hints tell the caller exactly what data type each parameter expects
#    and what data type the return value will be.
# ⚠️  IMPORTANT: These are HINTS for humans — Python does NOT enforce them.
#            Python won't auto-convert your string to float based on the hint.
#
# 📝 Syntax:   parameter_name: type    (in definition)
#              -> return_type           (before the colon at end of def line)

def calculate_discount_typed(price: float, rate: float) -> float:
    """Calculates the final price after applying a percentage discount."""
    return price - price * rate / 100

# ⚠️  Without type hints, someone might call it like this:
# calculate_discount_typed(100, "20%")   ← no hint = easy to make this mistake
# ✅ With type hints, the developer sees: price: float, rate: float
# and immediately knows NOT to pass "20%" — it must be a number like 20.0

print(f"With type hints: {calculate_discount_typed(100.0, 20.0)}")


# ✦ LUXURY RULE 8️⃣ : Extended Docstring (Args + Returns sections) ────────────
# 🏢 Not in PEP 8 but you'll find this in every professional Python codebase.
# 📖 Extend the docstring to document each parameter AND the return value.
# 💡 This way anyone can understand the function perfectly without reading the code.

def calculate_discount_full(price: float, rate: float) -> float:
    """
    Calculates the final price after applying a percentage discount.

    Args:
        price (float): Original product price.
        rate  (float): Discount rate as a percentage number (e.g., 20 for 20%).

    Returns:
        float: Final price after the discount has been applied.
    """
    return price - price * rate / 100

# ✅ Now help() shows a complete, professional description:
help(calculate_discount_full)

print(f"Full professional version: {calculate_discount_full(200.0, 10.0)}")


# ==============================================================================
# 🔷 SECTION 17: COMPLETE SUMMARY — ALL SHAPES & TYPES            (Line 1089)
# ==============================================================================
#
# 📐 SHAPES (based on data flow):
# ────────────────────────────────────────────────────────────────────────────
#  1️⃣  No input,  no output   → def greet(): print("Hello")
#  2️⃣  Input,     no output   → def write_log(msg): file.write(msg)
#  3️⃣  Input  →  output       → def clean_name(name): return cleaned
#  4️⃣  Multi-in → output      → def calc_discount(price, rate): return result
#  5️⃣  Input  →  multi-out    → def both_cases(name): return low, up
#
# 🎯 TYPES (based on purpose):
# ────────────────────────────────────────────────────────────────────────────
#  🟠 Action Function:         Makes things happen outside the program
#                              write_log(), save_to_db(), send_email(), call_api()
#
#  🟡 Transformation Function: Takes data in → changes shape → returns new data
#                              clean_name(), calc_discount(), parse_record()
#
#  🟢 Validation Function:     Checks a rule → returns True/False
#                              is_valid_email(), is_valid_password(), has_permission()
#
#  🔵 Orchestrator Function:   Calls other functions in order → controls the flow
#                              process_user_email(), run_pipeline(), handle_request()
#
# 📏 CLEAN CODE RULES (PEP 8 + professional standards):
# ────────────────────────────────────────────────────────────────────────────
#  ★ ✔ snake_case names            → calculate_discount  not  DiskPrint
#  ★ ✔ Verb + descriptive name     → calculate_discount  not  discount
#  ★ ✔ Descriptive parameter names → price, rate  not  p, r
#  ★ ✔ Docstring at first line     → triple-quoted string with args + returns
#  ★ ✔ Use return, not print       → programs work with values, not printed text
#  ★ ✔ Don't modify parameters     → use a local variable instead
#  ✦ ✔ Type hints (luxury rule)    → price: float, rate: float -> float
#  ✦ ✔ Extended docstring (luxury) → Args: and Returns: sections
#
# 📨 ARGUMENT RULES:
# ────────────────────────────────────────────────────────────────────────────
#  Positional args  → matched by ORDER     → risky for 3+ params
#  Keyword args     → matched by NAME      → safe, readable, more effort
#  Mixed            → positional THEN keyword (never keyword first)
#  Default params   → non-defaults FIRST, defaults LAST
#  *args            → any number of positional → collected as TUPLE
#  **kwargs         → any number of keyword   → collected as DICT
#
# 📦 VARIABLE SCOPE:
# ────────────────────────────────────────────────────────────────────────────
#  🌍 Global:    outside functions → long life → accessible EVERYWHERE
#  🗃️  Local:     inside function   → short life → accessible ONLY inside function
#  📥 Parameter: function input    → short life → accessible ONLY inside function
# ==============================================================================

print("\n" + "=" * 60)
print("✅  All sections completed successfully!")
print("=" * 60)