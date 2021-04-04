#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass_easy = ""

for _ in range(nr_letters):
    index = random.randint(0, len(letters)-1)
    pass_easy += letters[index]

for _ in range(nr_numbers):
    index = random.randint(0, len(numbers)-1)
    pass_easy += numbers[index]

for _ in range(nr_symbols):
    index = random.randint(0, len(symbols)-1)
    pass_easy += symbols[index]

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pass_hard = pass_easy
pass_list = list(pass_hard)

random.shuffle(pass_list)

pass_hard = "".join(pass_list)

print(f"Easy password: {pass_easy}\nHard password: {pass_hard}")