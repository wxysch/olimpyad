# import random
# NumberToGuess = random.randint(1,100)
# userGuess = -1
#
# while userGuess != NumberToGuess:
#     userGuess = int(input('Угадай число от 1 до 100: '))
#     if userGuess > NumberToGuess:
#         print('Число дожно быть меньше')
#     elif userGuess < NumberToGuess:
#         print('Число должно быть больше')
#     else:
#         print('Вы угадали, это число = '+str(NumberToGuess))
#         break

'''
Последовательности символов создаются по следующему правилу.Нулевая строка: "ABCDEFGH".
Каждая из следующих строк создается следующим действием: дважды подряд записывается
предыдущая строка и в конце дописывается очередная буква английского алфавита,
начиная с A. Вот строки номерами 1-3, созданные по этому правилу:

1.ABCDEFGHABCDEFGHA
2.ABCDEFGHABCDEFGHAABCDEFGHABCDEFGHAB
3.ABCDEFGHABCDEFGHAABCDEFGHABCDEFGHABABCDEFGHABCDEFGHAABCDEFGHABCDEFGHABC

Сколько раз в строке с номером 8 встретится символ D?
В ответе укажите  целое число.
'''

# a=b='ABCDEFGH'
# for i in range(0,8):
#     c=a+a+b[i]
#     a=c
# print(c)
# i=0
# sum=0
# while i<len(c):
#     sum=sum+1
#     i=i+1
# print(sum)

'''
Программист Билл занимается разработкой программного обеспечения для новейшего 
робота-исследователя, которого учёные планируют отправить на Марс с целью поиска 
там следов разумной жизни. Модули, которые отвечают за передвижение робота и сбор проб грунта, 
Билл уже скачал из Интернета. Оставалось лишь научить робота отличать разумные формы жизни от неразумных. 
Для этого Боб несколько месяцев посещал программистские форумы, и, наконец, нашёл подходящий модуль. 
Теперь, чтобы определить, 
является ли тот или иной объект представителем внеземной расы, роботу 
достаточно сравнить два вещественных числа.
Однако за несколько часов до запуска корабля на Марс обнаружилось, что 
робот неправильно сравнивает вещественные числа! Чтобы исправить эту ошибку, учёные обратились за помощью к Вам.
'''

from decimal import Decimal
a = Decimal(input())
b = Decimal(input())
if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('=')