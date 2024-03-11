#int(i) for i in x. x resents each of the lists in accounts. i is each num

accounts= [["1","2","3"], ["5","6","7"] ]
y= [[int(i) for i in x] for x in accounts]
print(sum(y[0]))
print(sum(y[1]))

both = y.append 

