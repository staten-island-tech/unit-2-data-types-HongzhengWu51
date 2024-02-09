bill=(input("Bill:"))
service=(input("How was the service?:"))

x="0%"
y="15%"
z="20%"
w="25%"



bill=60


if service=="Bad":
    tip=0
    print(f"Tip is {x}")
    
    
elif service=="Okay":
     print(f"Tip is {y}")
     tip=0.15
     
  
elif service=="Good":
     print(f"Tip is {z}")
     tip=0.20
     
elif service=="Great":
      print(f"Tip is {w}")
      tip=0.25
      
else:
     print("invalid")

total_bill=(bill*tip)+tip
print(total_bill)



