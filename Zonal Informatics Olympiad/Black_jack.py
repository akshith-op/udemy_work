import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []


def start_play(array):
    for i in range(2):
        start_card = random.choice(cards)
        array.append(start_card)
    return array


computer_start = start_play(computer)
user_start = start_play(user)

print(
    f"Your cards: {user_start}, Current score: {sum(user_start)}\nComputer's first card: {computer_start},Current score: {sum(computer_start)}  "
)


def hit(array):
    hit_card = random.choice(cards)
    if hit_card == 11:
        if sum(array) + hit_card > 11:
            hit_card = 1
    else:
        pass
    array.append(hit_card)
    return array


def with_blackjack(array):
    if sum(array) == 21 and len(array) == 2 and array == "user":
        is_game_over = True
        print(f"Your cards :{user_start}, Computer cards :{computer_start} ")
        print("You won with a blackjack!!!!!!")
    elif sum(array) == 21 and len(array) == 2 and array == "computer":
        is_game_over = True
        print(f"Your cards :{user_start}, Computer cards :{computer_start} ")
        print("computer won with a blackjack")


def compare(user_array, computer_array):
    user_sum = user_array
    computer_sum = computer_array
    if user_sum == computer_sum:
        return "Draw"
    elif computer_sum == 21:
        return "computer won"
    elif user_sum == 21:
        return "user won"
    elif computer_sum > user_sum:
        return "computer won"
    elif user_sum > computer_sum:
        return "user won"


is_game_over = False
with_blackjack(user)
with_blackjack(computer)
while is_game_over == False:
    sum_user = sum(user)
    sum_computer = sum(computer)
    if sum_user >= 21 or sum_computer >= 21:
        is_game_over = True
    else:
        user_choice = str(input("pls do you wanna 'y' or 'n'"))
        if user_choice == "y":
            hit(user)
        elif user_choice == "n":
            while sum(computer) < 16:
                hit(computer)
            is_game_over = True
        print(f"   Your final hand: {user}, final score: {sum(user)}")
        print(f"   Computer's final hand: {computer}, final score: {sum(computer)}")

result = compare(user, computer)
print(result)
