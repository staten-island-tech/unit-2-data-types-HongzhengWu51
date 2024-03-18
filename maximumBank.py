#int(i) for x in i. i resents each of the lists in accounts. x is each num
accounts = [['1','2','3'], ['3','2','1'], ["5","10"], ["12","16"]]
def maxMoney(accounts):
    int_accounts = [[int(x) for x in i] for i in accounts]
    largest = 0 
    for money in int_accounts:
        x = sum(money)
        if(x > largest):
            largest = x 
    print(largest)
maxMoney(accounts)