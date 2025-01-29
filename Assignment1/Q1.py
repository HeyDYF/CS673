# Q1 Multiplication table
# Write a program that prints a multiplication table for numbers up to 12

for i in range(1, 13):
    for j in range(1, i + 1):
        output = '{}x{}={}'.format(j, i, i * j)
        print(f'{output:<12}', end='')
    print()
