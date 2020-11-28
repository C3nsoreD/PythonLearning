from ds import Array2D

# Open the text file for reading.
gradeFile = open( "tests/2dtest.txt", "r" )
# Extract the first two values which indicate the size of the array.
values = gradeFile.readline().strip().split()
# print(values)
numStudents = int( values[0] )
numExams = int( values[1])
# Create the 2-D array to store the grades.
examGrades = Array2D( numStudents, numExams )
# Extract the grades from the remaining lines.
i = 0
for student in gradeFile :
    grades = student.split()
    for j in range(numExams):  # 0-3
        print(i, j)
        examGrades[i, j] = int( grades[j] )
    i += 1
# Close the text file.
gradeFile.close()