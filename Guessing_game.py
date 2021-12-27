#Declaring and initializing variables
secret_number = '9'
guess_count = 0
guess_limit = 3
#Printing Instructions
print("Guess the correct digit between 0-9\t'Hint: multiple of 3'\nYou only have 3 guesses!!")
#Beginning of "while" loop
while guess_count < guess_limit  :
    chance = input("Guess :")
    #Incrementing counter for every turn
    guess_count += 1
    #Comparing Input and Secret number
    if chance == secret_number:
        print("Congratulations! You guessed the right number")
        break
    else:
        print("wrong")
else:
    print("Sorry! You failed!")
print("Game Over")
