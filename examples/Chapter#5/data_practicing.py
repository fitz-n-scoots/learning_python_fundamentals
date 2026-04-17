
my_list = ['cat','dog']

def turn_to_set (a_list):
  if len(a_list) - len(set(a_list)) :
    return False
  my_set = set(a_list)
  return True

turn_to_set(my_list)
