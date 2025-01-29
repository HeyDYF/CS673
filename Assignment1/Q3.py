# Q3 Combine strings
# Write a program that asks the user to input two lists of equal length in the format: [a,b,c], [1,2,3].
# The program should test that both lists are of equal length, if not, print out an error message.
# If they are the same length, combine the two lists by alternatingly taking elements and output the results.
# Using the input example above, the output would be: [a,1,b,2,c,3].

list1 = [item.strip() for item in input("Enter first list: ").strip("[]").split(",")]
list2 = [item.strip() for item in input("Enter second list: ").strip("[]").split(",")]

if len(list1) != len(list2):
    print("Error: The two lists must have the same length.")
else:
    print(f"[{', '.join(sum(zip(list1, list2), ()))}]")


