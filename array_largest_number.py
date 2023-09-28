numbers = [10, 15, 25, 40, 45, 50, 55]

largest = numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest = num

# Print the largest number
print("The largest number in the list is:", largest)