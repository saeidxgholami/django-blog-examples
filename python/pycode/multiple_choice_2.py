data = {
	'1': {
		"question": "Which mountain located in Ardabil city?",
		"options": ['Sahand', 'Damavand', 'Sabalan', 'Zagros'],
		"answer": '3',

	},
	'2': {
		"question": "Which one is the national language in Iran?",
		"options": ['Arabic', 'Persian', 'Turkish', 'Ordu'],
		"answer": '2',

	},
	'3': {
		"question": "Which one is Iran Capital?",
		"options": ['Tehran', 'Baku', 'Baghdad', 'Donshabe'],
		"answer": '1',

	},
}

correct = 0

for item in data.values():
	question = item.get("question")
	options = item.get("options")
	answer = item.get("answer")

	print(question)
	
	for num, option in enumerate(options, 1):
		print(f"{num}. {option}")

	user_ans = input("Your answer: ")

	if user_ans == answer:
		correct += 1

print(correct)


