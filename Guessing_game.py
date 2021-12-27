secret_number = '9'
print("Guess the correct digit between 0-9\t'Hint: multiple of 3'\nYou only have 3 guesses!!")
guess_count = 0
guess_limit = 3
while guess_count < guess_limit  :
    chance = input("Guess :")
    guess_count += 1
    if chance == secret_number:
        print("Congratulations! You guessed the right number")
        break
    else:
        print("wrong")
else:
    print("Sorry! You failed!")
print("Game Over")