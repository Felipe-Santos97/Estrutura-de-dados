class Stack:
  '''Estrutura de dados pilha, representada por um array'''

  def __init__(self):
    self.items = []

  ''' --- Metodos --- 
  
    push(element)
    pop()
    peek()
    clear()
    size()
    is_empty()   
    to_string()
  '''

  def push(self, element):
    if element:
      self.items.append(element)
      return True
    else:
      return False  

  def pop(self):
    if not self.is_empty():
      return self.items.pop() 
    else:
      return False  

  def peek(self):
    if self.is_empty():
      return None
    return self.items[self.size() - 1]      

  def clear(self) -> None:
    self.items = []    

  def size(self):
    return len(self.items)

  def is_empty(self):
    return self.size() == 0

  def to_string(self):
    string = ''
    for element in self.items:
      string += str(f'[{element}] ') 
    return string

