
from DataStructures.StudentFileReader.studentfile import StudentFileReader

FILE_NAME = 'students.txt'

def main():
    reader = StudentFileReader(FILE_NAME)
    reader.open()
    student_list  = reader.fetchAll()
    reader.close()
    student_list.sort(key = lambda rec: rec.idNum)
    printReport(student_list)


def printReport(theList):
    print(theList)

