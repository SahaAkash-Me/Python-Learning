# Only one if between two statements and rest are elif and else
# starts with if
# if statement can stand alone but elif and else cannot

#---------------------------------------------
# if statement
#---------------------------------------------

score = 50
if score >= 90:
    print("A")      # In Python, indentation is the whitespace at the start of a line that defines a block of code.

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

#---------------------------------------------
# elif statement With Nested if
#---------------------------------------------

score = 85
submitted_project = True

if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score>= 70:
    print("C")
else:
    print("F")

#---------------------------------------------
# elif statement || and
#---------------------------------------------

score = 85
submitted_project = True

if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score>= 70:
    print("C")
elif score>= 60:
    print("D")
else:
    print("F")

#---------------------------------------------
# Independent if statements
#---------------------------------------------

score = 90
submitted_project = False

if score >=90:
    print("High Score")
else:
    print("Low Score")
# -------     -------
if submitted_project:
    print("Project Submitted")
else:
    print("Project is not submitted")

#---------------------------------------------
#                           Inline If & Match Case 
# inline if staement is also known as ternary operator
# inline if staement is only for quick checks & not for complex conditions
#---------------------------------------------

score = 90
submitted_project = False

#if score >=90:
 #   print("High Score")
#else:
#    print("Low Score")

"High Score" if score >=90 else "Low Score"

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

"High Score" if score >=90 else "Average Score" if score>=70 else "Low Score"

# grade = "High Score" if score >=90 else "Average Score" if score>=70 else "Low Score"
#print("grade")

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
    case _:
        print("Unknown Country")