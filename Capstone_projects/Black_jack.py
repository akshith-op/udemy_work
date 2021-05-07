# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     
print(logo)
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user = []
computer = []
is_game_over = False
def start_cards(array):
    for i in range(2):
        hit_card = random.choice(cards)
        array.append(hit_card)
    return array
user_start_cards = start_cards(user)
computer_start_cards = start_cards(computer)
if sum(user_start_cards) == 21:
    print(f'Win with a Blackjack 😎')
elif sum(computer_start_cards) == 21:
    print('Lose, opponent has Blackjack 😱')
print(f'   Your cards: {user_start_cards}, current score: {sum(user)}')
print(f"   Computer's first card: {computer_start_cards[0]}")


        

    
    
    
def ask_card(array):
    hit_card = random.choice(cards)
    array.append(hit_card)
    return array

def calalculate_score(array):
    sum_user = sum(array)
    
    if sum(array) == 21 and len(array) == 2:
        if array == 'user':
            print("Win with a Blackjack 😎")
        elif array == 'computer':
            print("Lose, opponent has Blackjack 😱") 

    elif 11 in array and sum(array) > 21:
        array.remove(11)
        array.append(1)

                
                
    
    
def compare(user_sum,computer_sum):
    
    if user_sum == 21:
        return "Win with a Blackjack 😎"

    elif user_sum == computer_sum:
        return "Draw 🙃" 

    elif computer_sum == 21:
        return "Lose, opponent has Blackjack 😱"

    elif user_sum > 21:
        return "You went over. You lose 😭"

    elif computer_sum > 21:
        return "Opponent went over. You win 😁"

    elif user_sum > 21 and computer_sum > 21:
        
        return "You went over. You lose 😤" 
    elif computer_sum > user_sum:
        return "You lose 😤" 
    elif computer_sum < user_sum:
        return "You win 😃"


calalculate_score(user)
calalculate_score(computer)

    
    
        
sum_user = sum(user) 
computer_score = sum(computer)

is_game_over = False    
while is_game_over == False:
    sum_user = sum(user)
    computer_score = sum(computer)
    if sum_user == 0 or computer_score == 0 or sum_user >= 21 or computer_score >= 21:
        is_game_over = True
    else:
        hit = str(input("Type 'y' to get another card, type 'n' to pass: "))
        if hit == 'y':
            all_user_cards = ask_card(user)
            sum_user = sum(user)
            print(f"    Your cards: {all_user_cards}, current score: {sum(user)}")
        else:
            hit == 'n'
            while computer_score < 16:
                all_computer_cards = ask_card(computer)
                computer_score = sum(computer)
            is_game_over = True
print()
print(f'   Your final hand: {user}, final score: {sum_user}')
print(f"   Computer's final hand: {computer}, final score: {computer_score}")




result = compare(sum_user,computer_score)
print(result)    


# %%



