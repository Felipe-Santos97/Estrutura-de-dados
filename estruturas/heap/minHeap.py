from math import floor
from util import compare_two_elements, Compare, swap


class MinHeap:

  def __init__(self):
    self._heap = []

  '''
  --- Métodos --- 

  get_left_child(index)
  get_right_child(index)
  get_parent(index)
  insert(value) 
  sift_up(index)
  extract()
  sift_down(index)
  find_first()
  size()
  is_empty()
  search(element)
  to_string()
  '''  

  @staticmethod
  def get_left_child(index):
    return 2 * index + 1

  @staticmethod
  def get_right_child(index):
    return 2 * index + 2  

  @staticmethod
  def get_parent(index):
    if index == 0:
      return None 
    return floor( (index - 1) / 2 )  

  def insert(self, element):
    self._heap.append(element)
    self.sift_up(self.size() - 1)
    return True

  def sift_up(self, index):
    parent = MinHeap.get_parent(index)
    while(index > 0 and 
    compare_two_elements(self._heap[parent] , self._heap[index]) == Compare['BIGGER_THAN']):
      swap(self._heap, parent, index)
      index = parent
      parent = MinHeap.get_parent(index)

  def extract(self):
    if self.is_empty():
      return False
    elif self.size() == 1:
      return self._heap.pop(0) 
    else:
      removed = self._heap[0]
      self._heap[0] = self._heap.pop()
      self.sift_down(0)      
      return removed

  def sift_down(self, index):
    element = index
    left = MinHeap.get_left_child(index)
    right = MinHeap.get_right_child(index)
    size = self.size()
    if left < size and compare_two_elements(self._heap[element], self._heap[left]) == Compare['BIGGER_THAN']:
      element = left
    if right < size and compare_two_elements(self._heap[element], self._heap[right]) == Compare['BIGGER_THAN']:
      element = right
    if index != element:
      swap(self._heap, index, element)
      self.sift_down(element)   


  def find_first(self):
    if self.is_empty():
      return None
    return self._heap[0]      

  def size(self):
    return len(self._heap)  

  def is_empty(self):
    return self.size() == 0

  def search(self, element):
    return element in self._heap  

  def to_string(self):
    string = ''
    for element in self._heap:
      string += f'[{element}] '
    return string    
 