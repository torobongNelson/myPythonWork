# passes = 0
# failures = 0
# counter = 0
#
# while counter < 10:
#     result = int(input('enter result(1 = pass, 2 = fail): '))
#     if result == 1:
#         passes = passes + 1
#         counter+=1
#     elif result == 2:
#         failures = failures + 1
#         counter += 1
#     else: print('wrong input, kindly enter 1 or 2')
#
#
#
#
# print('Passed:', passes)
# print('Failed:', failures)
#
#
#
# a = b = 7
# print('a =', a, '\nb =', b)
#


for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>',end='')
    print()


for row in range(7):
    for column in range(7):
        print('@', end='')
    print()
