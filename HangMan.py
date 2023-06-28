import random
import os
import hangman_words
import art

chosen_word = random.choice(hangman_words.word_list)
hang_list =[]
count = 0
lives = 6

print(art.hangman_logo+"\n")

for i in range(len(chosen_word)):
  hang_list.insert(i,"_")
  count += 1

print(hang_list)
while(count>0 and lives != 0):
  guess = input("\nGuess a letter: ").lower()
  os.system('cls')
  if guess not in chosen_word :
        print(f"{guess} is not in the word")
        lives -= 1
        print(art.hangman_stages[lives])
  if guess in hang_list:
      print("You have already entered the letter,your life is lost")
      lives -= 1
      print(art.hangman_stages[lives])
      print(hang_list)
  else:
    for i in range(len(chosen_word) ):
        if chosen_word[i] == guess:
            hang_list[i] = guess
            count -= 1
    print(hang_list)

if count == 0 and lives !=0:
  print("You have WON")
elif lives == 0:
  print("You LOST")
  print(f"the actual word was {chosen_word}")
