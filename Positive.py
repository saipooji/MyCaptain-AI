# Enter numbers separated by space
numbers = list(map(int, input().split()))
# Filtering positive numbers
positive_numbers = [num for num in numbers if num > 0]
# Printing the output
print("Output:", ", ".join(map(str, positive_numbers)))
