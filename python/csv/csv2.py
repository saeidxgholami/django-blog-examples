import model
import matplotlib.pyplot as plt


people = model.read_csv_dict('bmi.csv')


normal = 0
overweight = 0
underweight = 0

for person in people:
	bmi_result = person.get('BMI Status')
	if bmi_result == 'Normal':
		normal += 1
	elif bmi_result == 'Underweight':
		underweight += 1
	else:
		overweight += 1



print(normal, underweight, overweight)

all_bmi = normal + overweight + underweight

print('Overweighted People BMI: ', round((100 / all_bmi) * overweight, 2), '%')
print('Normal People BMI: ', round((100 / all_bmi) * normal, 2), '%')
print('Underweight People BMI: ', round((100 / all_bmi) * underweight, 2), '%')


data = {
	'Normal': round((100 / all_bmi) * normal, 2),
	'Underweight': round((100 / all_bmi) * underweight, 2),
	'Overweighte': round((100 / all_bmi) * overweight, 2)
}

categories = list(data.keys())
precentages = list(data.values())

# print(categories, percentages)
fig, ax = plt.subplots()
ax.bar(categories, precentages)
plt.show()