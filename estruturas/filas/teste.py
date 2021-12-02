from queue import Queue
from random import randint

fila = Queue()

for i in range(1,6):
  fila.enqueue(i)

print(fila.search(6)) 
 
print(fila.to_string())
 
 