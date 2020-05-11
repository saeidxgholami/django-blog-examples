import mycsv
import calc

import matplotlib.pyplot as plt



def create_bmi(src_file, res_file):
	people = mycsv.read_dict(src_file)
	data = []
	for person in people:
		name = person.get('Name')
		height = calc.meter(int(person.get('Height (in)')))
		weight = calc.kg(int(person.get('Weight (lbs)')))
		bmi = calc.bmi(height, weight)
		bmi_status = calc.bmi_status(bmi)

		data.append([name, height, weight, bmi, bmi_status])
	header = ["Name", "Height(M)", "Weight(KG)", "BMI", "BMI_Status"]
	data.insert(0, header)
	mycsv.write(res_file, data)

def draw_chart(x, y):
	fig, axs = plt.subplots()
	axs.bar(x, y)
	plt.show()


def main():
	# create_bmi('biostats.csv', 'bmi1.csv')
	data = mycsv.read_dict('bmi.csv')
	# total_records = len(data)

	bmi_status_list = []
	for record in data:
		bmi_status_list.append(record.get('BMI_Status'))


	bmi_status = set(bmi_status_list)	
	bmi_status_num = dict(zip(bmi_status, len(bmi_status)*[0]))

	# for bmi in bmi_status:
	# 	bmi_status_num[bmi] = 0


	for bmi in bmi_status_num:
		bmi_status_num[bmi] = calc.count(bmi, bmi_status_list)

	total_bmi = sum(bmi_status_num.values())
	bmi_status_pr = {}
	for bmi_name, bmi_val in bmi_status_num.items():
		# print(bmi_name, bmi_val, total_bmi)
		bmi_status_pr[bmi_name] = round((100 / total_bmi) * bmi_val)

	x = list(bmi_status_pr.keys()) 
	y = list(bmi_status_pr.values())




	print(x, y)


	
	draw_chart(x, y)


if __name__ == '__main__':
	main()