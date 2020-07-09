# Цикл while

i = 1
while i <= 10:
    print(i ** 2)
    i += 1
	
	
n = int(input())
length = 0
while n > 0:
    n //= 10  # это эквивалентно n = n // 10
    length += 1
print(length)	


# Инструкции управления циклом

i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Цикл окончен, i =', i)
	
	
a = int(input())
while a != 0:
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
    a = int(input())
else:
    print('Ни одного отрицательного числа не встретилось')	
	
	
n = int(input())
for i in range(n):
    a = int(input())
    if a < 0:
        print('Встретилось отрицательное число', a)
        break    
else:
    print('Ни одного отрицательного числа не встретилось')
	
	
for i in range(3):
    for j in range(5):
        if j > i:
            break
        print(i, j)

		
n = int(input())
length = 0
while True:
    length += 1
    n //= 10
    if n == 0:
        break
print('Длина числа равна', length)


n = int(input())
length = 0
while n != 0:
    length += 1
    n //= 10
print('Длина числа равна', length)


n = int(input())
print('Длина числа равна', len(str(n)))

#  Множественное присваивание

a = 1
b = 2
tmp = a
a = b
b = tmp
print(a, b)  
# 2 1


a = 1
b = 2
a, b = b, a
print(a, b)  
# 2 1


