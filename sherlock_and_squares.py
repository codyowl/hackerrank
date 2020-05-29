def squares(a, b):
	'''
	Psst ! Logic ! 
	for getting range between a and b we can use range (a, b+1)
	to check if a number is square or not we can use the perfect square numbers last digit to validate
	x**.5 % 1 => x is a perfect square ! phew ! hastla vista babe !
	To get the last/single digit we can convert that to str and access the last index n[-1] 
	'''
	perfect_square_count = 0
	numbers_range_list = range(a, b + 1)
	for number in numbers_range_list:
		if number**.5 % 1 == 0:
			perfect_square_count += 1

	return perfect_square_count		

