passes = 0
failures = 0
counter = 0

while counter < 10:
    result = int(input('enter result(1 = pass, 2 = fail): '))
    if result == 1:
        passes = passes + 1
        counter+=1
    elif result == 2:
        failures = failures + 1
        counter += 1
    else: print('wrong input, kindly enter 1 or 2')

print('Passed:', passes)
print('Failed:', failures)






