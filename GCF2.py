#return:returns the output back to the person.
#How to find GCF in general. Find factors of both and use the greatest common one. gcf cant exceed that of smaller number's gcf.

x=(input("pick a number:"))
y=(input("Pick another number:"))


def compare(x,y):
    smaller=0
    if x > y:
        smaller=y
    else:
        smaller=x

    gcf=1
    for i in range(1, smaller+1):
        if(x % i == 0) and (y % i ==0):
            gcf=i
         
number1=30
number2=10
print("gcf of" ,x, "and" ,y, "is",gcf)


