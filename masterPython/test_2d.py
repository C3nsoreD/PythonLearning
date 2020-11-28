from ds import Array2D

# gradeFile = open("tests/2dtest.txt", "rb").readlines()
# gradeFile.readlines().split()


# use a context manager
with open("tests/2dtest.txt", "r") as gradeFile:
    val = gradeFile.readline().split() 
    numStudents = int(val[0])
    numE = int(val[1])
    
    # print(numE, numStudents)
    examGrades = Array2D(numStudents, numE)

    i = 0
    # print(gradeFile.read()[:])
    for student in gradeFile.readlines():
        # grades = student.split()
        # print(type(student))
        # print()
        for j in range(numE):
            print(student[j])
            # examGrades[i, j] = int(student[j])
            # examGrades[i, j] = int(j)
        # i += 1

# print
# for i in range(numStudents): # row
#     total = 0
#     for j in range(numE): # col
#         total += examGrades[i, j]
    
#     examAvg = total / numE
#     print(f"{i+1:2d} : {examAvg:6.2f}")