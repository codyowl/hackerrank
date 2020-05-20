'''  
It must return YES if class is cancelled, or NO otherwise. 
k = threshold
a = number of students => (>=1 is considered as late)
'''

def angryProfessor(k, a):
    late_comer_count = 0
    for time in a:
        if time > 0:
            late_comer_count += 1
    if late_comer_count == k or late_comer_count > k:
        return "NO"
    else:
        return "YES"        


#k = 4
#a = [-93, -86, 49, -62, -90, -63, 40, 72, 11, 67]

# k = 10
# a = [23, -35, -2, 58, -67, -56, -42, -73, -19, 37]
# print (angryProfessor(k, a))        