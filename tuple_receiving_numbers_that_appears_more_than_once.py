def pick_duplicates(tuple_set=(20, 10, 15, 20, 5, 30, 10, 35, 10, 40, 45, 5)):
    counts = {}
    repeated_twice = []

    for num in tuple_set:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num, count in counts.items():
        if count > 1:
            repeated_twice.append(num)

    return tuple(repeated_twice)

result = pick_duplicates()
print(result)
