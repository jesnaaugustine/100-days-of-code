'''
This is a hangman game 
'''

from english_words import get_english_words_set
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print('Welcome to hangman game!!!!')
words = list(get_english_words_set(['web2'], lower=True))
word = random.choice(words)
#print(word)
max_run = len(stages)
current = 1
found_count =0
word_list = list(word)
fill_list = ['_']*len(word_list)
print(' '.join(fill_list))
while current<=max_run:
    u_c = input('gusses a letter: ')
    tem_c=False
    for l in range(len(word_list)):
        if word_list[l] == u_c.lower():
            fill_list[l]=u_c
            found_count+=1
            tem_c = True
    print(' '.join(fill_list))
    if found_count==len(word_list):
        print('You Win! \U0001F600')
        exit()

    else:
        if not tem_c:
            print(stages[-1*current])
            current +=1
print('You lost \U0001F641')

    


    

    

            

