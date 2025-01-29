# Q2 Palindrome
# Write a program that asks a user to input a string and then determine if it’s a palindrome.
# If it is, print out “The string  [is | is not] a palindrome. If the user types q, the program exits.

while True:
    s = input("Enter a string to check for palindrome (type 'q' to quit): ").strip()
    if s == 'q':
        break
    if s == s[::-1]:
        print(f'The string is a palindrome.')
    else:
        print(f'The string not a palindrome.')
