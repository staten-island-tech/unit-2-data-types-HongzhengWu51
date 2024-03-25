name = (input("type your name: "))
student_class= (input("type your class: "))
grades = (input("type in your grades (separated by spaces): ")).split()
grades = [int(grade) for grade in grades]


student = {
    'name' : name,
    'class' : student_class,
    'grades': grades,
}

def get_average(grades):
    total = sum(grades)
    average = total / len(grades)
    print(average)

get_average(student['grades'])

