class Stack:
  '''Estrutura de dados pilha, representada por um array'''

  def __init__(self):
    self._items = []

  ''' --- Metodos --- 
  
    append(element)
    pop()
    peek_last()
    _clear()
    size()
    is_empty()   
    search(element)
    to_string()
  '''

  def append(self, element):
    if element:
      self._items.append(element)
      return True
    else:
      return False  

  def pop(self):
    if self.is_empty():
      return False  
    else:
      return self._items.pop() 

  def peek_last(self):
    if self.is_empty():
      return None
    return self._items[self.size() - 1]      

  def _clear(self):
    self._items = []    

  def size(self):
    return len(self._items)

  def is_empty(self):
    return self.size() == 0

  def search(self, element):
    return element in self._items  

  def to_string(self):
    string = ''
    for element in self._items:
      string += str(f'[{element}] ') 
    return string
