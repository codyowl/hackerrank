def cutTheSticks(arr):
	sticks_cut = []
	while len(arr) != 0:
		sticks_cut.append(len(arr))
		length_of_cut = min(arr)
		for i in range(len(arr)):
			arr[i] = arr[i] - length_of_cut
		arr = list(filter(lambda a: a != 0, arr))
	return sticks_cut	



arr = [5,4,4,2,2,8]
print (cutTheSticks(arr))	