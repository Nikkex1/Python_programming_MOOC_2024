# tee ratkaisu tänne
if True: #if True: always executed; if False: never executed
    student_info = input("Student information:")
    exercise_data = input("Exercised completed:")
    exam_data = input("Exam points:")
    course_info = input("Course information:")
else: #hard coded input for testing
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    course_info = "course1.txt"

name_dictionary = {}
with open(student_info) as student_file:
    for line in student_file:
        #line = line.replace("\n", "") #strip() is more efficient
        line = line.strip() #strip removes everything unnecessary
        parts = line.split(";")
        if parts[0] == "id":
            continue
        name_dictionary[parts[0]] = [f"{parts[1]} {parts[2]}"]

exercises_completed = {}
exercise_points = {}
with open(exercise_data) as exercise_file:
    for line in exercise_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        help_sum = 0
        for number in parts[1:]:
            help_sum += int(number)
        exercises_completed[parts[0]] = help_sum
        exercise_points[parts[0]] = int(help_sum / 40 * 10)

exam_dictionary = {}
with open(exam_data) as exam_file:
    for line in exam_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        help_sum = 0
        for number in parts[1:]:
            help_sum += int(number)
        exam_dictionary[parts[0]] = help_sum

total = {}
for key, value in exercise_points.items():
    if key in exam_dictionary:
        total[key] = value + exam_dictionary[key]

grade = {}
for key, value in name_dictionary.items():
    if key in total:
        if total[key] in range(0,15):
            grade[key] = 0
        elif total[key] in range(15,18):
            grade[key] = 1
        elif total[key] in range(18,21):
            grade[key] = 2
        elif total[key] in range(21,24):
            grade[key] = 3
        elif total[key] in range(24,28):
            grade[key] = 4
        elif total[key] >= 28:
            grade[key] = 5

course = []
with open(course_info) as course_file:
    for line in course_file:
        line = line.strip()
        parts = line.split(": ")
        course.append(parts[1])

with open("results.txt", "w") as result_table:
    result_table.write(f"{course[0]}, {course[1]} credits\n{"="*38}\n")
    result_table.write(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade"}\n")
    for key, value in name_dictionary.items():
        result_table.write(f"{value[0]:30}{exercises_completed[key]:<10}{exercise_points[key]:<10}{exam_dictionary[key]:<10}{total[key]:<10}{grade[key]:<10}\n")

with open("results.csv", "w") as result_file:
    for key, value in name_dictionary.items():
        result_file.write(f"{key};{value[0]};{grade[key]}\n")