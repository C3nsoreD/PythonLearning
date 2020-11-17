def commad_parser(cmd, lst):
    if cmd[0] == 'insert':
        lst.insert(int(cmd[1]), int(cmd[2]))
    if cmd[0] == 'remove':
        lst.remove(int(cmd[1]))
    if cmd[0] == 'append':
        lst.append(int(cmd[1]))
    if cmd[0] == 'sort':
        lst.sort()
    if cmd[0] == 'pop':
        lst.pop()
    if cmd[0] == 'reverse':
        lst.reverse()
    if cmd[0] == 'print':
        print(lst)

class Commands:
    def __init__(self, _list):
        self.cmd = _list[0]
        self.i = int(_list[1])
        self.e = int(_list[2])
    
    def action(self):
        if self.cmd != "print":            
            eval("l.{0}({1}, {2})".format(self.cmd, self.i, self.e))

if __name__ == "__main__":
    with open('input00.txt','r') as f:
        input_lines = [line.strip() for line in f]
    n = int(input_lines[0])
    
    print([line for line in input_lines[1:]])
    
    for line in input_lines[1:]:
        cmd = Commands(line.split(' '))
        # cmd.action()