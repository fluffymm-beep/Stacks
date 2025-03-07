stack = []
for i in range(1,11):   #push 1 to 10
    stack.append(i)

print(stack)
print(stack.pop())  #pop 10
print(stack[-1])    #peek the last item:9
print(len(stack))   #size :9
print(stack)
print("--------------------------------------------------")
from collections import deque
stack_1 = deque()
for i in range(10,31,10):   #push 10,20,30
    stack_1.append(i)
print(stack_1)
print(stack_1.pop())  #pop 30
print(stack_1[-1])    #peek the last item:20
print(len(stack_1))   #size:2
print(stack_1)

from queue import LifoQueue as lf
stack_2 = lf()
stack_2.put(10)
stack_2.put(20)
print(stack_2.get()) #pop:20
print("--------------------------------------------------")
class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items) == 0
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)

stack_3 = Stack()
for i in range(101,111):stack_3.push(i) #push 101 to 110
print(stack_3.pop()) # pop :110
print(stack_3.peek()) #peek the last number :109
print(stack_3.size()) #size:9
print("--------------------------------------------------")
def being_correct(text):
    stack = []
    pairs = {")":"(","}":"{","]":"["}
    for i in text:
        if i in "([{":
            stack.append(i)
        elif i in ")]}":
            if not stack or stack.pop() != pairs[i]:
                return False
    return not stack
print(being_correct("a{b(c)d}ef"))
print(being_correct("a{bc]def"))