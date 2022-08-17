class stack:

    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def push(self,item):
        self.itemsappend(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    num=int(input("enter a number for verification\n"))
    def eoro(num):
        if num%2==0:
            print("given number ",num," is even\n")
        else:
            print("given number ",num," is odd")
a=stack()
a.eoro()

