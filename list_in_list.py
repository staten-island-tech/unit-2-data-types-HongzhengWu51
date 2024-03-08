#int(i) for i in x. x resents each of the lists in accounts. i is each num

accounts= [["1","2","3"], ["5","6","7"] ]
y= [[int(i) for i in x] for x in accounts]
print(sum(y[0]))

if (sum(y[0])) > (sum(y[1])):
    print(sum(y[0]))
elif (sum(y[1])) > (sum(y[1])):
    print(sum(y[1]))
elif (sum(y[0])) == (sum(y[1])):
    print(sum(y[0]))
else:
    print("invalid")