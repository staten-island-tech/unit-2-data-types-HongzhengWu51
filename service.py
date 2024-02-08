bill=(input("Bill:"))
service=(input("How was the service?:"))

x="0%"
y="15%"
z="20%"
w="25%"


tip=0*bill
tip1=0.15*bill
tip2=0.20*bill
tip3=0.25*bill


total=0*bill+bill
total1=0.15*bill+bill
total2=0.20*bill+bill
total3=0.25*bill+bill


if service=="Bad":
    print(f"Tip is {x}")
    print(tip)
    print(total)
elif service=="Okay":
    print(f"Tip is {y}")
    print(tip1)
    print(total1)
elif service=="Good":
    print(f"Tip is {z}")
    print(tip2)
    print(total2)

elif service=="Great":
    print(f"Tip is {w}")
    print(tip3)
    print(total3)
   



