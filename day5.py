import string
import random
letters_l = string.ascii_lowercase
letters_u = string.ascii_uppercase

letters = list(letters_l)+list(letters_u)
numbers =['0','1','2','3','4','5','6','7','8','9']
symbols =['!','@','#','$','%','&','*','(',')']

print('Welcome to the Pypassword generator')
n_letters = int(input('How many letters would you like in your password\n'))
n_numbers = int(input('How many numbers would you like\n'))
n_symbols =int(input('How many symbols would you like?\n'))

password =[]
for i in range(n_letters):
    password.append(random.choice(letters))

for i in range(n_numbers):
    password.append(random.choice(numbers))

for i in range(n_symbols):
    password.append(random.choice(symbols))


random.shuffle(password)
print(''.join(password))


