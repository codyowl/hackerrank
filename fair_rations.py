def fairRations(B):
	loaf_increment = 0
    if sum(B) % 2 != 0:
        return "NO"
    for i in range(len(B)):
        if B[i] % 2 != 0:
            B[i+1] += 1
            loaf_increment += 2
    if B[-1] %2 != 0:
        return "NO"
    else:
        return loaf_increment            