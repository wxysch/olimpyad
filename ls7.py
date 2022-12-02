'''Требуется вставить в массив на данное место данный элемент, сдвинув
остальные элементы вправо. '''

# n = int(input())
# array = []
# for i in input().split():
#     array.append(int(i))
# k, j = input().split()
# k, j = int(k), int(j)
# array = array[:j - 1] + [k] + array[j - 1:]
# ret = str(array[0])
# for i in range(1, len(array)):
#    ret = ret + ' ' + str(array[i])
# print(ret)

''' найдите двойной факториал числа '''

# n = int(input())
# start = 1 if n % 2 else 2
# for i in range(start + 2, n + 1, 2):
#     start *= i
# print(start)

'''Простое число называется гиперпростым, если любое число, получающееся из него
откидыванием нескольких цифр, тоже является простым. Например, число 733 –
гиперпростое, так, как и оно само, и числа 73 и 7 – простые. Напишите программу, которая
определяет, верно ли, что переданное ей число – гиперпростое'''

# x = int(input())
# deliteli = 0
# for i in range(1,x):
#     if x%2 == 0:
#         deliteli +=1
# print(deliteli)