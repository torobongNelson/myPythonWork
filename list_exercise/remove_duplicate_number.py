def remove_duplicates(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)