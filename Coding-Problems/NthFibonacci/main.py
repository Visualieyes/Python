import math

#f(0)==0, f(1)==1, f(2)==1
def F(n): 
  if n<0:
    return 'incorrect input'
  elif n==0:
    return 0
  elif n<=2:
    return 1
  else:
    return round ((
    ( 1/math.sqrt(5) ) * (
    ( ((1+math.sqrt(5)) / 2 )**n ) - 
    ( ((1-math.sqrt(5)) / 2 )**n )
    )  
  ), 0)