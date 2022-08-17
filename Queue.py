class Queue:

    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def enqeue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items) - 1]
a=Queue()
a.enqeue(5)
a.enqeue(6)
print(a.is_empty())
a.dequeue()
print(a.size())
print(a.peek())

