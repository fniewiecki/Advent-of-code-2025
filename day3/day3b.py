from day3a import read_data

def day3b():
    joltage = []
    joltagetest = []
    path = "day3.txt"
    pathtest = "day3test.txt"
    read_data(path, joltage)
    read_data(pathtest, joltagetest)
    answer = [0,0,0,0,0,0,0,0,0,0,0,0]
    print(joltagetest)
    wholesum = 0
    for line in joltage:
        i = 0
        positionslefttofill = 11
        positionleft = 0
        while i < len(answer):
            positionright = len(line) - positionslefttofill
            for j in range(positionleft, positionright):
                if int(line[j]) > answer[i]:
                    answer[i] = int(line[j])
                    positionleft = j + 1
            positionslefttofill -= 1
            i += 1
        number = ""
        for x in answer:
            number += str(x)
        wholesum += int(number)
        answer = [0,0,0,0,0,0,0,0,0,0,0,0]
    print(wholesum)
if __name__ == '__main__':
    day3b()
