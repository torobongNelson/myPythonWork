def largest_number_in_array(numbers):
    max_num = numbers.arr[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
