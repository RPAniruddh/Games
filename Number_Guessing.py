import random
import art

def easy(number):
    flag = False
    chances = 10
    print(f"You have {chances} chances to figure out the number")
    while chances != 0:
        user_guess = int(input("Enter your guess "))
        if user_guess == number:
            chances = 0
            flag = True
        elif user_guess > number:
            print("You're guess is too high")
            chances -= 1
            print(f"remaining chances are {chances}")
        else:
            print("the number is too low")
            chances -= 1
            print(f"remaining chances are {chances}")
    if flag == True:
        print("YOU WON ")
    else:
        print("YOU LOST")     

def hard(number):
    flag = False
    chances = 5
    print(f"You have {chances} chances to figure out the number")
    while chances != 0:
        user_guess = int(input("Enter your guess "))
        if user_guess == number:
            chances = 0
            flag = True
        elif user_guess > number:
            print("You're guess is too high")
            chances -= 1
            print(f"remaining chances are {chances}")
        else:
            print("the number is too low")
            chances -= 1
            print(f"remaining chances are {chances}")
    if flag == True:
        print("YOU WON ")
    else:
        print("YOU LOST")     

print(art.number_guessing)
print("The computer is guessing a number between 1 and 100 (both included) can you guess it?")
number = random.randint(1, 100)
print(number)
option = input("which level of difficulty do you prefer 'EASY' or 'HARD' :- ").lower()
if option == "easy":
    easy(number)
elif option == "hard":
    hard(number)
else:
    print("INVALID CHOICE")
