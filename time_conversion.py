def timeConversion(s):
    hour, minute, second = s.split(":")
    if s== "12:00:00AM":
        return "00:00:00"
    if "PM" in second:
        if int(hour)!= 12:
            hour = str(int(hour) + 12)
            second = second[:-2]
        elif int(hour) == 12:
            second = second[:-2]
    if "AM" in second:
        if int(hour) == 12:
            hour = "00"
            second = second[:-2]        

    return "%s:%s:%s" % (hour, minute, second)               

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
