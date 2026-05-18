import turtle
import csv
import random

t = turtle.Turtle()

colours = {'red' , 'green' , 'blue' , 'yellow','orange'}
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



def read_csv_data():
  with open('people.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data_list = list(reader)
    return data_list

def generate_shapes ():
  list_of_drawable_shapes  = []
  n = 4678
  m = 60
  for x in range(0,int(n)):
    if random.random() < m/100:  # we are deciding what shape this is ( triangle = true )
      if random.random() < m/100: # we are deciding what colour this is ( blue = true )
        list_of_drawable_shapes.append (('blue','triangle'))
      else:
        list_of_drawable_shapes.append (('orange','triangle'))
    else:
      if random.random() < m/100: # we are deciding what colour this is ( blue = true )
        list_of_drawable_shapes.append (('blue','circle'))
      else:
        list_of_drawable_shapes.append (('orange','square'))
  return list_of_drawable_shapes

  
def draw_shapes (list_of_colour_shape_pairs):
  triangle = 0

  circle = 0

  square = 0
  for colour_shape_pair in list_of_colour_shape_pairs:
    shape = colour_shape_pair[1]
    t.pencolor(str(colour_shape_pair[0]))
    if shape == 'circle':
      t.circle(10)
      t.forward(50)
      circle = circle + 1
    if shape == 'triangle':
      for x in range(3):
        t.left(120)
        t.forward(20)
      t.forward(30)
      triangle = triangle + 1
    if shape == 'square':
      for x in range(4):
        t.left(90)
        t.forward(20)
      t.forward(30)
      square = square + 1										
  turtle.done()

colours = {'red' , 'green' , 'blue' , 'yellow' , 'orange'}

def stats (list_of_colour_shape_pairs):
  # list_of_colour_shape_pairs might look like this
  # [('orange','circle'),('blue','triangle'),('red','square')]
  for colour_and_shape_list in len(list_of_colour_shape_pairs):


# print(list_of_shapes)
colour_shapes = collect_shapes()   
colour_shapes = read_csv_data()
write_csv_data(colour_shapes)

print(colour_shapes)

draw_shapes (colour_shapes)

h = generate_shapes()
print(h)

	
