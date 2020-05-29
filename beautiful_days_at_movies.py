def beautifulDays(i, j, k):
	# getting days between range i and j
	days_list = [days for days in range(i,j+1)]
	beautiful_days_count = 0
	"""
	psst ! Logic:
	For reversing a number we can use int(str(n)[::-1])
	for checking if the number is whole number we can use n % 1 == 0
	"""
	for day in days_list:
		if (day - int(str(day)[::-1]))/k % 1 == 0:
			beautiful_days_count += 1
	return beautiful_days_count
	
print (beautifulDays(13,45,3))
# print (beautifulDays(20,23,6))			 
