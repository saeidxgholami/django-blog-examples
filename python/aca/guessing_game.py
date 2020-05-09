# Create random number
# Get a guess from user
# check if the guess < rand_guess : "Guess High"
# check if the guess > rand_guess : "Guess Low"
# check if the guess == rand_guess : "Correct."

import random


# the random number
rand_num = random.randint(1, 100)
print(rand_num)

user_guess = int(input("Enter a guess: "))

for i in range(10):
	if user_guess < rand_num:
		print("Guess High")
	elif user_guess == rand_num:
		print("Correct")
	else:
		print("Guess Low")