from minHeap import MinHeap
from random import randint

heap = MinHeap()


for i in range(1,7):
  heap.insert(randint(1,30))



print(heap.to_string())
print(heap.find_first())
print('-=' * 23)

