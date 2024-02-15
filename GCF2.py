#return: returns the output back to the person.
#How to find GCF in general. Find factors of both and use the greatest common one. gcf cant exceed that of smaller number's gcf.
#Return needs to be used in order to leave the function and calls the thing so that it can be used. 
#Return is useful when there are many functions using the same variable like x and it wouldn't work becuase it has different values.
#EX:         gcf = i, smaller, x
#         return gcf, a, b, c.        It would print it in that order.
# x = int(input("pick a number: "))
#y = int(input("Pick another number: "))
#It wouldn't work because it was a string and can't be converted to smaller+1 because it wasn't an integer.

x = int(input("pick a number: "))
y = int(input("Pick another number: "))


def find_gcf(x, y):
    smaller = 0
    if x > y:
        smaller = y
    else:
        smaller = x

    gcf = 1
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i ==0):
            gcf = i

    return gcf


result = find_gcf(x, y)
print("gcf of ", x, "and " , y, "is", result)

