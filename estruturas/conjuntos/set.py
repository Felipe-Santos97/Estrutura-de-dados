class Set:

  '''Set é uma estrutura onde só permite valores unicos
    É salvo em um dicionario onde o elemento é a chave e o valor
    A chave será string e o valor qualquer tipo
      items = {
       '1': 1,
       '2': 2 
      } 
  '''

  def __init__(self):
    self._items = {}

  '''
    --- Metodos ---

    has(element)  
    add(element)
    delete(element)
    values()
    size()
    is_empty()
    _clear()
    to_string()
  '''    

  def has(self, element):
    return element in self.values() 

  def add(self, element):
    if not self.has(element):
      self._items[str(element)] = element
      return True
    return False      

  def delete(self, element):
    if self.has(element):
      del self._items[str(element)]  
      return True
    return False  

  def values(self):
    return self._items.values()  

  def size(self):
    return len(self.values())

  def is_empty(self):
    return self.size() == 0  

  def _clear(self):
    self._items = {}  

  def to_string(self):
    if self.is_empty():
      return None
    string = ''
    values = self.values()
    for value in values:
      string += f'[{value}] '  
    return string
