def collect_student_data ():
  my_list = []
  while (True):
    s = input('add another student?:')
    
    if s != 'yes':
      if s != 'no':
        print('has to be yes or no')
        
    if s == 'no':
      break
      
    if s == 'yes':
      h = input('whats there name:')
      txt = ""
      d = 0
      while not txt.isdigit():
        txt = input('whats there age:')
        if txt.isdigit():
          d = int(txt)
      v = ''
      while v != 'm' and 'f':
        v = input('whats there sex:')
        if v != 'm':
          if v != 'f':
            print('has to be f or m')
    student_data = (h,d,v)
    print (student_data)
    my_list.append(student_data)
  return my_list

list_of_students = collect_student_data ()
#list_of_students = [('bill',6,'m'),('joe',6,'m'),('joe',7,'m')]
print(list_of_students)

# We want a dictionary in the form:
# {
#   "name1" : ("name1", age1, "sex1"), 
#   "name2" : ("name2", age2, "sex2")
# }

print('there are ' + str(len(list_of_students)) + ' students')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

my_dict = {}

for student_data in list_of_students:
  if student_data[0] in my_dict:
    print('ERROR! two of the same name!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
  my_dict [student_data[0]] = student_data 
  
  
print(my_dict)
