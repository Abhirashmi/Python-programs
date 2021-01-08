n=18
number_of_guesses=1
print("WELCOME TO GUESS THE NUMBER GAME !!!")
print("Enter your name :",str)
str=input("")
print("HEY !!! ",str)
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you have entered a number which is less than the hidden number . please input greater number.\n")
    elif guess_number>18:
        print("you have entered a number  greater than the hidden number . please input smaller number.\n ")
    else:
        print("CONGRATULATIONS ",str,"you WON !!!!",)
        print(number_of_guesses,"no.of guesses you took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1
if(number_of_guesses>9):
    print("Game Over")

