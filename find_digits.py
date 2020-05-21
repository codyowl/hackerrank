def findDigits(n):
	# getting each digits of number
	number_list = list(str(n))
	divisible_count = 0
	for digit in number_list:
		if int(digit) != 0:
			if n % int(digit) == 0:
				divisible_count += 1
	return divisible_count		


# n = 12
# print (findDigits(n))
n = 1012
print (findDigits(n))
