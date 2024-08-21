# till last number as input
print("Enter the end number/range of fibonacci series: ", end="")
n = int(input())
print("The Series is: ", end="")
 

def fibonacci(n):
    c = 0
    a = 0
    b = 1
    if n == 0:
        print(a, end=" ")
    if n == 1:
        print(a, b, end=" ")
    else:
        print(a, b, end=" ")
        while c < n:
            c = a + b
            if c <= n:
                print(c, end=" ")
            a = b
            b = c


fibonacci(n)


# for total digits as inputs
print("Enter the total digits in fibonacci series: ", end="")
n = int(input())
print("The Series is: ", end="")


def fib(n):
    a = 0
    b = 1
    c = 0
    if n == 1:
        print(a)
    if n == 2:
        print(a, b, end=" ")
    else:
        print(a, b, end=" ")
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c, end=" ")


fib(n)
