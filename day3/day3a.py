def read_data(path, array):
    f = open(path, 'r')
    for line in f.readlines():
        line = line.strip()
        array.append(line)

def day3a():
    joltage = []
    joltagetest = []
    path = "day3.txt"
    pathtest = "day3test.txt"
    read_data(path, joltage)
    read_data(pathtest, joltagetest)
    numbers = ['9','8','7','6','5','4','3','2','1']
    wholesum = 0
    for line in joltage:
        firstNum = 0
        position = 0
        secondNum = 0
        i = 0
        while i < len(numbers):
            for j in range(len(line)-1):
                if line[j] == numbers[i]:
                    firstNum = line[j]
                    position = j
                    break
            if firstNum != 0:
                break
            i += 1
        for x in range(position + 1, len(line)):
            if secondNum < int(line[x]):
                secondNum = int(line[x])
        wholesum += int(str(firstNum)+str(secondNum))

    print(wholesum)




if __name__ == '__main__':
    day3a()
