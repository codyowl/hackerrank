def libraryFine(d1, m1, y1, d2, m2, y2):
	'''
	psst ! logic
	d1, m1, y1 are returned date, month and year
	if y1 > y2 : then its a 10,000 Hackos fine
	if the returned year is equal and month is greater than no of delayed months * 500
	if the returned year is equal and month is also equal and date is delayed then no of delated date * 15
	
	'''
	fine = 0
	if y1 == y2:
		if m1 == m2:
			if d1 > d2:
				fine = 15 * abs(d1-d2)
		elif m1 > m2:
			fine = 500 * abs(m1-m2)
	elif y1 > y2:
		fine = 10000
	return fine
# print (libraryFine(9, 6 ,2015,6, 6, 2015))
print (libraryFine(2,7,1014,1,1,1014))