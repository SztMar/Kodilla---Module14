def add(x, y):
   """Return the sum of x and y
   >> add(2, 2)
   4
   >> add(1, 1)
   2
   """

   return x 

def square(x):
   """Return the square of x 
   >> add(2)
   4
   >> add(11)
   121
   """

   return x ** 2

if __name__ == '__main__':
   import doctest
   doctest.testmod()