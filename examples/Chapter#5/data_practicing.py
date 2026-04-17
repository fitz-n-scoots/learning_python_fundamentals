
my_list = ['cat','dog']

def turn_to_set (a_list):
  if len(a_list) - len(set(a_list)) :
    return 'can not be a set'
  my_set = set(a_list)
  print('this is a set ' + str(set(a_list)))

turn_to_set(my_list)
