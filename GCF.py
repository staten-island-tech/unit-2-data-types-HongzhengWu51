x=int(input("Pick a number:"))
y=int(input("Pick another number:"))

def factor1(x):
    for i in range(1,x+1):
        if x % (i)==0:
            print(i)
factor1(x)
factor1=[]

def factor2(y):
    for i in range(1,y+1):
        if y % (i)==0:
            print(i)
factor2(y)
factor2=[]

print(factor1[-1])