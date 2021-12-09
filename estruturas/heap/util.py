def compare_two_elements(first, second):
  if first == second:
    return Compare['EQUALS']
  elif first < second:
    return Compare['LESS_THAN']
  else:
    return Compare['BIGGER_THAN']    

Compare = {
  'LESS_THAN': -1,
  'BIGGER_THAN': 1,
  'EQUALS': 0
}

def swap(list, first, second):
  temp = list[first]
  list[first] = list[second]
  list[second] = temp
