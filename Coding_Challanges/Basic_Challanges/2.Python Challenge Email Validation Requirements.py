# Python Challenge: Email Validation Requirements
# 1. Must not be empty
# 2. Must contain '.' and '@'
# 3. Must contain exactly one '@' symbol
# 4. Must end with '.com', '.org', or '.net'
# 5. Must not be longer than 254 characters
# 6. Must start and end with a letter or digit


email = "sahaakash6@gmail.com"   # Sample email input

email = email.strip()            # Remove spaces from start and end of the string


# Rule 1: Check if email is empty or None
# 'None' means no value, "" means empty string
if email is None or email == "":
    print("No email found")

else:

    # Rule 2: Email must contain '.' AND '@'
    # If either of them is missing → invalid
    if "." not in email or "@" not in email:
        print("Invalid email")

    # Rule 3: Email must contain exactly one '@'
    # count() counts how many times '@' appears
    elif email.count("@") != 1:
        print("More than 1 @ not allowed in email")

    else:

        # Rule 4: Email must end with allowed domains
        # endswith() checks the ending of the string
        # Tuple is used to check multiple endings
        if not email.endswith(('.com', '.org', '.net')):
            print("Restricted Organisation")

        # Rule 5: Email length must be <= 254 characters
        # len() returns the total number of characters
        elif len(email) > 254:
            print("Email is long")

        # Rule 6: Email must start and end with letter or digit
        # email[0] → first character
        # email[-1] → last character
        # isalnum() checks if it is a letter (A-Z, a-z) or number (0-9)
        elif not (email[0].isalnum() and email[-1].isalnum()):
            print("Invalid Email")

        # If all conditions pass
        else:
            print("Valid Email: ", email)


# ======================================== OR ========================================
email = "baraa@gmail.com"
valid = True
# Clean the String
email = email.strip()
# Email must not be empty
if email == "":
    print("Email cannot be empty.")
    valid = False
# Email must contain a '.' and '@'
if not('.' in email and '@' in email):
    print("Email must contain . and @")
    valid = False
# Email must contain exactly one '@' symbol
if email.count('@') != 1:
    print("Email must contain exactly one @.")
    valid = False
# Email must end with '.com', '.org', or '.net'
if not email.endswith(('.com', '.org', '.net')):
    print("Email must end with .com, .org, or .net")
    valid = False
# Email must not be longer than 254 characters
if len(email) > 254:
    print("Email must not be longer than 254 characters")
    valid = False
# Email must start and end with a letter or digit
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
    valid = False
if valid:
    print("Email is valid.")


# Python Challenge #2: Password Validation Requirements
# - Must not be empty
# - Must be at least 8 characters
# - Must include at least 1 uppercase
# - Must include at least 1 lowercase
# - Must not be same as the email
# - Must not contain any spaces
# - Must start and end with a letter or digit

email=""
password = ""
password = password.strip()

if password is None or password == "":
    print("Invalid Password")
else:
    if len(password) < 8:
        print("Password is less than 8 characters")
    elif password == email:
        print("Must not be same as the email")
    elif not any(char.isupper() for char in password):
        print("Must include at least 1 uppercase")
    elif not any(char.islower() for char in password):
        print("Must include at least 1 lowercase")
    elif not(password[0].isalnum and password[-1].isalnum):
        print("Must start and end with a letter or digit")
    else:
        print("Password is valid")