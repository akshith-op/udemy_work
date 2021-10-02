import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_game_over = False
comp_ask = False
user = []
computer = []


def dist_cards(pivot, cards):
    for i in range(2):
        idx = random.choice(cards)
        pivot.append(idx)


def ask_card(pivot):
    aa = random.choice(cards)
    if aa == 11:
        if sum(pivot) > 21:
            aa = 1
            pivot.append(aa)


def compare(arr, brr):
    arr1 = sum(arr)
    arr2 = sum(brr)

    if arr1 == arr2:
        print("Draw")
    elif arr1 > arr2:
        print("user won")
    elif arr1 < arr2:
        print("computer won")


dist_cards(user, cards)
dist_cards(computer, cards)
while is_game_over == False:
    ask = input('please say "y" or "n": ')
    if ask == "y":
        ask_card(user)
    else:
        while is_game_over == False:
            if sum(pivot) < 16:
                ask_card(computer)
            else:
                is_game_over = True
