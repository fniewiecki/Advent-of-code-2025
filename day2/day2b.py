from day2a import read_data

def find_patern(number):
    isvalid = True
    i = 2
    while i <= len(number):
        if len(number) % i == 0:
            index = len(number) // i
            part = number[:index]
            copy = part*i
            if copy == number:
                isvalid = False
        i += 1
    return isvalid

def day2b():
    ids = []
    idtest = []
    path = "day2.txt"
    pathtest = "day2test.txt"
    read_data(path, ids)
    read_data(pathtest, idtest)
    idsum2 = 0
    for rangestr in ids:
        start, end = rangestr.split('-')
        startnum = int(start)
        endnum = int(end)
        for number in range(startnum, endnum + 1):
            numberstr = str(number)
            if not find_patern(numberstr):
                idsum2 +=number
    print(idsum2)
if __name__ == '__main__':
    day2b()

