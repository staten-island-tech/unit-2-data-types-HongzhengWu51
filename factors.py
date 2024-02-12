#First we need to make a function that allows and input.
#for i in range creates a loop. Here it tells the range from 1 to x+1. But it's exclusive so it excluedes one.
#This makes it from 1 to x.
#The % symbol is used for finding the remainder in division.
#The code means that if the remainder is zero then print that number.



number=int(input("Pick a number:"))
def factor(x):
    for i in range(1,x+1):
        if x % (i)==0:
            print(i)
factor(number)