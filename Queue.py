class Queue: # Just an implementation of a queue.
    def __init__(self):# Initialises the queue to an empty queue.
        self.queue = []

    def enqueue(self,val): # Appends item val onto the end of the queue.
        self.queue.append(val)

    def dequeue(self):# Pops the head off the queue and returns it value.
        val = None
        try:
            val = self.queue[0]
            if len(self.queue) == 1:
                self.queue = []
            else:
                self.queue = self.queue[1:]
        except:pass
        return val

    def IsEmpty(self):# Returns True if the queue is empty.
        result = False
        if len(self.queue) == 0:
            result = True
        return result


