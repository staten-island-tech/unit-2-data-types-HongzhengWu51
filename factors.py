#First we need to make a function that allows and input. The word input in () allows person to put an input.
#for i in range creates a loop. Here it tells the range from 1 to x+1. But it's exclusive so it excluedes one.
#This makes it from 1 to x.
#The % symbol is used for finding the remainder in division.
#The code means that if x divided by i creates zero then it means that it is a factor. So we print i.
#I also don't really understand so I don't know. 



number=int(input("Pick a number:"))
def factor(x):
    for i in range(1,x+1):
        if x % (i)== 0:
            print(i)
factor(number)