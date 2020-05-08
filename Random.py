import random

def print2DArray(randomBoard = [], *args):
    for x in range(10):
        for y in range(10):
            print(randomBoard[x][y], end=" ")
        print("")
        
def findSum(randomBoard = [], *args):
    totalSum = 0
    for x in range(10):
        for y in range(10):
            totalSum = totalSum + randomBoard[x][y]
    print(totalSum)

randomArray = [[0 for i in range(10)] for i in range(10)]
for x in range(10):
    for y in range(10):
        randomArray[x][y] = random.randint(0, 9);
print2DArray(randomArray)
findSum(randomArray)
