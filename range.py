#九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(i) + '*' + str(j) + '=' + str(i * j), end='\t')
    print()

for i in range(1, 10):
    for j in range(i,10):
        print(str(i) + '*' + str(j) + '=' + str(i * j), end='\t')
    print('\n'+'\t\t' * i, end='')
#打印菱形
print('---------------------------')
for i in range(1, 8, 2):
        print(' ' * (7-i), end='')
        print('* ' * i)
for i in range(5, 0, -2):
        print(' ' * (7 - i), end='')
        print('* ' * i)
#中心对称
prespace = 0
for i in range(-3, 4):
    if i > 0:
        prespace = i
    else:
        prespace = -i
    print(' '*prespace*2+'* ' * (7 - prespace * 2))

