import random

def guess_number():
    return random.randint(1,100)

def compare(guess,user):
    if guess<user:
        print('Too high')
        return 'con'
    elif guess>user:
        print('Too low')
        return 'con'
    else:
        print('Your guess is correct. You Win!!!!')
        return 'break'


if __name__=='__main__':
    print('Welcome to the Number Guessing game!!')
    print("I'm thinking of a number between 1 and 100")
    number = guess_number()
    c_input = True
    total =0
    while c_input:
        level=input('Choose a difficulty. Type "easy" or "hard":  ')
        if level.lower()=='easy':
            total = 10
            c_input = False
        elif level.lower()=='hard':
            total = 5
            c_input = False
        else:
            print('Choose correct dificulty.')
            c_input = True
    corect=False
    for i in range(1,total+1):
        print(f'You have {total+1-i} attempts remaining to guess the number')
        user = int(input('Make a guess: '))
        res = compare(number, user)
        if res =='break':
            corect = True
            break
    if not corect:
        print('you lost')

    




