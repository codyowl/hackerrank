def repeatedString(s, n):
	# when one 'a' is given
	if len(s) == 1:
		return n
	else:
		remaining_len = n - len(s)
		if remaining == len(s):
			s += s
			a_dict = {}
			for letter in s:
				a_dict[letter] = [index for index, element in enumerate(s) if element == letter]	
			return len(a_dict['a'])
