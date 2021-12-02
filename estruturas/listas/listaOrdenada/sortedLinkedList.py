from sys import path
from os import getcwd
'''
Para importar modulos em outros diretórios devemos passar o caminho completo
Caso não funcione coloque o caminho completo no segundo parametro do metodo: path.insert()
'''
path.insert(1, f'{getcwd()}/estruturas/listas/listaLigada')

from linkedList import LinkedList
 
 
class SortedLinkedList(LinkedList):
  def __init__(self):
      super().__init__()
 
  '''
    ---- Métodos ----

    remove_at(index)
    remove(element)  
    get_element_at(index)
    index_of(element)
    search(element)
    size()
    is_empty()
    _clear()
    to_string()

    --- Sobrescrito/Novo ---
  
    insert(index, element)
    append(element)
    get_sorted_index(element)
  '''

  def insert(self, index , element):
    '''Se nao for o primeiro item, devemos descobrir onde inscerir'''
    if self.is_empty():
      return super().insert(0, element)
    else:
      position = self.get_sorted_index(element)
      return super().insert(position, element)
   
  def append(self, element):
    return self.insert(0, element) 
    
  def get_sorted_index(self, element):
    current = self._head
    index = 0
    while(index < self.size() and current):
      if element < current._element:
        return index
      current = current._next
      index += 1
    return index    
