#return:returns the output back to the person.
def compare(x,y):
    if x > y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if(x % i == 0) and (y % i ==0):
            gcf=i
        return gcf
number1=6
number2=8
print("gcf is:", compare(number1,number2))