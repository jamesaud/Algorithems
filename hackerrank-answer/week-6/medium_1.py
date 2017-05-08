#https://www.hackerrank.com/challenges/balanced-brackets

#!/bin/python


  
def Match(string):
    stack = []
    pairs = {'{':'}', '[':']','(':')'}
    for char in string:
        if char in '[{(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            
            if pairs.get(last) != char:
                return False
      
    if len(stack) != 0:
        return False
              
    return True
 

x = int(raw_input())
for _ in range(x):
    s = raw_input()
    if Match(s):
        print "YES"
    else:
        print "NO"
