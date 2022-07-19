import random

# print("\033[1;32;10m Bright Green  \n")
# print("\033[1;31;10m Bright Red  \n")

lenghtCode = int(input("code length: "))

a = ""
didWin = False

for i in range(lenghtCode):
    b = random.randint(0, 9)
    a += str(b)
print(a)

passArr = list(a)
print(passArr)

while not didWin:
    userInput = input("guess: ")
    if len(userInput) == lenghtCode:
        userArr = list(userInput)
        #print(userArr)

        c = 0
        d = 0
        checkArr = []

        for i in passArr:
            if i == userArr[c]:
                #print(i)
                checkArr.append(i)
            else:
                checkArr.append(userArr[c])
            c += 1
        #print(checkArr)

        for i in passArr:
            if i == checkArr[d]:
                print("\033[1;32;10m" + checkArr[d], end="")
            else:
                print("\033[1;31;10m" + checkArr[d], end="")
            d += 1

        print("", end="\n")

        if passArr == checkArr:
            print("\033[1;33;10m brawo bambusie zlamales kod")
            didWin = True
        else:
            print("\033[1;33;10m debil")
    else:
        print("guess is not " + str(lenghtCode) + " numbers long")
