class Queue:
  '''
    Etrutura de dado fila, representado por um dicionario.
    Filas seguem o principio FIFO (first in first out)   
  '''

  def __init__(self):
      self._count = 0
      self._first_element = 0
      self._items = {}

  ''' --- Metodos ---
   
    enqueue(element)
    dequeue()
    peek_first()
    peek_last()
    is_empty()
    size()
    search(element)
    _clear()
    to_string()
  '''    
  
  def enqueue(self, element):
    self._items[self._count] = element
    self._count += 1
    return True
     
  def dequeue(self):
    if self.is_empty():
      return False
    result = self.peek_first()
    del self._items[self._first_element]
    self._first_element += 1
    return result  

  def peek_first(self):
    if self.is_empty():
      return None
    return self._items[self._first_element]  

  def peek_last(self):
    if self.is_empty():
      return None
    return self._items[self.size() - 1]    

  def is_empty(self):
    return self.size() == 0

  def size(self):
    return self._count - self._first_element

  def search(self, element):
    values = self._items.values()
    if element in values:
      return True
    return False   

  def _clear(self):
    self._count = 0
    self._first_element = 0
    self._items = {}

  def to_string(self):
    if self.is_empty():
      return None
    values = self._items.values()
    string = ''
    for i in values:
      string += str(f'[{i}] ')
    return string     
