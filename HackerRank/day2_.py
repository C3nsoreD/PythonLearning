import re 

experssion = re.compile(r'[456](\d{1,3})^ -?')
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
)
    # r"[456]"
    # r"\d{3}"
    # r"(?:-?\d{4}){3}"
    # r"$")
Test = re.compile(
    r'(?!.*(\d)(-?\1){4})')

with open("input1.txt", 'r') as f:
    # line.strip() removes any whitespace charater
    _lines = [line.strip() for line in f]
# take the first line as n
n = int(_lines[0])
# confirm the output
print([line for line in _lines[1:]])

if __name__ == "__main__":
    # test the solution
    print()
    for s in _lines[1:]:
        if Test.search(s):
            print(s)
        else:
            print("invalid", s)    
    # exp = re.compile(r'a[bcd]*b')
    # print(exp.search('abcbd'))