from node import Node

class LinkedList:
  def __init__(self):
    self._count = 0
    self._head = None

  '''
   --- Métodos ---

   append(element)
   insert(index, element)
   remove_at(index)
   remove(element)  
   get_element_at(index)
   index_of(element)
   search(element)
   size()
   is_empty()
   clear()
   to_string()
  '''   

  def append(self, element):
    if element:
      if self._head:
        '''Se a lista não estiver vazia pegamos o ultimo elemento'''
        last = self.get_element_at(self.size() - 1) 
        last._next = Node(element)
      else:
        '''Se a lista estiver vazia'''
        self._head = Node(element)    
      self._count += 1
      return True
    return False  

  def insert(self, index, element):
    if index >= 0 and index <= self.size() and element:
      node = Node(element)
      if index == 0:
        node._next = self._head
        self._head = node
      else:
        previous = self.get_element_at(index - 1)  
        current = previous._next
        node._next = current
        previous._next = node
      self._count += 1
      return True
    return False    

  def remove_at(self, index):
    '''Remove um elemento apartir de seu indice'''  
    if index >= 0 and index < self.size():
      current = self._head
      if index == 0:
        self._head = current._next
      else:
        previous = self.get_element_at(index - 1)
        current = previous._next
        previous._next = current._next
      self._count -= 1
      return current._element
    return False   

  def remove(self, element):
    index = self.index_of(element)
    result = self.remove_at(index) if index else False
    return result 
      
  def get_element_at(self, index):
    '''Apartir de um indice retorna o elemento correspondente'''
    if index >= 0 and index < self.size():
      current = self._head
      for i in range(index):
        current = current._next
      return current
    return None    

  def index_of(self, element):
    '''Descobre o indice de um elemento na lista'''
    if element:  
      current = self._head
      for i in range(self.size()):
        if current._element == element:
          return i
        current = current._next
    return None    

  def search(self, element):
    result = self.index_of(element)  
    if result != None:
      return True
    else:
      return False  

  def size(self):
    return self._count

  def is_empty(self):
    return self.size() == 0

  def clear(self):  
    self._count = 0
    self._head = None

  def to_string(self):
    if self.is_empty():
      return None
    string = ''
    current = self._head
    for i in range(self.size()):
      string += f'[{current._element}] '
      current = current._next
    return string  
