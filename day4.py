import random
# Rock
Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
li = [Rock,Paper,Scissors]
h_c =int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))

if h_c<len(li):
    print(f'You choose:{h_c}\n')
    print(li[h_c])
else:
    print('invalid Number')
    exit(1)
c_c = random.randint(0,2)
print(f'Computer Choose:{c_c}\n')
print(li[c_c])

if h_c==0 and c_c==2:
    print('you Wins!')
elif h_c> c_c:
    print('you Wins.')
elif h_c == c_c:
    print('Its a draw')
else:
    print('you lose')



