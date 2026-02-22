 
 
 
def check_divisbility (number):
  if number != int(number):
    print(  'ERROR NOT INT!!!!!!!!!!')
    return False
  d = number//2+1
  for x in range(d):
    if d == 1:
      break
    if number%d != 0:
      print(str(number) + ' is not divisible by ' + str(d) )
      n = ' true'
    if number%d == 0:
      print(str(number) + ' is divisible by ' + str(d))
      n = ' false'
      return False
    d = d - 1
  return True
      
  
for x in range(102,122):  
  check_divisbility(x)
