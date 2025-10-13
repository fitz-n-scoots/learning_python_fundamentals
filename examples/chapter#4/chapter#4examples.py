# what is a function?

# a block of code that can change somthing
def pets():
  print('are you a dog are you a cat?')  
pets()

# what is an if

# you ask it somthing and it gives you somthing else
name = ('sebastian')  
if len(name) >7: 
    print(name+' is a long name')
  
# what is else

# its like if but the opposite
victor = ('victor')
jack = ("jack")
if len(victor) < len(jack):
  print("victor is shorter than jack")
else:
  print("jack is shorter than victor")

# what is elif
    
# elif is both combined
if 1 > 1:
  print("1 is greater than 1")
elif 1 == 1:
  print("1 and 1 are equal")
  
# what is a while loop
# every time you go around the loop it changes what you give it 
count = 0
while count < 3:
  print('yes!' + '!'*count)
  count=count+3-1+4-5
   
# what is a for loop
# a for loop is a loop that goes aruond as man times as what you give it has
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
