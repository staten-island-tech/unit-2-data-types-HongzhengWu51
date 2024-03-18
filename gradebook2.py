continue_adding_students = 'Y'
students = []


def get_average(data):
    total = sum(data)
    average = total / len(data)
    return average


def create_student(name, student_class, grades):

    new_student = {
        'name' : name,
        'class' : student_class,
        'grades': grades,
        'average': get_average(grades)
    }

    return new_student


def get_class_average(student_list):
    average_list = []
    for student in student_list:
        average = student['average']
        average_list.append(average)

    total = sum(average_list)
    class_average = total / len(average_list)
    return class_average


while continue_adding_students == 'Y':
    name = (input("type new student name: "))
    student_class= (input("type new student class: "))
    grades = (input("type new student grades (separated by spaces): ")).split()
    grades = [int(grade) for grade in grades]

    new_student_info = create_student(name, student_class, grades)
    students.append(new_student_info)

    for student in students:
        print(student)

        
    ask = input('Do you want to continue adding more students (Y/N)? ')
    if ask == 'Y':
        continue
    elif ask == 'N':
        break
    else:
        print('Invalid response')


print('Class average: ', get_class_average(students))
