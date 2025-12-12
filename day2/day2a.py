
def read_data(path, array):
    f = open(path, 'r')
    for line in f.readlines():
        line = line.strip()
        for i in line.split(','):
            array.append(i)
def day2a():
    ids = []
    idtest = []
    path = "day2.txt"
    pathtest = "day2test.txt"
    read_data(path, ids)
    read_data(pathtest, idtest)
    idsum = 0
    for rangestr in ids:
        start,end = rangestr.split('-')
        startnum = int(start)
        endnum = int(end)
        for number in range(startnum,endnum+1):
            numberstr = str(number)
            if len(numberstr) % 2 == 0:
                part1 = numberstr[:len(numberstr)//2]
                part2 = numberstr[len(numberstr)//2:]
                if part1 == part2:
                    idsum += number
    print(idsum)
if __name__ == '__main__':
    day2a()



