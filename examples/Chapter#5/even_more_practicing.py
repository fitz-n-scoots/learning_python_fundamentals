import turtle
import csv

t = turtle.Turtle()

colours = {'red' , 'green' , 'blue' , 'yellow'}
shapes = {'circle','triangle','square'}

def collect_shapes ():
  c = ''

  my_list = []
  while (True):
    y = ''
    s = ''
    c = ''
    while y != 'yes' and y != 'no':
      y = input('add more discrption?:  ')
    
    if y == 'no':
      break
	
    while c not in colours:
      c = input('what colour?:  ')
    while s not in shapes:
      s = input('circle triangle or square?:  ')
    shape_data = (c,s) 
    my_list.append(shape_data)
  return my_list
  print("done collecting.")

 




    
def write_csv_data(list_of_colour_shape_pairs):
  with open('people.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(list_of_colour_shape_pairs)
#  with open('people.csv', 'r') as file:
#    for line in file:
#        print(line.strip())
#  import csv


def read_csv_data():
  with open('people.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data_list = list(reader)
#    for row in data_list:
    return data_list





def draw_shapes (list_of_colour_shape_pairs):
  for colour_shape_pair in list_of_colour_shape_pairs:
    shape = colour_shape_pair[1]
    t.pencolor(str(colour_shape_pair[0]))
    if shape == 'circle':
      t.circle(10)
      t.forward(50)
    if shape == 'triangle':
      for x in range(3):
        t.left(120)
        t.forward(20)
      t.forward(30)
    if shape == 'square':
      for x in range(4):
        t.left(90)
        t.forward(20)
      t.forward(30)
  turtle.done()
	

#print(list_of_shapes)
colour_shapes = collect_shapes()   
colour_shapes = read_csv_data()
write_csv_data(colour_shapes)

print(colour_shapes)

draw_shapes (colour_shapes)

