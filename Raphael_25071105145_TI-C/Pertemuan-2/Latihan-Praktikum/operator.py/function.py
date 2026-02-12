def my_function():
  print("Hello from a function")

my_function()

#argument 

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# scope 
def myfunc():
  x = 300
  print(x)

myfunc()

#lambda 

x = lambda a : a + 10
print(x(5))

#recursion

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

