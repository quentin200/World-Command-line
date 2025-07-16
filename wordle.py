import random
import json


# first we convert the json containing all the english 5 letter word so that we can access it
with open('words.json', 'r') as file:
    words = json.load(file)

word_list = words['words']


word_to_guess = random.choice(word_list)
print(word_to_guess)






number_of_try = 0
user_input = input("Enter a 5 letter word: ").lower()
while number_of_try < 6:
    if len(user_input) != 5 or not user_input.isalpha():
        print("Invalid input. Please enter a 5 letter word.")
        user_input = input("Enter a 5 letter word: ").lower()

    if user_input not in word_list:
        print("Not an english word. Please try again.")
        user_input = input("Enter a 5 letter word: ").lower()
    


    number_of_try+=1   

    if user_input == word_to_guess:
        print("Congratulations! You found the word in ", number_of_try, " attempt !")
        break



    for i in range(len(user_input)):
        if user_input[i]==word_to_guess[i]:
            print("Letter ", user_input[i], " correctly placed")
        elif user_input[i] in word_to_guess:
            print("Letter ", user_input[i], " in word but not correctly placed")
        else:
            print("Letter ", user_input[i], " not in word to guess")
            
    print("Only ", 6-number_of_try, " attempts left")
   
    user_input = input("Enter a 5 letter word: ").lower()

