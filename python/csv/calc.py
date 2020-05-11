def get_meter(inch):
	try:
		return round(float(inch) / 39.37, 2)
	except ValueError:
		return "Cannot convert to int."

def get_kg(pound):
	try:
		return int(pound) // 2.205
	except ValueError:
		return "Cannot convert to int."


def get_bmi(height, weight):
	bmi = weight / height ** 2
	bmi = round(bmi, 1)
	return bmi
	
	if bmi <= 18.5:
		return -1
	elif bmi >= 18.5 and bmi <= 24.9:
		return 0
	else:
		return 1


def get_bmi_status(bmi):
	stat = None
	if bmi <= 18.5:
		stat = 'Underweight'
	elif bmi >= 18.5 and bmi <= 24.9:
		stat = 'Normal'
	else: 
		stat = 'Overweighte'

	return stat

if __name__ == '__main__':
	h = 74.80
	w = 250.3
	hh = get_meter(h)
	ww = get_kg(w)
	print(hh, ww)
	bmi_result = get_bmi(hh, ww)
	if bmi_result == 0: print('Normal')
	elif bmi_result == -1: print('Underweight')
	else: print('Overweighted.')
