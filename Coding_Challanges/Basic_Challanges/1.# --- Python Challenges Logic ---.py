# --- Python Challenges Logic ---

# 1. Check if a user's name is not empty and the age is greater than or equal to 18
# if name != "" and age >= 18:

name = input("Please enter your name : ")
age = int(input("Please enter your age : "))

print(bool(name != "" and age >= 18))


# 2. Check if the password is at least 8 characters long and does not contain spaces
# if len(password) >= 8 and " " not in password:

password = input("Please enter your password : ")
print(bool(len(password) >= 8 and " " not in password))


# 3. Check if a user's email is not empty, contains '@', and ends with '.com'
# if email != "" and "@" in email and email.endswith(".com"):

email = input("Please enter your email : ")
print (bool(email != "" and "@" in email and email.endswith(".com")))

# 4. Check if a username is a string, is not None, and is longer than 5 characters
# if isinstance(username, str) and username is not None and len(username) > 5:

username = input("Please enter your username : ")
print(bool(isinstance(username, str) and username is not None and len(username) > 5))

# 5. Check if the user is either an admin or a moderator, 
# and either they're not banned or they've verified their email
# if (role == "admin" or role == "moderator") and (not is_banned or email_verified):

role = input("Please enter your role (admin/moderator) : ")
is_banned = input("Are you banned? (yes/no) : ").lower() == "yes"
email_verified = input("Is your email verified? (yes/no) : ").lower() == "yes"