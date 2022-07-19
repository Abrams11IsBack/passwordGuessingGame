import random

#alright kids so this code is an expandable passcode cracker and the code looks cool and all, my friend that kind of tries to get into programming-
#...-wanted to do this and it was his idea (or some challange from the internet that I didn't know) so I decided to do it incase he doesn't finish it...
#and he didn't! of course... guys stick to projects if you wanna get into programming you need to code not just think about coding
#anyway I'm havin a good time and you should too (ignoring the current 2022 events) and inflation yeahhh it's great fantastic I'm well alive which is good
#the reason this github is dead is because most of my projects aren't "polished" enough, that applies to my old java projects, they kind of really stink
#also i forget to upload them simply or I am too lazy to do it cuz who wants to see a half working midi player am i right?
#omg i almost deleted the code with ctrl a and del
#the code is you know down there you can look there yeah
#seriously if you are reading this that's cool if anyone sees this thing
#subscribe star fork ring the bell like follow download watch or something

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
            print("\033[1;33;10m brawo bambusie zlamales kod") #ignore polish here it basically says that u got it yee(no need to translate)
            didWin = True
        else:
            print("\033[1;33;10m debil") #ignore it too just assume is says oops! you are wrong
    else:
        print("guess is not " + str(lenghtCode) + " numbers long")
