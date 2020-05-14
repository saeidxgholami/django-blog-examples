
questions = {
	'1': "Which mountain located in Ardabil city?",
	'2': "Which one is the national language in Iran?",
	'3': "Which one is Iran Capital?",
}

choices = {
	'1': ['Sahand', 'Damavand', 'Sabalan', 'Zagros'],
	'2': ['Arabic', 'Persian', 'Turkish', 'Ordu'],
	'3': ['Tehran', 'Baku', 'Baghdad', 'Donshabe'],
}

answers = {
	'1': '3',
	'2': '2',
	'3': '1',
}

correct = 0
flag = True

for q_index, question in questions.items():
	print(question)
	for opt_num, option in enumerate(choices[q_index], 1):
		print(f'{opt_num}. {option}')

	ans = input("You answer: ")

	if ans == answers.get(q_index):
		correct += 1


print(correct)