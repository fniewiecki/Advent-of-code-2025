from itertools import count


def read_data(path,array1,array2):
    f = open(path,'r')
    ranges = True
    for l in f.readlines():
        line = l.strip()
        if l == "\n":
            ranges = False
            continue
        if ranges:
            firstdigit = ""
            position = 0
            seconddigit = ""
            for char in line:
                position += 1
                if char == "-":
                    break
                firstdigit += char
            for char in range(position, len(line)):
                seconddigit += line[char]
            array1.append([int(firstdigit),int(seconddigit)])
        else:
            array2.append(int(line))

def day5a():
    indexes = []
    ingr = []
    count = 0
    read_data("input.txt",indexes,ingr)
    for i in ingr:
        for j in range(len(indexes)):
            if indexes[j][0] <= i <= indexes[j][1]:
                count+=1
                break
    print(count)
if __name__ == '__main__':
    day5a()
