# importing librieries
import secrets
import string
import random

# split different kind of characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
all_chars = lower + upper + digits + special

# password variable
password = ""

print("Welcome to the password generator.")
print("These are the special characters used in the generator -> !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
answer = str(input("Do you want to remove any of them? (y or n): "))

# check if the answer is correct
while answer != "y" and answer != "n":
    print("Not a valid input, please retry.")
    answer = str(input("Do you want to remove any of them? (y or n): "))

# if the answer is yes, update the string with the translate() module
if answer == "y":
    special_new = special.translate({ord(i): None for i in str(input("Which ones?\n"))})
    print("New special characters list ->", special_new)

# input section
psw_len = int(input("How long should the password be? "))
min_upper = int(input("Minimum Upper case: "))
min_lower = int(input("Minimum Lower case: "))
min_digits = int(input("Minimum Numbers: "))
min_spec = int(input("Minimum Special: "))

summ_min_inputs = min_lower + min_upper + min_spec + min_digits

# check if total min inputs > password length
while summ_min_inputs > psw_len:
    print("Number of total inputs greater than password length, please retry.")
    psw_len = int(input("How long should the password be? "))
    min_upper = int(input("Minimum Upper case: "))
    min_lower = int(input("Minimum Lower case: "))
    min_digits = int(input("Minimum Numbers: "))
    min_spec = int(input("Minimum Special: "))

    summ_min_inputs = min_lower + min_upper + min_spec + min_digits

# for loops to fill in the password variable
for i in range(min_upper):
    password += "".join(random.choice(secrets.choice(upper)))
                        
for i in range(min_lower):
    password += "".join(random.choice(secrets.choice(lower)))

for i in range(min_digits):
    password += "".join(random.choice(secrets.choice(digits)))

for i in range(min_spec):
    password += "".join(random.choice(secrets.choice(special)))

# adding the remaining position left
remaining = psw_len - min_upper - min_lower - min_digits - min_spec

for i in range(remaining):
    password += "".join(random.choice(secrets.choice(all_chars)))


# randomize upper, lower, digits and spec positions
password = list(password)
random.shuffle(password)

print("".join(password))