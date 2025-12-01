
def day1():
    path = "day1.txt"
    start_number = 50
    rotations = []
    counter = 0
    rotations_test = ['R11','L911','L47']
    f = open(path,"r")
    for line in f:
        rotation = line.strip()
        rotations.append(rotation)
    for rotation in rotations:
        number = int(rotation[1:])
        if rotation[0] == "R":
            start_number += number
        elif rotation[0] == "L":
            start_number -= number
        start_number %= 100


        print(start_number)
        if start_number == 0:
            counter += 1
    print("Counter: ",counter)


if __name__ == '__main__':
    day1()

