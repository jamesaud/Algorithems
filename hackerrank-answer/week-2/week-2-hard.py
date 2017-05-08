#Queue using stacks
#https://www.hackerrank.com/challenges/queue-using-two-stacks

# Enter your code here. Read input from STDIN. Print output to STDOUT

nums = input()

class Queue(object):

    def enqueue(self, num):
        self.queue.append(num)

    def dequeue(self):
        del self.queue[0]

    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)
    
    def peak_front(self):
        try:
            return self.queue[0]
        except IndexError:
            return []
q = Queue()

for _ in range(nums):
    inp = raw_input()
    if inp == '3':
        print(q.peak_front())
    elif inp == '2':
        q.dequeue()
    else:
        q.enqueue(inp.split(' ')[1])
