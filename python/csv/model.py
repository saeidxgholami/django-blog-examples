import csv





def append_row(filename, row):
	with open(filename, 'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(row)


def read_csv(filename):
	with open(filename, 'r') as csv_file:
		reader = csv.reader(csv_file, skipinitialspace=True,)
		return list(reader)


def write_csv(filename, rows):
	with open(filename, 'w') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerows(rows)


def read_csv_dict(filename):
	with open(filename, 'r') as csv_file:
		reader = csv.DictReader(csv_file, skipinitialspace=True,)
		return list(reader)





if __name__ == '__main__':

	# persons = [
	# 	['Name', 'Age', 'Height', 'Weight', 'City'],
	# 	['John Doe', '30', '180', '80', 'NY'],
	# 	['Kate Smith', '30', '170', '90', 'CA'],
	# 	['Jack Ma', '45', '165', '60', 'MI']
	# ]
	# write_csv('people.csv', persons)
	person = ['Mary Jackson', '49', '150', '83', 'IN']
	append_row('people.csv', person)