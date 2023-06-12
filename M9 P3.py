#Greg Brewer
#6/10/23
#Problem 3 Use a while loop, ask the user to enter a number

numbers = []  # Empty list to store entered numbers
total = 0  # Variable to keep track of the sum

while total <= 100:
    user_input = int(input("Enter a number: "))
    numbers.append(user_input)
    total = sum(numbers)

print("Sum of numbers:", total)
print("List of numbers:", numbers)
