name = (input("type your name:"))
student_class= (input("type your class:"))
grades = (input("type in your grades :")).split()
grades = [int(grade) for grade in grades]

student = {
    'name' : name,
    'class' : student_class,
    'grades': grades,
}
#Finds average. Len finds how many numbers there are.
def get_average(grades):
    total = sum(grades)
    average = total / len(grades)
    print(average)

get_average(student['grades'])

