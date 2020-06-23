__author__ = "Gabriel Ugolole"


class StudentFileReader:
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None  # Input file set to None

    def open(self):
        self._inputFile = open(self._inputSrc, "r")  # Sets the file for reading

    def close(self):
        self._inputFile.close()
        self._inputFile = None  # Resets the inputFile to None

    def fetchAll(self):
        theRecords = list()  # empty list for keeping the records
        student = self.fetchRecord()
        while student is not None:
            theRecords.append(student)
            student = self.fetchRecord()
        return theRecords

    def fetchRecord(self):
        line = self._inputFile.readline()
        if line == "":
            return None

        # if ther is another record, create a storage object and fill it
        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = float(self._inputFile.readline())
        return student


# Storage class used for an individual student record
class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0
