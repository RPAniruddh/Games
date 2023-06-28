import random
import art
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_list = []
user_score = 0
computer_list = []
computer_score = 0

print(art.Blackjack_logo)
def user():
    card_no = random.randint(0, 12)
    if card_no == 0:
        value= int(input(f"You have got an ace choose your score would you like 1 or 11 your current score is{calculate_score(user_list)} :-"))
        user_list.append(value)
    else:
        user_list.append(card_list[card_no])

def computer():
    card_no = random.randint(0, 12)
    computer_list.append(card_list[card_no])

def calculate_score(game_list):
    score =0
    for value in game_list:
        score += value
    return score

def continue_game(resume_game):
    while resume_game == 'y':
        user()
        computer()
        print(f"Your cards are {user_list}")
        user_score = calculate_score(user_list)
        if user_score > 21:
            print(f"Your score was {user_score} YOU LOOSE")
            resume_game = 'n'
            break
        elif user_score == 21:
            print(f"Computer score was {user_score} YOU WIN")
            resume_game = 'n'
            break
        while calculate_score(computer_list) < 17:
            computer()
        computer_score = calculate_score(computer_list)
        if computer_score > 21:
            if user_score > 21:
                print(f"Your score was {user_score} YOU LOOSE")
                resume_game = 'n'
            else:
                print(f"Computer score was {computer_score} YOU WIN")
                resume_game = 'n'
        elif computer_score == 21:
            print(f"Computer score was {computer_score} YOU LOOSE")
            resume_game = 'n'
        elif computer_score < 21:
            if computer_score == user_score:
                print(f"Computer score was {computer_score} and your score was {user_score} GAME DRAW")
                resume_game = 'n'
            elif computer_score < user_score:
                print(f"Computer score was {computer_score} and your score was {user_score} YOU WIN")
                resume_game = 'n'
            else:
                print(f"Computer score was {computer_score} and your score was {user_score} YOU LOOSE")
                resume_game = 'n'


def start_game():
    start = input("Do you want to play blackjack 'y' or 'n' ").lower()
    while start == 'y':
        user()
        computer()
        user()
        computer()

        print(f"Your cards are {user_list} and score is {calculate_score(user_list)}")
        print(f"The computer card is {computer_list[0]}")
        user_score = calculate_score(user_list)
        if user_score > 21:
            print(f"Your score was {user_score} you loose")
            break
        elif user_score == 21:
            print(f"Computer score was {user_score} you loose")
            break
        resume_game = input("Do you want another card 'y' or 'n' ").lower()
        if resume_game =='n':
            start ='n'
            while calculate_score(computer_list) < 17 :
                computer()
            computer_score = calculate_score(computer_list)
            if computer_score > 21:
                if user_score > 21:
                    print(f"Your score was {user_score} YOU LOOSE")
                else:
                    print(f"Computer score was {computer_score} YOU WIN")
            elif computer_score == 21:
                print(f"Computer score was {computer_score} YOU LOOSE")
            elif computer_score < 21:
                if computer_score == user_score:
                    print(f"Computer score was {computer_score} and your score was {user_score} GAME DRAW")
                elif computer_score < user_score:
                    print(f"Computer score was {computer_score} and your score was {user_score} YOU WIN")
                else:
                    print(f"Computer score was {computer_score} and your score was {user_score} YOU LOOSE")
        else:
            start = 'n'
            continue_game(resume_game)


start_game()
