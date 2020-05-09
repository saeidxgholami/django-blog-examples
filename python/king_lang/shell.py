import king

while True:
	text = input("King>> ")

	result, error = king.run(text)
	if error:
		print(error)
	else:
		print(result)