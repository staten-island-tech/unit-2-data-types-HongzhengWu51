H = int(input("Hunger:"))
A = int(input("Apples:"))
s = int(input("seconds:"))

hunger1 = min(H,A)
remaining_hunger = hunger1 - s
if remaining_hunger < 0:
    remaining_hunger = 0
print(remaining_hunger)
