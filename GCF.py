x=int(input("Pick a number:"))
y=int(input("Pick another number:"))

def factor_both(x):
    for i in range(1,x+1):
        if x % (i)==0:
            print(i)
factor_both(x)
factor_both=[]

def factor2(y):
    for i in range(1,y+1):
        if y % (i)==0:
            print(i)
factor2(y)
factor2=[]








