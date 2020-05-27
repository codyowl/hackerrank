def bonAppetit(bill, k, b):
	# accessing the kth index of bill
	anna_declines = bill.pop(k)
	# adding rest of the items in bill
	sum_of_bill = sum(bill)
	half_sum_bill = int(sum_of_bill/2)
	import pdb; pdb.set_trace()
	if half_sum_bill == b:
		print ("Bon Appetit")
	else:
		print (int(abs(sum_of_bill-b)))

bill = [3,10,2,9]
k = 1
b = 12
bonAppetit(bill, k, b)