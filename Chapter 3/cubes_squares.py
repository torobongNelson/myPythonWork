print(f'   number     square     cube')
for number in range(0, 5 + 1):
    square = number * number
    cube = number * number * number
    print(f'{number:^10} {square:^10} {cube:^10} ')
