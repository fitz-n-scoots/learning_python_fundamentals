# chapter#4

## How would we read in a string variable called 'name' and print out that the person has a short name if the name is less than 5 characters, that they have a normal name if it between 5 and 8 characters, and that they have a long name otherwise?

```python
if len(victor) = <5:
    print('you have a normal name')
elif (len(victor)) == >5:
    print('you have a long name')
```

## How can we use the 'for' statement, the 'len()' function, and the 'range()' function to print every element in a list?
```python
for i in range(len('victor')):
   print(i, 'victor'[i])
```
### How does this work?
it checks the lengh of victor and then prints victor line by line

# day 2

## What is the difference between positional args and keyword args?
positional args have to be in sertent places key word args have sertant names

## How could we write a function that accepted one greeting string and a list of pet names which would print that greeting once for each pet?

```python
pets = ['mason,'scooter','fitz']
def pets(greeting, name):
pets('hi', pets)  
```


# day 3

## what hapends in the header of a python function definition
it says the name of the function and the def  

### what hapends in the body  
it says the stuff that it is going to do somthing

## does a function always return something to the caller? what about when we dontinclde a "return" statment
no kindof

## 
```python
pets = ['scooter','fitz']

def pets(greeting, name , punctuation):
pets('hi',punctuation='.',name = 'fitz')  
pets('hello',punctuation='?',name = 'scooter') 
```
