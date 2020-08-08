class stack:
    
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return bool(self.stack == [])

    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def sizeOfStack(self):
        return len(self.stack)
    
    
Stack = stack()
Stack.push(1)
Stack.push(2)
Stack.push(3)

print(Stack.peek())
print(Stack.sizeOfStack())
        