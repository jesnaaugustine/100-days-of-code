import os

Art=''' 
   ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                     /_______________\
'''

print(Art)
cont = 'yes'
dict ={}
while cont =='yes':
    name = input('What is your name:  ')
    bid =input('What is your bid?: $')
    dict[name.capitalize()]= float(bid)
    temp =input('Are there any other bidders? Type "yes" or "no"\n')
    cont = temp.lower()
    os.system('cls' if os.name == 'nt' else 'clear')
h = max(dict, key = dict.get)
print(f'The winner is {h} with a bid of ${max(dict.values())}')


