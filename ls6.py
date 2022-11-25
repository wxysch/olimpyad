# x=int(input())
# a=(x+3)/2
# b=(a+3)/2
# c=(b+3)/2
# print(c)
# ==========================================================
# борбору 1 чекитте жаткан 2 тегерек берилген
# чондуку Р р
# -----------------------
# from math import pi
# R=float(input())
# r=float(input())
# S1=pi*R**2
# S2=pi*r**2
# s=S1-S2
# print(s)
# ================================
# from math import *
# a=float(input())
# print(((a**2)+10)/sqrt(a**2+1))
# эки чекиттин кординатасы берилген алардын арасындагы аралыкты тапкыла
# ======================================
# from math import *
# x1,y1,x2,y2=map(float,input().split())
# d=sqrt(x2-x1)**2 + (y2+y1)**2
# print(d)
# =============================================
# from math import *
# xa,ya,xb,yb,xc,yc=map(float,input().split())
# d=sqrt((xb-xa)**2 + (yb-ya) **2 )+ sqrt((xb - xc) ** 2 + (yb - yc)**2) + sqrt((xc -xa)**2+(yc+ya)**2)
# print(d)
# -------------------------------------------------------------------------
# mm=int(input())ццв
# m=mm//1000
# sm=mm%1000//10
# Wmmm=mm%1000%10
# print(mk,sm,mmm)
# ======================================
# a=int (input())#
# if a>0:
#	print("он сан ")
# elif a<0:
#	print("терс сан")
# else :
#	print("нол")
# -------------------------------------------------------------------------------------
# a=int(input())
# if a%2==0:
#	print("жуп")
# else :
#	print("так")
# =========================================================
# m,n=map(int,input("Введите размер канверта").split())
# q,p=map(int,input("Введите размер письма").split())
# if m>q and n>p or m>p and n>q:
#	print("Кат конвертке батат")
# else:
#	print("кат конвертке батпайт")
# =========================================================
# x,y=map(int,input("Введите два разных чисел").split())
# if x%2==1 and y%2==1:
#	print(x,y)
# elif x%2==1:
#	print(x)
# elif y%2==1:
#	print(y)
# else:
#	print("Нету ничетных чисел")
# ===========-----------------------------------
# from math import sqrt
# x,y,r=map ()
# sqrt(d=x**2+y**2)
# if x=0 and y=0:
#	print("борборунда")
# elif d


# ========================
# a=input()
# print(a[0])
# print(a[-2])
# print(a[0:5])
# print(a[-1::-2])
# print(a[1::2])
# print(a[2::2])
# print(a[::-1])
# print(a[::-2])
# print(len(a))
# ======================================================
# a=input()
# print (a)
# print(a.count("м"))
# сап берилген анан  палиндром экенин далилдегиле
# --------------------------------------------------------------------------------------------
#n = int(input())
#m = (input().split(" "))
#m2 = []
#for i in m:
#    m2.append(int(i))
#max1 = max(m2)
#min1 = min(m2)
#m3 = []
#for i in range(min1, max1 + 2, 2):
#    if i > max1:
#        break
#    else:
#        m3.append(i)

#h = []
#for i in m2:
#    if i != min1:
#        h.append(i)
#    min1 += 2
#set1 = set(m3)
#set2 = set(m2)
#list3 = list(set1.difference(set2))

#if not list3:
#    print(*h)
#elif not h:
#    print(*list3)

#n = int(input())
#sum = (1 + n) / 2 * n
#print(sum)

'''Ввести натуральное число N и вывести все натуральные числа, не
превосходящие N и делящиеся на каждую из своих цифр.'''

# n = int(input())
# for i in range(1,n+1,1):
#     print(i, end=" ")

'''Дано натуральное число. Требуется посчитать количество четных и нечетных
цифр в числе.'''

# n = int(input())
# even=odd=0
# while n>0:
#     if n%2 == 0:
#         even += 1
#     else:
#         odd += 1
#     n = n//10
# print("%d %d" % (even, odd))

'''Ввести натуральное число и определить, верно ли, что в его записи есть две
одинаковые цифры (не обязательно стоящие рядом).'''

# a = input()
# if len(a) == len(set(a)):
#     print("NO")
# else:
#     print("YES")