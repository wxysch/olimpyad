'''
Найдите наибольшее число
'''
# a = int(input())
# b = int(input())
# if a > b:
#     print("a ")
# else:
#     print("b")




'''На свой день рождения Петя купил красивый и вкусный торт, который имел идеально круглую форму. 
Петя не знал, сколько гостей придет на его день рождения, поэтому вынужден был разработать алгоритм, 
согласно которому он сможет быстро разрезать торт на N равных частей. Следует учесть, что разрезы торта можно 
производить как по радиусу, так и по диаметру.
Помогите Пете решить эту задачу, определив наименьшее число разрезов торта по заданному числу гостей
'''

# n = int(input())
# if n %2==0:
#     print(n//2)
# else:
#     if n==1:
#         print(0)
#     else:
#         print(1)

'''
Бандиты Гарри и Ларри отдыхали на природе. Решив пострелять, они выставили на бревно несколько банок из-под кока-колы (не больше 10). Гарри начал простреливать банки по порядку, начиная с самой левой, Ларри — с самой правой. В какой-то момент получилось так, что они одновременно прострелили одну и ту же последнюю банку.
Гарри возмутился и сказал, что Ларри должен ему кучу денег за то, что тот лишил его удовольствия прострелить несколько банок. В ответ Ларри сказал, что Гарри должен ему еще больше денег по тем же причинам. Они стали спорить кто кому сколько должен, но никто из них не помнил сколько банок было в начале, а искать простреленные банки по всей округе было неохота. Каждый из них помнил только, сколько банок прострелил он сам.
Определите по этим данным, сколько банок не прострелил Гарри и сколько банок не прострелил Ларри.
'''

# a,b=map(int,input().split())
# c=a+b-1
# print(c-a,c-b)

'''
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
'''

# x = int(input())
# d6 = x%10
# d5 = x//10%10
# d4 = x//100%10
# d3 = x//1000%10
# d2 = x//10000%10
# d1 = x//100000%10
# if d1+d2+d3+d4+d5+d6:
#     print("YES")
# else:
#     print("No")


'''
Белочка собрала в лесу N шишек c орешками. 
Белочка очень привередливо выбирала шишки, и брала только те, в которых ровно M орешков. 
Также известно, что для пропитания зимой ей необходимо не менее K орешков. 
Определите, хватит ли на зиму орешков белочке.
'''

# a = list(map(int,input().split()))
# if a[0]*a[1] >= a[2]:
#     print("YES")
# else:
#     print("NO")

'''
В шкатулке хранится разноцветный бисер (или бусины). Все бусины имеют одинаковую форму, размер и вес. 
Бусины могут быть одного из N различных цветов. 
В шкатулке много бусин каждого цвета.
Требуется определить минимальное число бусин, 
которые можно не глядя вытащить из шкатулки так, чтобы среди них гарантированно были две бусины одного цвета.
'''

# n = int(input())
# print(n+1)

#n = int(input())
#if n%2 == 0:
#    print('Четное')
#else:
#    print('Нечетное')