import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
characters = list(characters)
key = characters.copy()

random.shuffle(key)

print(f"characters : {characters}")
print(f"key : {key}")

plain_text = input("Enter original text: \n")
cipher_text = ""

for letter in plain_text:
    index = characters.index(letter)
    cipher_text += key[index]

print(f"Your encrypted message is: {cipher_text}")

plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += characters[index]

print(f"Your oroginal mesaage is: {plain_text}")