# Movie Tickets
# get visitors ages and calculate ticket price for each and total price

total_price = 0

while True:
	age = int(input("Enter your age: "))
	if 0 < age < 3:
		print("Free for age under 3.")
	elif 3 <= age <= 12:
		print("10$ age 3..12")
		total_price += 10
	elif age > 12:
		print('15$ age over 12')
		total_price += 15

	else:
		print("Invalid age.")
		break

print(f'Total cost {total_price}$')
