from random import random

from day3.day3a import read_data

def strip_data(array,elementsarray):
    for i in array:
        arr = []
        for j in i:
            arr.append(j)
        elementsarray.append(arr)


def day4b():
    rolls = []
    rollstest = []
    singlerolls = []
    singlerollstest = []
    tabforx = []


    changes = True
    path = "day4.txt"
    pathtest = "day4test.txt"
    countPaperAll = 0
    read_data(path, rolls)
    read_data(pathtest, rollstest)

    strip_data(rolls,singlerolls)
    strip_data(rollstest,singlerollstest)
    strip_data(rolls, tabforx)

    rowsmax = len(singlerolls) - 1
    columnmax = len(singlerolls[0]) - 1

    def isthispaperroll(i, j):
        if singlerolls[i][j] == '@':
            return 1
        else:
            return 0

    countPaper = 0
    while changes:
        for i in range(len(singlerolls)):
            for j in range(len(singlerolls[0])):
                if singlerolls[i][j] != '@':
                    continue
                counter = 0
                # górna krawędź
                if i == 0:
                    if j == 0 or j == rowsmax:
                        countPaper += 1
                        tabforx[i][j] = "X"
                        continue
                    else:
                        for x in [0, 1]:
                            for y in [-1, 0, 1]:
                                if x == 0 and y == 0:
                                    continue
                                counter += isthispaperroll(i + x, j + y)

                # dolna krawędź
                elif i == rowsmax:
                    if j == 0 or j == rowsmax:
                        countPaper += 1
                        tabforx[i][j] = "X"
                        continue
                    else:

                        for x in [-1, 0]:
                            for y in [-1, 0, 1]:
                                if x == 0 and y == 0:
                                    continue
                                counter += isthispaperroll(i + x, j + y)

                # lewa krawędź
                elif rowsmax > i > 0 == j:

                    for x in [-1, 0, 1]:
                        for y in [0, 1]:
                            if x == 0 and y == 0:
                                continue
                            counter += isthispaperroll(i + x, j + y)

                # prawa krawędź
                elif rowsmax > i > 0 and j == columnmax:

                    for x in [-1, 0, 1]:
                        for y in [-1, 0]:
                            if x == 0 and y == 0:
                                continue
                            counter += isthispaperroll(i + x, j + y)

                # środek
                elif 0 < i < rowsmax and 0 < j < columnmax:

                    for x in [-1, 0, 1]:
                        for y in [-1, 0, 1]:
                            if x == 0 and y == 0:
                                continue
                            counter += isthispaperroll(i + x, j + y)
                if counter < 4:
                    countPaper += 1
                    tabforx[i][j] = "X"
        for i in range(len(singlerolls)):
            for j in range(len(singlerolls[0])):
                singlerolls[i][j] = tabforx[i][j]
        if countPaper == 0:
            changes = False
            break
        countPaperAll += countPaper
        countPaper = 0
    print(countPaperAll)



if __name__ == '__main__':
    day4b()