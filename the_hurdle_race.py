# Complete the hurdleRace function below.
def hurdleRace(k, height):
    maximum_height = max(height)
    if maximum_height < k:
        return 0
    else:
        return abs(maximum_height-k)
