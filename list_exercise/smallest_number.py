def largest_number_in_array(numbers):
    min_num = numbers.arr[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num
