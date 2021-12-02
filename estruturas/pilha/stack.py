class Stack:
  '''Classe pilha representada com um dicionário'''

  def __init__(self):
    self._count = 0
    self._items = {}
  
  '''
  --- Metodos --- 
    
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
      self._items[self._count] = element
      self._count += 1
      return True
    return False

  def pop(self):
    if self.is_empty():
      return None
    self._count -= 1
    result = self._items[self._count]  
    del self._items[self._count]
    return result

  def peek_last(self):
    if not self.is_empty():
      return self._items[self._count - 1]
    return None  

  def _clear(self):
    self._count = 0
    self._items = {}  

  def size(self):
    return self._count    

  def is_empty(self):
    return self.size() == 0

  def search(self, element):
    return element in self._items.values()  

  def to_string(self):
    values = self._items.values()  
    string = ''
    for element in values:
      string += str(f'[{element}] ')  
    return string
