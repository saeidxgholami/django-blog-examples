def bmi(height, weight):
	return round(weight / height ** 2, 2)


def meter(inch):
	return round(inch / 39.37, 2)


def kg(pound):
	return round(pound / 2.205, 2)


def bmi_status(bmi):
	if bmi <= 18.5:
		return 'Underweight'
	elif bmi > 18.5 and bmi < 24.9:
		return 'Normal'
	else:
		return 'Overweight'


def count(n, seq):
	""" Count how may n is in seq """
	return seq.count(n)




if __name__ == '__main__':
	print("Testing area ....")
	x = count(5, [1, 2, 3, 5, 6, 5, 6, 4, 5, 5])
	print(x)
