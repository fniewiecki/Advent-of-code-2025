import math


def read_data(file_name,array):
    file = open(file_name, 'r')
    for line in file:
        line = line.strip()
        array.append(line)


def day1b():
    path = "day1.txt"
    pathtest = "day1test.txt"
    rotationstest = []
    rotations = []
    read_data(pathtest,rotationstest)
    read_data(path,rotations)
    start_number = 50
    counter = 0

    for sequence in rotations:
        direction = sequence[0]
        number = int(sequence[1:])

        while (number > 0):
            if direction == "R":
                start_number+=1
            elif direction == "L":
                start_number-=1
            if abs(start_number) == 100:
                start_number = 0
            if start_number == 0:
                counter+=1
            number-=1

        print(" ")
    print(rotationstest)
    print(counter)
if __name__ == '__main__':
    day1b()

