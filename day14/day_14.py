import data
import random
import os
def random_num(exclude =50):
    ran =random.randint(0,len(data.data)-1)
    while ran==exclude:
        ran =random.randint(0,len(data.data)-1)
    return ran
    

def play():
    score =0
    first = random_num()
    second = random_num(first)
    con = True
    while con:
        
        data_A = data.data[first]
        data_B = data.data[second]
        print(f"Compare A: {data_A['name']}, a {data_A['description']}, from {data_A['country']}")
        print(data.vs)
        print(f"Aganist B: {data_B['name']}, a {data_B['description']}, from {data_B['country']}")
        A_B =input('Who has more followers? Type A or B: ')
        if A_B.upper() not in ['A','B']:
            print('Give proper input')
            os.system('cls' if os.name == 'nt' else 'clear')
            print(data.logo)
            continue
        if A_B=='A':
            if data_A['follower_count']>=data_B['follower_count']:
                os.system('cls' if os.name == 'nt' else 'clear')
                score+=1
                print(data.logo)
                print(f"You're right! Current score: {score}")
                first = second
                second = random_num(first)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(data.logo)
                print(f"Sorry, that's wrong.Final score: {score}")
                con = False
        else:
            if data_A['follower_count']<data_B['follower_count']:
                os.system('cls' if os.name == 'nt' else 'clear')
                score+=1
                print(data.logo)
                print(f"You're right! Current score: {score}")
                second = first
                first = random_num(second)

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(data.logo)
                print(f"Sorry, that's wrong.Final score: {score}")
                con = False

   
if __name__=='__main__':
    print(data.logo)
    play()

