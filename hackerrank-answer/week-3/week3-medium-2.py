class Editor(object):
    def __init__(self):
        self.string = ''

    def append(self, string):
        self.string += string 
        
    def delete(self, num):
        self.string = self.string[:-int(num)]
    
    def printe(self, num):
        print self.string[num-1]

    def __str__(self):
        return self.string
    
stack = []

e = Editor()

operations= []
lines = raw_input()
for i in range(int(lines)):
    operations.append(raw_input())
    
for op in operations:
    if op == '4':
        operation = op
    else:
        op = op.split()
        operation, value = op[0], op[1]
    
    if operation == '1':
        
        stack.append(e.string)
        e.append(value)
        
    elif operation == '2':
        stack.append(e.string)
        e.delete(value)
        
    elif operation == '3':
        e.printe(int(value))
        
    elif operation == '4':
        e.string = stack.pop()
