import calc
import model




people = model.read_csv_dict('biostats.csv')
people_bmi = []

for person in people:
	name = person.get('Name')
	age = person.get('Age')
	height = person.get('Height (in)')
	weight = person.get('Weight (lbs)')

	# some converting and bmi calculation.
	h = calc.get_meter(height)
	w = calc.get_kg(weight)
	bmi = calc.get_bmi(h, w)
	bmi_status = calc.get_bmi_status(bmi)

	# print(name,h, w, bmi, bmi_status)
	people_bmi.append([name, age, bmi, bmi_status])

header = ['Name', 'Age', 'BMI', 'BMI Status']

people_bmi.insert(0, header)


# write to new csv
model.write_csv('bmi.csv', people_bmi)	