# count = 0
# number_of_even_numbers = 0
# number_of_odd_numbers = 0
#
# number = 1, 2, 3, 4, 5, 6, 7, 8, 9
#
# for count in number(1,9):
#     if number % 2 == 0:
#     print(number_of_even_numbers)
#
#     if number % 2 == 0:
#     print(number_of_even_numbers)


even = 0
odd = 0
number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for checker in number:
    if checker % 2 != 0:
        even = even + 1
    else:
        odd += 1

print("Number of even number:", even)
print("Number of odd number:", odd)
