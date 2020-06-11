import itertools

def getMoneySpent(keyboards, drives, b):
	'''
	psst Logic ! we need to get all the combinations of keyboards and drives and find the closes number of b
	to get all the combinations 
	we can use itertools.product()
	min(combinations,key=lambda x:abs(x-b))
	'''
	if len(keyboards) and len(drives) == 1:
		if keyboards[0] + drives[0] > b:
			return -1
	else:		
		combinations = list(itertools.product(keyboards, drives))
		# sum of all the combinations
		combinations = [sum(data) for data in combinations] 
		# getting the closes number from combinations 
		closest_number = min([ number for number in combinations if number < b], key=lambda x:abs(x-b)) 
		# closes_number = min(combinations,key=lambda x:abs(x-b))   
		return closest_number


keyboards = [3,1]
drives = [5,2,8]

print (getMoneySpent(keyboards, drives, 10))