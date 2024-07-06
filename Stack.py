class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def push(self, item):
        self.stack.append(item)
        self.size += 1
    
    def pop(self):
        returnValue = None
        try:
            returnValue = self.stack.pop()
            self.size -= 1
        except: pass
        return returnValue

    def isEmpty(self):
        if self.getSize() > 0:
            return False
        return True

if __name__ == '__main__':
    stack = Stack()
    print(stack.pop())
    print(stack.getSize())