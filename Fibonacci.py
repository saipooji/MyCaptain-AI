#Enter input
n = int(input("Enter value of n: "))
a, b, c = 0, 0, 1
print("Fibonacci Series:")
for i in range(n):
    a = b
    b = c
    c = a + b
    print(a, end=" ")
