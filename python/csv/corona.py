import model



def get_data():
	data = model.read_csv_dict('covid19.csv')
	return data


def count(data):
	counter = {}
	for item in data:
		country = item.get('Country/Region')
		counter[country] = 0

	for item in data:
		country = item.get('Country/Region')
		if country in counter:
			counter[country] += float(item.get('Confirmed'))

	print(counter.get('Iran'))

def main():
	# Confirmed,Deaths,Recovered
	i = 0
	data = get_data()
	data_list = []

	for item in data:
		observation_date = item.get('ObservationDate')
		country = item.get('Country/Region')
		confirmed = item.get('Confirmed')
		deaths = item.get('Deaths')
		recovered = item.get('Recovered')
		# d.append([observation_date, country, confirmed, deaths, recovered])
		data_dict = {
			'ObservationDate': observation_date,
			'Country/Region': country,
			'Confirmed': confirmed,
			'Deaths': deaths,
			'Recovered': recovered

		}
		data_list.append(data_dict)

		if i == 100:
			break
		i += 1

	count(data)
	# for item in d:
	# 	print('{}  {}  {}  {}  {}'.format(*item))

if __name__ == '__main__':
	main()


