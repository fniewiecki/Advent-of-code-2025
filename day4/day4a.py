from day3.day3a import read_data

def day4a():
    rolls = []
    rollstest = []
    path = "day4.txt"
    pathtest = "day4test.txt"
    read_data(path, rolls)
    read_data(pathtest, rollstest)
    rowsmax = len(rolls) - 1
    columnmax = len(rolls[0]) - 1
    countPaper = 0

    def isthispaperroll(i, j):
        if rolls[i][j] == '@':
            return 1
        else:
            return 0

    for i in range(len(rolls)):
        for j in range(columnmax + 1):
            if rolls[i][j] != '@':
                continue

            counter = 0
            #górna krawędź
            if i == 0:
                if j == 0 or j == rowsmax:
                    countPaper += 1
                    continue
                else:
                    for x in [0,1]:
                        for y in [-1,0,1]:
                            if x == 0 and y == 0:
                                continue
                            counter += isthispaperroll(i+x, j+y)

            #dolna krawędź
            elif i == rowsmax:
                if j == 0 or j == rowsmax:
                    countPaper += 1
                    continue
                else:

                    for x in [-1,0]:
                        for y in [-1,0,1]:
                            if x == 0 and y == 0:
                                continue
                            counter += isthispaperroll(i+x, j+y)

            #lewa krawędź
            elif rowsmax > i > 0 == j:

                for x in [-1,0,1]:
                    for y in [0,1]:
                        if x == 0 and y == 0:
                            continue
                        counter += isthispaperroll(i + x, j + y)

            #prawa krawędź
            elif rowsmax > i > 0 and j == columnmax:

                for x in [-1,0,1]:
                    for y in [-1,0]:
                        if x == 0 and y == 0:
                            continue
                        counter += isthispaperroll(i + x, j + y)

            #środek
            elif 0 < i < rowsmax  and 0 < j < columnmax :

                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if x == 0 and y == 0:
                            continue
                        counter += isthispaperroll(i+x,j+y)
            if counter < 4:
                countPaper += 1

    print(countPaper)

if __name__ == '__main__':
    day4a()