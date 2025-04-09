import random
import os

def deal_card():
    cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
    r_card = random.choice(cards)
    return r_card

def calaculate_score(li):
    if sum(li)==21 and len(li)==2:
        return 0
    if 11 in li  and sum(li)>21:
        li.remove(11)
        li.append(1)
    return sum(li)
def compare(u_score,c_score):
    if u_score== c_score:
        return 'Draw'
    elif c_score ==0:
        return 'Lose, the opponent has blackjack'
    elif u_score ==0:
        return 'Win with a BlackJack'
    elif u_score>21:
        return 'You went over, you lose'
    elif c_score>21:
        return 'Opponenet went over, you Win'
    elif u_score>c_score:
        return 'You Win'
    else:
        return 'You lose'

def play_game():
    art = ''' 
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 '''
    print(art)
    user_cards =[]
    computer_cards =[]
    computer_score=-1
    user_score =-1
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calaculate_score(user_cards)
        computer_score = calaculate_score(computer_cards)
        print(f"your cards in hand : {user_cards}, your score: {user_score}")
        print(f"computers first card: {computer_cards[0]}")
        if user_score==0 or computer_cards==0 or user_score>21:
            is_game_over =True
        else:
            user_continue=input("Type 'y' to get another card, type 'n' to pass: ")
            if user_continue=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calaculate_score(computer_cards)

    print(f"your final hand : {user_cards}, final_score: {user_score}")
    print(f"computers final card: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        play_game()
if __name__=='__main__':
    play_game()
    


