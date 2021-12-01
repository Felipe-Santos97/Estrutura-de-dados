#from stackArray import Stack
from stack import Stack
from random import randint

pilha = Stack()
 
for i in range(1,6):
  pilha.push(randint(1,20))


print(pilha.to_string())


print(pilha.peek())
