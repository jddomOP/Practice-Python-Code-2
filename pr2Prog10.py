a = int(input ("Enter first number:"))
b = int (input ("Enter second number:"))

if a > b:
    a, b = b, a

for i in range (a + 1, b):
    print(i)
