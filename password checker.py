        #Password Checker

password = input("Enter your Password: ")
length = len(password)

print("Password length: " , length)

has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigit():
        has_digit = True

else: 
 has_special = True

print("Has Uppercase" , has_uppercase)
print("Has Lowercase" , has_lowercase)
print("Has Digit" , has_digit)
print("Has Special" , has_special)



