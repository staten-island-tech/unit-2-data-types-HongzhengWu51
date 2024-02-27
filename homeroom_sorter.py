last_name = input("Last name: ")
first_initial = last_name[0]
homeroom = 103
if first_initial.lower() == "a":
    homeroom = 101
    print(f"Homeroom: {homeroom}")
elif first_initial in "bB":
    homeroom= 102
    print(f"Homeroom: {homeroom}")
else:
    print(f"Homeroom: {homeroom}")






