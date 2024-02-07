bill=(input("Bill:"))
service=(input("How was the service?:"))
if service=="Bad":
    tip=0
elif service=="Okay":
    tip=15
elif service=="Good":
    tip=20
elif service=="Great":
    print('25%')
