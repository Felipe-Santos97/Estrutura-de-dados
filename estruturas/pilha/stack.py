class Stack:
  '''Classe pilha representada com um dicionário'''

  def __init__(self):
    self.__count = 0
    self._items = {}
  
  ''' --- Metodos --- 
    
     push(element)
     pop()
     peek()
     _clear()
     size()
     is_empty()   
  '''

  @property
  def count(self):
    return self.__count

  @count.setter
  def count(self, value):
    self.__count = value  

  def push(self, element):
    if element:
      self._items[self.count] = element
      self.count += 1
      return True
    return False

  def pop(self):
    if self.is_empty():
      return None
    self.count -= 1
    result = self._items[self.count]  
    del self._items[self.count]
    return result

  def peek(self):
    if not self.is_empty():
      return self._items[self.count - 1]
    return None  

  def _clear(self):
    self.count = 0
    self._items = {}  

  def size(self):
    return self.count    

  def is_empty(self):
    return self.size() == 0

  def to_string(self):
    values = self._items.values()  
    string = ''
    for element in values:
      string += str(f'[{element}] ')  
    return string
