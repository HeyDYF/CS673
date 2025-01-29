# Q4 Fibonacci
# Write a program that computes the list of the first 100 Fibonacci numbers.
# The first two Fibonacci numbers are 1 and 1.
# The n+1 Fibonacci number is computed by adding the n-th and the n-1-th Fibonacci number.
# The first few are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8. Print out the results.

a, b = 1, 1
print(a)
print(b)
for _ in range(98):
    c = a + b
    print(f"{a} + {b} = {c}")
    a, b = b, c
