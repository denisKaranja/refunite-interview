#!/usr/bin/python3
import csv, collections

def fibonacci(num):
	x = 0
	y = 1
	z = 1
	for a in range(1, num+1):
		x = y
		y = z
		z = x + y

	return x


'''
Calculates the largest average age
@params list of tuples [(town_code, gender, age)+]
@return tuple - > (max_avg_age, town_code)
'''
def get_max_avg(town_input):
	males, females = [], []
	assert type(town_input) is list

	for values in town_input:
		if values[1] == "1-Male":
			#append male ages only
			males.append(int(values[2]))
		elif values[1] == "2-Female":
			#append female ages only
			females.append(int(values[2]))

	#get average for both male and female
	total_females = len(females)
	total_males = len(males)

	if total_females > 0:
		avg_female = sum(females) / total_females
	elif total_females <= 0:
		avg_female = 0

	if total_males > 0:
		avg_male = sum(males) / total_males
	elif total_males <= 0:
		avg_male = 0

	max_age = max(avg_female, avg_male)

	return (max_age, values[0])


def main(filename):
	towns, values, sorted_freq, avg_values, town_freq = [], [], [], [], []

	with open(filename) as data:
		reader = csv.reader(data)

		for stuff in reader:
			town_code = stuff[2]
			gender = stuff[6]
			age = stuff[7]

			values.append((town_code, gender, age))
			towns.append(town_code)


	sorted_values = sorted(values)
	sorted_towns = sorted(towns)
	#print(sorted_values[38:59])

	#get frequency per town
	frequency = collections.Counter(towns)
	#print(frequency)
	#print(frequency)

	#sort the dictionary
	x = 0
	y = 1
	#print(len(frequency), frequency)
	[town_freq.append(frequency[key])  for key in sorted(frequency)]

	town_freq = town_freq[:len(town_freq) - 1]

	for value in town_freq:
		town_values = sorted_values[x: (value + x)]
		#print(town_values)
		avg_values.append(get_max_avg(town_values))
		x += value
	
	avg_age, t_code = max(avg_values)
	
	return t_code + str(int(avg_age))


if __name__ == "__main__":
	#print(fibonacci(10000))
	print(main("ebola_data_public.csv"))
