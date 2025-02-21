# Write a program that generates a random number and asks the user to guess it.

# If the player's guess is higher than the actual number, the program displays "Lower number please".
# Similarly, if the user's guess is too low, the program prints "higher number please".
# When the user guesses the correct number, the program displays the number of guesses the player used to arrive the number.

#------------ MY CODE -----------------# 
# import random

# # Getting choices
# def perfect_guess():
#     print("Welcome to The Perfect Guess!") 
#     comp_choice = random.randint(0, 11)
#     counter = 0
#     while True:
#         user_choice= int(input("Enter a number from 0-10 : "))
#         counter += 1
    
#         if (user_choice<0 or user_choice>10) :
#             print("Please guess a number between 0 and 10!")
#             continue
#         if user_choice == comp_choice :
#             print(f"Your guess was correct. You guessed the number in {counter} attempts.")
#             break
#         elif user_choice > comp_choice :
#             print("Lower number please!")
#         else :
#             print("Higher number please!")
# perfect_guess()

# ----------- CWH code --------------#
import random

n = random.randint(0, 100)
a = -1
guesses = 1

while (a != n):
    a = int(input("Enter a number from 0-100 : "))
    if (a > n) :
        print("Lower number please!")
        guesses += 1
    elif (a < n) :
        print("Higher number please!")
        guesses += 1
        
print(f"You've guessed the number {n} correctly in {guesses} attempts.")