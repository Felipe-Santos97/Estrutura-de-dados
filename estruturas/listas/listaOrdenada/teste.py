from sortedLinkedList import SortedLinkedList
from random import randint


lista = SortedLinkedList()


for i in range(20):
  lista.append(randint(1,30))

lista.insert(0, 100)  
 
print(lista.to_string())
 