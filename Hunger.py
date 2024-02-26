H = int(input("Hunger:"))
A = int(input("Apples:"))
s = int(input("seconds:"))

hunger1 = min(H,A)
remaining_hunger = hunger1 - s
print(remaining_hunger)
