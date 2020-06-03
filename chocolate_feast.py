def chocolateFeast(n, c, m):
	'''
	Psst ! Logic :
	choclates = n/c
	choclate_count = choclates
	now we have to find how many wrappers we can get from choclates
	wrappers = choclate_count /  m
	choclates += wrappers
	choclate_count = wrapper + (choclate_count % m) 
	Ffinding the remining choclate 
	'''

    choclate = int(n / c)
    choclate_count = choclate
    
    while choclate_count >= m:
        wrappers = int(choclate_count / m)
        choclate += wrappers
        choclate_count = wrappers + (choclate_count % m) # finding the left over from choclate 

    return choclate
	
				
			
		
print (chocolateFeast(15, 3, 2))

