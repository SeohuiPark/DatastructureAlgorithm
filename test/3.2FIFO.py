class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)


class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack() # 스택 두개로 큐 구현하기
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size() + self.stack2.size()

    def push(self, item):
        if self.qsize() == self.max_size:
            return False
        self.stack1.push(item)
        return True

    def pop(self):
        try:
            if self.stack2.size() == 0:
                while self.stack1.size() > 0:
                    self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        except IndexError:
            return False


n, max_size = map(int, input().strip().split(' '))

queue1 = MyQueue(max_size)

for _ in range(n):
    cmd = input()
    if "POP" == cmd:
        print(queue1.pop())
    elif "SIZE" == cmd:
        print(queue1.qsize())
    else: # PUSH
        x = cmd.split()[1] # push element
        print(queue1.push(x))

