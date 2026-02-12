#arithmetic operator
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#assignment operator
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#comparison operator

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#logical operator
 
x = 5

print(x > 0 and x < 10)

x = 5

print(x < 5 or x > 10)

x = 5

print(not(x > 3 and x < 10))

#identity operator

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#membership operator

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

# bitwise operator

print(6 & 3)

#precedence operator

print(5 + 4 - 7 + 3)