from itertools import cycle

fl = open("frequency_changes.txt")

def sum_list(frequency_changes):
	base_frequency = 0
	for i in frequency_changes:
		base_frequency = base_frequency+ int(i)
	print(base_frequency)

def freqeuncy_addition_repitition(frequency_changes):
	frequency_array=[]
	curr_frequency = 0
	cycled_changes = cycle(frequency_changes)
	for i in cycled_changes:
		curr_frequency= curr_frequency+ int(i)
		if curr_frequency in frequency_array:
			break
		frequency_array.append(curr_frequency)
	print (curr_frequency)
	print (frequency_array)



freqeuncy_addition_repitition(fl)
sum_list(fl)
