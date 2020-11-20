__author__ = "Gabriel Ugolole"

# Storage class used for an individual student record
class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0


class StudentFileReader:
    def __init__(self, file_path):
        self._input_source = file_path
        self._inputFile = None  

    def open(self, mode=None):
        # Default mode = 'r'
        if mode:
            self._inputFile = open(self._inputSrc, "r")  # Sets the file for reading
        else:
            self._inputFile = open(self._inputSrc, mode)

    def close(self):
        self._inputFile.close()
        self._inputFile = None  # Reset inputFile to None

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


