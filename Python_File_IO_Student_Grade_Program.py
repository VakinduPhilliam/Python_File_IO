# Python File IO.
# Python Student Grading.
# A student grades program that is uses file IO to keep a record of the students.

assignments = [‚hw ch 1‚, ‚hw ch 2‚, ‚quiz ‚, ‚hw ch 3‚, ‚test‚]
students = { }

# Function to read student data

def load_grades(gradesfile):

inputfile = open(gradesfile, "r")

grades = [ ]

while True:
student_and_grade = inputfile.readline()
student_and_grade = student_and_grade[:-1]

if not student_and_grade:
break

else:
studentname, studentgrades = student_and_grade.split(",")

studentgrades = studentgrades.split(" ")
students[studentname] = studentgrades

inputfile.close()

print "Grades loaded."

# Function to add new student data

def save_grades(gradesfile):

outputfile = open(gradesfile, "w")

for i in students.keys():
outputfile.write(i + ",")

for x in students[i]:

outputfile.write(x + " ")
outputfile.write("\n")

outputfile.close()

print "Grades saved."

# Function to Print Menu Choices

def print_menu():

print "1. Add student"
print "2. Remove student"
print "3. Load grades"
print "4. Record grade"
print "5. Print grades"
print "6. Save grades"
print "7. Print Menu"
print "9. Quit"

# Function to Print student grades

def print_all_grades():

keys = students.keys()

if keys:
keys.sort()
print ‚\t‚,

for i in range(len(assignments)):
print assignments[i], ‚\t‚,
print

for x in keys:
print x, ‚\t‚,
grades = students[x]
print_grades(grades)

else:
print "There are no grades to print."

# Function to capture menu choices

def print_grades(grades):

for i in range(len(grades)):

print grades[i], ‚\t‚,
print
print_menu()


menu_choice = 0
while menu_choice != 9:
print
menu_choice = input("Menu Choice: ")

if menu_choice == 1:
name = raw_input("Student to add: ")
students[name] = [0] * len(assignments)

elif menu_choice == 2:
name = raw_input("Student to remove: ")

if name in students:
del students[name]

else:
print "Student:", name, "not found"

elif menu_choice == 3:
gradesfile = raw_input("Load grades from which file? ")
load_grades(gradesfile)

elif menu_choice == 4:
print "Record Grade"
name = raw_input("Student: ")

if name in students:
grades = students[name]

print "Type in the number of the grade to record"
print "Type a 0 (zero) to exit"

for i in range(len(assignments)):

print i + 1, assignments[i], ‚\t‚,
print
print_grades(grades)
which = 1234

while which != -1:
which = input("Change which Grade: ")
which = which - 1

if 0 <= which < len(grades):
grade = raw_input("Grade: ") Change from
input() to raw_input() to avoid an error when saving
grades[which] = grade

elif which != -1:
print "Invalid Grade Number"

else:
print "Student not found"

elif menu_choice == 5:
print_all_grades()

elif menu_choice == 6:
gradesfile = raw_input("Save grades to which file? ")
save_grades(gradesfile)

elif menu_choice != 9:
print_menu()
