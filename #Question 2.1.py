#Question 2.1
from collections import deque
from queue import LifoQueue
class Empty(Exception):
    pass
class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    
    def transfer(self):
        S = [10,25,15,7]
        T = []
        print("Stack S: ",S)
        print("Lenght of stack S before the transfer:",len(S))   
        print("Lenght of stack T before the transfer:",len(T))
        print("Item at the top of stack S:",S[0])

        while S:
            T.append(S.pop())
        print("The transfer was succesfull")
        print("Item at the top of stack T",T[0])
        print("Lenght of stack S after Transfer:",len(S))
        print("Stack T after the transfer: ",T)
        print("Stack S after the transfer:", S)
        
    



arr = []
ArrayStack.transfer(arr)

