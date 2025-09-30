# Chapter 3  
  
## what types of numbers do we use in python  
binary & power of 2  
  
  
### how are they differnt  
A power of two is a number that can be expressed as 2  
Binary, on the other hand, is a numeral  
system that uses only two digits, 0 and 1,  
  
## if we wanted to calculate the whole number part of `15 divided by 2`  
print(15/2)

### what about the remainder  
print(15%2)  
  
## what is a string, and what is differnt about a string and a comment  
a sring is text with quotes and a comment has a hash tag  
  
## what are two ways two ways to creat a string with quotes like this `victor is a "kid" so they say`
"victor is a "\kid"\ so they say"  
'victor is a "kid" so they say'  

## how do we write a string on one line and print out on several lines  
"victor \n is \n a \n kid "  
  
## whats a list in python  
a group of separated charecters  
  
## asign a list to a variable called `pet_names`
pet_names = ["cat", "dog", "snake"]  
extra_pet_names = pet_names  
id(pet_names) == id(extra_pet_names)  
extra_pet_names.append("bunny")  
pet_names  

## how would we add the string `mango` to pets namesafter the list is aleready created  
pet_names = ["cat", "dog", "snake"]  
extra_pet_names = pet_names  
id(pet_names) == id(extra_pet_names)  
extra_pet_names.append("bunny")  
mango = pet_names  
id(pet_names) == id(mango)  
mango.append("mango")


