class PriorityQueue:
    def __init__(self):
        self.holder = []

    def enqueue(self, item, value):
        self.holder.append([item, value])
        self.holder.sort(key=lambda tuple: tuple[1], reverse=True)

    def dequeue(self):
        item, value = self.holder.pop()
        return item
    
    def peek(self):
        item, value = self.holder[-1]
        return item
    
    def updatePriority(self, item, value):
        for tuple in self.holder:
            if tuple[0] == item:
                tuple[1] = value
                self.holder.sort(key=lambda tuple: tuple[1], reverse=True)
                return True

        return False
    
    def isEmpty(self):
        if len(self.holder) == 0:
            return True
        return False
    
if __name__ == '__main__':
    testQueue = PriorityQueue()

    testQueue.enqueue(5, 1)
    testQueue.enqueue(2, 10)
    testQueue.enqueue('hello', 2)
    testQueue.enqueue('captain', 5)

    print(testQueue.dequeue())
    print(testQueue.updatePriority('hello', 8))
    print(testQueue.updatePriority('sergeant', 4))
    print(testQueue.holder)
    print(testQueue.dequeue())