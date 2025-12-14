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
    print(joltagetest)
    for line in joltagetest:
        firstNum = 0
        numbers = sorted(set(line))
        print(numbers)
        i = len(numbers)-1
        print(numbers[i])
        position = 0
        for j in range(0,len(line) - 2):
            if numbers[i] == line[j]:
                position = j
                firstNum = numbers[i]
                break
            i -= 1
        secondNum = 0
        for x in range(position,len(line)-1):
            if int(line[x]) > secondNum:
                secondNum = int(line[x])
        print(firstNum, secondNum)



if __name__ == '__main__':
    day3a()
