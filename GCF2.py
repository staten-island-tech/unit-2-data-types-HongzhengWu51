#return:returns the output back to the person.
def compare(x,y):
    smaller=0
    if x > y:
        smaller=y
    else:
        smaller=x
    
    for i in range(1, smaller+1):
        if(x % i == 0) and (y % i ==0):
            print("gcf=(i)")
         
number1=30
number2=10
print("gcf is", compare(number1,number2))


