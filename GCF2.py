#return:returns the output back to the person.
def factor_both(x,y):
    smaller=0
    if x > y:
        smaller=y
    else:
        smaller=x
    gcf=0
    for i in range(1,smaller+1):
        if(x % i == 0) and (y % i ==0):
           gcf=i
        return gcf
         
number1=30
number2=10
print("gcf is", factor_both(number1,number2))


