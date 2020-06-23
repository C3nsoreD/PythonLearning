
import studentfile

FILE_NAME = 'students.txt'


def main():

    reader = SttudentFileREader(FILE_NAME)
    reader.open()
    student_list  = reader.fetchAll()
    reader.close()


    student_list.sort(key = lambda rec: rec.idNum)

    printReport(student_list)


def printReport(theList):
    print(theList)
