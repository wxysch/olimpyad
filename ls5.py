# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# if a % b == 0:
#    print(" Yes")
# else:
#   print("No")
# --------------------------------------------
# a = int(input(" Input Ђ amount ЂofЂ money :Ђ"))
# if a >= 120:
#    print (" Bread Ђand Ђ cheese ")
# elif a >= 100:
#    print (" Cheese Ђ only ")
# elif a >= 20:
#    print (" Bread Ђ only ")
# else:
#    print (" Nothing Ђ:(")
# -------------------------------------------------
# a=int(input("Введите ваш возраст"))
# if a<=7:
#    print('Вам в детский сад')
# elif a<=18 :
#    print("Вам в школу")
# elif a<=25:
##    print("Вам профиссиональное учебное заведение")
# elif a<=60 :
#    print("Вам на работу")
# elif a<=120:
#    print("Вам предоставляется выбор")
# else:
#    print("¾Ошибка! Это программа для людей!")
##-----------------------------------------------------------
# x = 12 - 5
# h1 = x == 4
# h2 = x == 7
# h3 = x != 7
# h4 = x != 4
# h5 = x > 5
# h6 = x < 5
# print (h1 , h2 , h3 , h4 , h5 , h6)
# -----------------------------------------------
# N=int(input("окуучунун саны :"))
# K=int(input("алма"))
# T=K // N
# C=N % K
# print(T)
# print(C)

# -------------------------------------------------------------
# A = int(input())
# a1=A//10
# a2=A%10
# print(a1+a2)
# -------------------------------
# a=int(input())
# a1=a//100
# a2=a%100//10
# a3=a%100%10
# print(a1,a2,a3 ,sep=",")
# ---------------------------------------------------------------
# a=int(input())
# a4=a//10
# a3=a//10%10
# a2=a//10//10
# a1=a
# print(a2,a3 ,4 ,sep=",")
# --------------------------------------------------------------------------------
# a1=int(input())
# a2=a1*a1
# a3=a2*a2
# a4=a3*a1
# a5=a4*a4
# print(a5)
# тик бурч катеттери гипатенузасын тапкыла
# -------------------------------------------------------------------------------

# from math import *
# a,b=map(float,input().split())
# c=sqrt((a**2)+(b**2))
# print(c)
# -=================================================================================================
# rom math import *

# Шахматная доска
# k=int(input())
# l=int(input())
# if (k+l)%2==0:
#	print("kara")
# else:
#	print("ak")
# =================================================================
# x=int(input())
# if x%2==0:
#	print(x+2)
# else:
#	print(x+1)
# -----------------------------------------------------------

# a,b,c=map(int,input().split())
# if a==b or b==c or c==a :
#	print("тен капталдуу")
# elif a==b==c:
#	print("тен жактуу")
# else:
#	print()
# ================================================================================
# сандардын удалаштыгын биринчи 0 деген санга чейин киргизгиле
# x=int(input())
# while x!=0:
#	print(x)
#	x=int(input())
# ====================================================================
# биринчи 4ко эселуу санга чейинки сандарды тапкыла
# s=0
# x=int(input())
# while x%4!=0:
#	s+=x
#	x=int(input())
# print(s)
# ----------------------------------------------------------------
# c=0
# x=int(input())
# while x>=0:
#	if x==0:
#		c+=1
#	x=int(input())
# print(c)
# n натуралдык саны берилди бул санды  туура киргизуучу
# f = True
# while f:
#    x = int(input("Эки орундуу сан киргиз: "))
#    if 9 < x < 100:
#        f = False
# s = x//10 + x%10
# print(s)
# ==============================================
# Вывести четные элементы списка.
# a=[int ( x ) for x in input ().split()]
# for i in a :
#	if i%2==0 and (i != 0):
#		print( i , end='')
# --------------------------------------------------
# Найти количество элементов списка кратных 3 и не кратных 5.
# t = [int(x) for x in input().split()]
# for k in t:
#    if k%3==0 and k%5!=0:
#        print(k, end=" ")
# -----------------------------------------------------
# Определить каких элементов больше в списке положительных или отрицательных.
# t= [int(x) for x in input().split()]
# a=0
# b=0

# for k in t:
#	if k>0:
#		a=a+1
#	if k<0:
#		b=b+1

# if a>b:
#	print("+")
# elif a<b:
#	print("-")
# else:
#	print("+,-")
# =============================================================
# Удалить из списка отрицательные элементы
# from random import random
# a = []
# for i in range(10):
#    n = int(random()*10) - 5
#    a.append(n)
# print(a)
# i = 0
# m = 10
# while i < m:
#    if a[i] < 0:
#        del a[i]
#        m -= 1
#    else:
#        i += 1
# print(a)
# -------------------------------------------------------------
# Поменять местами первый отрицательный и первый нулевой элементы.
# n = int(input('n='))
# t = []
# for i in range(n):
#    t.append(int(input()))
# print(t)
# k0 = t.index(0)

# for i in range(n):
#    if t[i] < 0:
#        kt = i
#        break
# t[k0],t[kt] = t[kt],t[k0]
# print(t)
# =============================================
# 6. Терс элементтердин көбөйтүндүсүн, он элементтердин суммасын тапкыла.
# t = [int(k) for k in input().split()]
# n = len(t)
# if n % 2 == 1:
#    n = n - 1
# for i in range(0,n,2):
#    t[i],t[i+1] = t[i+1],t[i]
# print(t)
# ============================================================
# x=[int(k) for k in input () . split()]
# y=[]
# for i in x :
#    if i % 3 == 0:
#        y.append(i)
# print(x)
# -=-=-=-=-==--=-=-==--==-=-=-=-=-=--=-=-=-=-=-==-=-=-=--==--=-=
# x=[int(x) for x in input () . split()]
# print(max(x))
# print(min(x))
# -----------------------------------------------
# тизменин элементеринин орточо арифметикалык маанисин тапкыла

# x=[int(t) for t in input () . split()]

# a1=max(x)
# a2=min(x)

# x.remove(a1)
# x.remove(a2)
# c=sum(x)/len(x)
# print(c)
# ----------------------------------------------------------------
# x=int(input())
# y=int(input())
# c=(y-x)/2
# print(c+x)
# --------------------------------------------------------------------
# maxab=
# a,b=map(int,input().split())
# if a>b:
#    print(a)
# else:
#    print(b)
# ------------------------------------------------------------------
# a=[[12,3,5],[-3, 76],[49,-5,0,75,3]]
# s=0
# for i in a:
#    for j in i:
#        s+=j
# print(s)
# -------------------------------------------------------------------
# from random import randint
# x = [[randint(-1,1)*randint(1,100) for j in range(4)] for i in range(3)]
# print(x)
# y=[]
# for i in x:
#    y.append(max(i))
# print(max(y))
# -------------------------------------------------------------------------
# from random import randint
# x = [[randint(-1,1)*randint(1,100) for j in range(4)] for i in range(3)]
# print(x)
# s=0
# for i in x:
#   print(sum(i))
# -----------------------------------------------------------------------------
# from random import randint
# x = [[randint(-1,1)*randint(1,9) for j in range(4)] for i in range(3)]
# print(x)

# for i in range(3):
#    s= 0
#    for j in range(4):
#        s += x[i][j]
#    print(s,end=" ")
# ------------------------------------------------------------------------------
# from random import randint
# x = [[randint(-1,1)*randint(1,9) for j in range(4)] for i in range(3)]
# print(x)

# for j in range(3):
#    s= 0
#    for i in range(4):
#        s += x[j][i]
#    print(s/3,2,end=" ")
# --------------------------------------------------------
# Графика
# from turtle import *
# shape("turtle")
# speed(1)
# color("#b00","#00f")
# begin_fill()
# for i in range(4):
#    bk(200)
#    right(90)
# end_fill()
# left(90)
# color("#A259FF","#ff0")
# begin_fill()
# for i in range(4):
#    bk(200)
#    left(90)
# end_fill()
# left(45)
# fd(285)
# bk(570)
# ======================================================================================================
# from turtle import *
# shape("turtle")
# speed(1)
# color("#b00","#00f")
# begin_fill()
# up()
# goto(-300, 100)
# down()
# left(70)
# fd(160)
# left(220)
# fd(160)
# bk(60)
# left(250)
# fd(70)
# up()
# goto(-150, 100)
# down()
# left(270)
# fd(150)
# right(90)
# fd(80)
# right(90)
# fd(150)
# up()
# goto(-30, 100)
# down()
# left(160)
# fd(160)
# left(220)
# fd(160)
# bk(60)
# left(250)
# fd(70)
# fd(160)

# ----------------------------------------------------------------------------------------
# a=int(input())
# b=int(input())
# if a<b:
#    print("<")
# elif a>b:
#    print(">")
# else:
#    print("=")
# -----------------------------------------------------------
# N,M,K=map(int,input().split())
# a=N*M
# if a>=K:
#    print("+")
# else:
#    print("-")
# --------------------------------
# a,b,c=map(int,input().split())
# print(a*b*c*2)
# -------------------------------
# k,m=map(int,input().split())
# print(k*k*m)
# --------------------------------
# a,b=map(int,input().split())
# c=a+b-1
# print(c-a,c-b)
# -----------------------------
# a,e=map(int,input().split())
# b,f=map(int,input().split())
# c,g=map(int,input().split())
# d,h=map(int,input().split())
# x=a+b+c+d
# y=e+f+g+h
# if x>y:
#    print("1")
# elif x<y:
#    print("2")
# else:
#    print("DRAW")
# -----------------------------
# X,Y,Z=map(int,input().split())
# a=X+Y-Z
# if a>Z:
#    print(a)
# else:
#    print("Impossible")
# --------------------------------------
# S=int(input())
# c=S/6
# d=S/6*4
# f=S/6
# print(int(c),int(d),int(f))
# --------------------------------------
# M1,M2, M3 =map(int,input().split())
# if M1>=94 and M1<=727 and M2>=94 and M2<=727  and M3>=94 and M3<=727:
#    print(max(M1,M2,M3))
# else :
#    print("Error")
# -------------------------------------
# a=int(input())
# if a%2==0:
#    print("Yes")
# else:
#    print("No")
# ---------------------
# W,H,R=map(int,input().split())
# d=R*2
# if d<=W and d<=H:
#    print("yes")
# else:
#    print("No")
# --------------------------------
# a=int(input())
# b=int(input())
# q=0
# for  a in range (a,b+1):
#    print(a)
#    q=q+1
# print("кол чисел",q)
# -------------------
# b=int(input())
# stoi=0
# for a in range(1,11):
#        stoi=b*a
#        print("stoi :",a,"кг = ",stoi)
# _------------------------------------------
# a=int(input())
# su=0
# for a in range(1,a+1):
#    b=int(input())
#    if  b<0:
#        su=su+b
# print("sum =",su)
# -------------------------------
# q=0
# a=int(input())
# if a>0:
#    q=q+1
# a=int(input())
# if a>0:
#    q=q+1
# a=int(input())
# if a>0:
#    q=q+1
# print(q)
# -----------------------
# a=int(input())
# if a>0:
#    print(a+1)
# else:
#    print(a-2)
# ----------------------
# a=int(input())
# print(a*100/30)
# ________________________________
# a=int(input())
# q=0
# for b in range(0,a):
#    a=int(input())
#    if a%6==0 and a%10==4:
#        q=q+1
# print(q)
# ------------------------------
# x=int(input())
# y=int(input())
# c=(y-x)/2
# print(c+x)
# ______________________________________

# x = int(input('Введите X:'))
# y = int(input('Введитe Y:'))
# print((y*3)-(x*2))

# ____________________________________

# user = input('Введи буквы: ')
# for i in range(len(user) + 1):
#    print(user[:i])
# _______________________________________
# a=int(input())
# if a%2!=0:
#    print("3")
# else:
#    print("2")
# ________________________________________________
# a=int(input())
# if a==12 or a==1 or a==2:
#    print("Winter")
# elif a==3  or a==4 or a==5:
#    print("Spring")
# elif a==6  or a==7 or a==8:
#    print("Summer")
# elif a==9  or a==10 or a==11:
#    print("Autumn")
# else:
#    print("Error")
# ----------------------------------------------
# a=float(input("Com ="))
# print("Dollar =",a*0.012)
# print("Euro =",a*0.010)
# ==================
# a=23
# print(a%1.5)
# print(a%2)#
# _________________________________________
# a1,a2,a3=map(int,input().split())
# b=a1+a2
# c=a2+a3
# d=a1+a3
# if b==a3:
#    print("YES")
# elif c==a1:
#    print("YES")
# elif d==a2:
#    print("YES")
# else:
#    print("NO")
# ____________________________________
# a = map(int,input().split())
# for a in range(0,a):
#    a=input()
#    print(a[::-1])
# ----------------------------------------------------------
# a,b,c=map(int,input().split())
# print(a*b*c*2)
# _________________________
# a=int(input())
# su=0
# q=0
# while a!=0:
#    if a%2==0:
#        su=su+a
#    q=q+1
#    a=int(input())
# print(q)
# print(su)
# _____________________________
# a=int(input())
# q=[0]*a
# s=0
# for i in range(a):
#    q[i]=int(input())
#    s=s+q[i]
# print(q)
# print(s)
# --------------------------
# import random
# a=int(input())
# x=int(input())
# y=int(input())
# q=[0]*a
# for i in range (a):
#    q[i]= random.randint(x,y)
# q.sort()
# rint(q)
# ______________________________
# st=input()
# c="о"
# count=0
# for i in st:
#    if i==c:
#        count=count+1
# print(count)
# ------------------------------
# import random
# n=int(input())
# ch=[0]*n
# for i in range(n):
#    ch[i]=random.randint(1,100)
# print(ch)
# print(max(ch))
# print(min(ch))
# -------------------------------
# X,Y,Z=map(int,input().split())
# if X+Y<Z:
#    print("Impossible")
# else:
#    print(X+Y-Z)
# ---------------------------------
# Tort
# n=int(input())#
# if n>=1:
#    if n%2==0:
#        print(int(n/2))
#    if n%2!=0:
#        print(int(n))
# else:
#    print("0")
# --------------------
# a=int(input())
# c=0
# for i in range(0,a):
#    b=int(input())
#    c+=b
# if c<=a/2:
##    print(c)
# else:
#     print(a-c)
# ---------------
# a=int(input())
# c=0
# for i in range(0,a):
#   b=int(input())
# print(b.count("0"))
# ______________________________
# a1,a2,a3,b1,b2,b3=map(int,input().split())
# if a1<a2:
#    c=a1
#    a1=a2
#    a2=c
# if a2<a3:
#    c=a2
#    a2=a3
#    a3=c
# if a1<a2:
#    c=a1
#    a1=a2
#    a2=c
# if b1<b2:
#    c=b1
#    b1=b2
#    b2=c
# if b2<b3:
#    c=b2
#    b2=b3
#    b3=c
# if b1<b2:
#    c=b1
#    b1=b2
#    b2=c
# else:
#    print(a1*b1+a2*b2+a3*b3)
# __________________________________
#
# a,b,c=map(int,input().split())
# print(2*(a*b+a*c+b*c),a*b*c)
# _________________________________
#
# M,N=map(int,input().split())
# print((M-1)*(N-1))
# ___________________
# c,h,o=map(int,input().split())
# c/=2
# h/=6
# print(int(min(c,h,o)))
# -----------------------------------
# n=int(input())
# m2=[]
# for i in range(0,n) :
#    m=(input().split(" "))
#    m2.append(int(m))
# max1=max(m2)
# min2=min(m2)
# m3=[]
# for i in range (min1,max1+2,2):
#    if i>max1:
#        break
#    else:
#        m3.append(i)
# h=[]
# for i in m2:
#   if i!=min1:
#       h.append(i)
#    min1+=2
# set1=set(m3)
# set2=set(m2)
# list1=list(set1.difference(set2))
# if not list1:
#    print(*h)
# elif not h:
#    print(*list1)

# ____________________________________________
# input()
# a=list(map(int,input().split()))
# b=[]
# c=[]
# for i in a:
#    if i%2==0:
#        b.append(i)
#    else:
#        c.append(i)
# print(*c)
# print(*b)
# if len(b)>=len(c):
#    print("YES")
# else:
#    print("NO")
# -------------------------------------
# a,b,c,d=list(map(int,input().split()))
# b=[]
# for i in range(-100,100):
#    if a[0]*x**3+a[1]*x**2+a[2]*x+a[3]==0:
#        b.append(x)
# print(*b)
# __________________________________
# from math import *
# a,b=map(int,input().split())
# print(int(a*b/gcd(a,b)))
# ______________________________________
# a=input()
# if (a=="q") :
#    print("w")
# elif a=="w" :
#    print("e")
# elif a=="e" :
#    print("r")
# elif a=="r" :
#    print("t")
# elif a=="t" :
#    print("y")
# elif a=="y" :
#    print("u")
# elif a=="u" :
#    print("i")
# elif a=="i" :
#    print("o")
# elif a=="o" :
#    print("p")
# elif a=="p" :
#    print("a")
# elif a=="a" :
#    print("s")
# elif a=="s" :
#    print("d")
# elif a=="d" :
#    print("f")
# elif a=="f" :
#    print("g")
# elif a=="g" :
#    print("h")
# elif a=="h" :
#    print("j")
# elif a=="j" :
#    print("k")
# elif a=="k" :
#    print("l")
# elif a=="l" :
#    print("z")
# elif a=="z" :
#    print("x")
# elif a=="x" :
#    print("c")
# elif a=="c" :
#    print("v")
# elif a=="v" :
#    print("b")
# elif a=="b" :
#    print("n")
# elif a=="n" :
#    print("m")
# elif a=="m" :
#    print("q")
# ______________________________________________________________
# a=int(input())
# y=0
# for i in range(a):
#    x=int(input())
#    y+=x
# y=y/a
# print(str(y))
# ------------------------------------------------------------------------------
# a=int(input())
# if a>=10000:
#    print("yes")
# else:
#    print("No")
# _____________
# ____________________________________

# b=[]
# for i in range(int(input())):
#    a=list(map(int,input().split()))
#    b.append(sum(a))
# print(sum(b)//2)
# ____________________________________
# a=int(input())
# for i in range(a):
#    a=int(input())
#    a+=1
# print(a)

# __________________________________________________
# a=int(input())
# if a<=10000:
#    print("no")
# else:
#    print("yes")
# _________________________
# a=input()
# for i in range(len(a)+1):
#    print(a[:i])
# _________________________________________________

# n=int(input())
# for i in n:
#    n=list(map(int,input().split()))#
# )))))))))))))))))))))))))))))))))|
# s=int(input())
# minu=s//60
# sec=s%60
# print(minu,sec)
# __________________________________________
# s=int(input())
# hours=s//3600
# minu=s%3600//60
# sec=s%3600%60
# print(hours,minu,sec)
# ______________________________
# l,w,h=map(int,input().split())
# s=2*(h*l+h*w)
# if s%16==0:
#    print(int(s/16))
# else:
#    print(int(s/16+1))
# ________________________________________________________________________________________________________________________________________________
# s,t=map(int,input().split())#
# if t > s:
#    print(t-s)
# else:
#    print(12-s+t)
# ____________________________
# def kubik(n):
#    a=[1]+[0]*n
#    for i in range (1,n+1):
#        for j in range(n,i-1,-1):
#            a[j]+=a[j-i]

#    return a[n]
# print(kubik(int(input())))
# _____________________________
# a=int(input())
# if a[0]+a[1]+a[2]==a[3]+a[4]+a[5]:
#    print("YES")
# else:
#    print("NO")
# ___________________________________________________________________________________________
# from math import*
# x1,y1,x2,y2=map(int,input().split())
# c1=x2-x1
# c2=y2-y1
# c=c1*c1+c2*c2
# s=sqrt(c)
# print(s)
# ________________________________________
# tr,tc=map(int,input().split())
# name=input()
# if name=="freeze":
#    print(min(tr,tc))
# elif name=="heat":
#    print(max(tr,tc))
# elif name=="auto":
#    print(tc)
# elif name=="fan":
#    print(tr)
# ________________________
# a,b,c,t=map(int,input().split())
# if t<=a:
#    print(t*b)
# else:
#    print(a*b+(t-a)*c)
# ____________________________
# n = int(input())
# i = 1
# while i ** 2 <= n:
#    print(i ** 2)
#    i += 1
# ________________________________________
# k=int(input())
# s="GCV"
# for i in range(i,k):
# _______________________________________________
# """ zada4a "A"
# import math
# xa,ya=map(int,input().split())
# xb,yb=map(int,input().split())
# xk,yk=map(int,input().split())
# adil=math.sqrt((xa-xk)*(xa-xk)+(ya-yk)*(ya-yk))
# bael = math.sqrt((xb - xk) * (xb - xk) + (yb - yk) * (yb - yk))
# if adil>bael:
#    print("Bayel")
# elif bael > adil:
#    print("Adil")
# else:
#    print("Adil and Bayel")
"""______________________________________________________________________
#zada4a "B"
#n,m=map(int,input().split())
#for i in n:
#    for j in m:
#        n=int(input())
#        m=list(map(int,input().split()))
#______________________________________
#zada4a "C"
#n,m=map(int,input().split())
#a=n+m
#if n>0:
#    print(n+m)
#else:
#    if a<=-1:
#        print(n+m)
#    else:
#        print(a+1)
__________________________"""
'''a,b=map(int,input().split())
c=a+b
print(c)
__________________________________________________'''
# a,b=map(int,input().split())
# q=0
# for c in range(0,a):
#    a,b=list(map(int,input().split()))
#    q=q=1
# ______________________________
name = input()
c = "o"
nym = 0
for i in name:
    if i == c:
        nym += 1
print(nym)#a = int(input('Введите первое число: '))
#b = int(input('Введите второе число: '))
#if a % b == 0:
#    print(" Yes")
#else:
 #   print("No")
#--------------------------------------------
#a = int(input(" Input Ђ amount ЂofЂ money :Ђ"))
#if a >= 120:
#    print (" Bread Ђand Ђ cheese ")
#elif a >= 100:
#    print (" Cheese Ђ only ")
#elif a >= 20:
#    print (" Bread Ђ only ")
#else:
#    print (" Nothing Ђ:(")
#-------------------------------------------------
#a=int(input("Введите ваш возраст"))
#if a<=7:
#    print('Вам в детский сад')
#elif a<=18 :
#    print("Вам в школу")
#elif a<=25:
##    print("Вам профиссиональное учебное заведение")
#elif a<=60 :
#    print("Вам на работу")
#elif a<=120:
#    print("Вам предоставляется выбор")
#else:
#    print("¾Ошибка! Это программа для людей!")
##-----------------------------------------------------------
#x = 12 - 5
#h1 = x == 4
#h2 = x == 7
#h3 = x != 7
#h4 = x != 4
#h5 = x > 5
#h6 = x < 5
#print (h1 , h2 , h3 , h4 , h5 , h6)
#-----------------------------------------------
#N=int(input("окуучунун саны :"))
#K=int(input("алма"))
#T=K // N
#C=N % K
#print(T)
#print(C)

#-------------------------------------------------------------
#A = int(input())
#a1=A//10
#a2=A%10
#print(a1+a2)
#-------------------------------
#a=int(input())
#a1=a//100
#a2=a%100//10
#a3=a%100%10
#print(a1,a2,a3 ,sep=",")
#---------------------------------------------------------------
#a=int(input())
#a4=a//10
#a3=a//10%10
#a2=a//10//10
#a1=a
#print(a2,a3 ,4 ,sep=",")
#--------------------------------------------------------------------------------
#a1=int(input())
#a2=a1*a1
#a3=a2*a2
#a4=a3*a1
#a5=a4*a4
#print(a5)
#тик бурч катеттери гипатенузасын тапкыла
#-------------------------------------------------------------------------------

#from math import *
#a,b=map(float,input().split())
#c=sqrt((a**2)+(b**2))
#print(c)
#-=================================================================================================
#rom math import *

#Шахматная доска
#k=int(input())
#l=int(input())
#if (k+l)%2==0:
#	print("kara")
#else:
#	print("ak")
#=================================================================
#x=int(input())
#if x%2==0:
#	print(x+2)
#else:
#	print(x+1)
#-----------------------------------------------------------

#a,b,c=map(int,input().split())
#if a==b or b==c or c==a :
#	print("тен капталдуу")
#elif a==b==c:
#	print("тен жактуу")
#else:
#	print()
#================================================================================
#сандардын удалаштыгын биринчи 0 деген санга чейин киргизгиле
#x=int(input())
#while x!=0:
#	print(x)
#	x=int(input())
#====================================================================
#биринчи 4ко эселуу санга чейинки сандарды тапкыла
#s=0
#x=int(input())
#while x%4!=0:
#	s+=x
#	x=int(input())
#print(s)
#----------------------------------------------------------------
#c=0
#x=int(input())
#while x>=0:
#	if x==0:
#		c+=1
#	x=int(input())
#print(c)
#n натуралдык саны берилди бул санды  туура киргизуучу
#f = True
#while f:
#    x = int(input("Эки орундуу сан киргиз: "))
#    if 9 < x < 100:
#        f = False
#s = x//10 + x%10
#print(s)
#==============================================
#Вывести четные элементы списка.
#a=[int ( x ) for x in input ().split()]
#for i in a :
#	if i%2==0 and (i != 0):
#		print( i , end='')
#--------------------------------------------------
#Найти количество элементов списка кратных 3 и не кратных 5.
#t = [int(x) for x in input().split()]
#for k in t:
#    if k%3==0 and k%5!=0:
#        print(k, end=" ")
#-----------------------------------------------------
#Определить каких элементов больше в списке положительных или отрицательных.
#t= [int(x) for x in input().split()]
#a=0
#b=0

#for k in t:
#	if k>0:
#		a=a+1
#	if k<0:
#		b=b+1

#if a>b:
#	print("+")
#elif a<b:
#	print("-")
#else:
#	print("+,-")
#=============================================================
#Удалить из списка отрицательные элементы
#from random import random
#a = []
#for i in range(10):
#    n = int(random()*10) - 5
#    a.append(n)
#print(a)
#i = 0
#m = 10
#while i < m:
#    if a[i] < 0:
#        del a[i]
#        m -= 1
#    else:
#        i += 1
#print(a)
#-------------------------------------------------------------
#Поменять местами первый отрицательный и первый нулевой элементы.
#n = int(input('n='))
#t = []
#for i in range(n):
#    t.append(int(input()))
#print(t)
#k0 = t.index(0)

#for i in range(n):
#    if t[i] < 0:
#        kt = i
#        break
#t[k0],t[kt] = t[kt],t[k0]
#print(t)
#=============================================
#6. Терс элементтердин көбөйтүндүсүн, он элементтердин суммасын тапкыла.
#t = [int(k) for k in input().split()]
#n = len(t)
#if n % 2 == 1:
#    n = n - 1
#for i in range(0,n,2):
#    t[i],t[i+1] = t[i+1],t[i]
#print(t)
#============================================================
#x=[int(k) for k in input () . split()]
#y=[]
#for i in x :
#    if i % 3 == 0:
#        y.append(i)
#print(x)
#-=-=-=-=-==--=-=-==--==-=-=-=-=-=--=-=-=-=-=-==-=-=-=--==--=-=
#x=[int(x) for x in input () . split()]
#print(max(x))
#print(min(x))
#-----------------------------------------------
#тизменин элементеринин орточо арифметикалык маанисин тапкыла

#x=[int(t) for t in input () . split()]

#a1=max(x)
#a2=min(x)

#x.remove(a1)
#x.remove(a2)
#c=sum(x)/len(x)
#print(c)
#----------------------------------------------------------------
#x=int(input())
#y=int(input())
#c=(y-x)/2
#print(c+x)
#--------------------------------------------------------------------
#maxab=
#a,b=map(int,input().split())
#if a>b:
#    print(a)
#else:
#    print(b)
#------------------------------------------------------------------
#a=[[12,3,5],[-3, 76],[49,-5,0,75,3]]
#s=0
#for i in a:
#    for j in i:
#        s+=j
#print(s)
#-------------------------------------------------------------------
#from random import randint
#x = [[randint(-1,1)*randint(1,100) for j in range(4)] for i in range(3)]
#print(x)
#y=[]
#for i in x:
#    y.append(max(i))
#print(max(y))
#-------------------------------------------------------------------------
#from random import randint
#x = [[randint(-1,1)*randint(1,100) for j in range(4)] for i in range(3)]
#print(x)
#s=0
#for i in x:
#   print(sum(i))
#-----------------------------------------------------------------------------
#from random import randint
#x = [[randint(-1,1)*randint(1,9) for j in range(4)] for i in range(3)]
#print(x)

#for i in range(3):
#    s= 0
#    for j in range(4):
#        s += x[i][j]
#    print(s,end=" ")
#------------------------------------------------------------------------------
#from random import randint
#x = [[randint(-1,1)*randint(1,9) for j in range(4)] for i in range(3)]
#print(x)

#for j in range(3):
#    s= 0
#    for i in range(4):
#        s += x[j][i]
#    print(s/3,2,end=" ")
#--------------------------------------------------------
#Графика
#from turtle import *
#shape("turtle")
#speed(1)
#color("#b00","#00f")
#begin_fill()
#for i in range(4):
#    bk(200)
#    right(90)
#end_fill()
#left(90)
#color("#A259FF","#ff0")
#begin_fill()
#for i in range(4):
#    bk(200)
#    left(90)
#end_fill()
#left(45)
#fd(285)
#bk(570)
#======================================================================================================
#from turtle import *
#shape("turtle")
#speed(1)
#color("#b00","#00f")
#begin_fill()
#up()
#goto(-300, 100)
#down()
#left(70)
#fd(160)
#left(220)
#fd(160)
#bk(60)
#left(250)
#fd(70)
#up()
#goto(-150, 100)
#down()
#left(270)
#fd(150)
#right(90)
#fd(80)
#right(90)
#fd(150)
#up()
#goto(-30, 100)
#down()
#left(160)
#fd(160)
#left(220)
#fd(160)
#bk(60)
#left(250)
#fd(70)
#fd(160)

#----------------------------------------------------------------------------------------
#a=int(input())
#b=int(input())
#if a<b:
#    print("<")
#elif a>b:
#    print(">")
#else:
#    print("=")
#-----------------------------------------------------------
#N,M,K=map(int,input().split())
#a=N*M
#if a>=K:
#    print("+")
#else:
#    print("-")
#--------------------------------
#a,b,c=map(int,input().split())
#print(a*b*c*2)
#-------------------------------
#k,m=map(int,input().split())
#print(k*k*m)
#--------------------------------
#a,b=map(int,input().split())
#c=a+b-1
#print(c-a,c-b)
#-----------------------------
#a,e=map(int,input().split())
#b,f=map(int,input().split())
#c,g=map(int,input().split())
#d,h=map(int,input().split())
#x=a+b+c+d
#y=e+f+g+h
#if x>y:
#    print("1")
#elif x<y:
#    print("2")
#else:
#    print("DRAW")
#-----------------------------
#X,Y,Z=map(int,input().split())
#a=X+Y-Z
#if a>Z:
#    print(a)
#else:
#    print("Impossible")
#--------------------------------------
#S=int(input())
#c=S/6
#d=S/6*4
#f=S/6
#print(int(c),int(d),int(f))
#--------------------------------------
#M1,M2, M3 =map(int,input().split())
#if M1>=94 and M1<=727 and M2>=94 and M2<=727  and M3>=94 and M3<=727:
#    print(max(M1,M2,M3))
#else :
#    print("Error")
#-------------------------------------
#a=int(input())
#if a%2==0:
#    print("Yes")
#else:
#    print("No")
#---------------------
#W,H,R=map(int,input().split())
#d=R*2
#if d<=W and d<=H:
#    print("yes")
#else:
#    print("No")
#--------------------------------
#a=int(input())
#b=int(input())
#q=0
#for  a in range (a,b+1):
#    print(a)
#    q=q+1
#print("кол чисел",q)
#-------------------
#b=int(input())
#stoi=0
#for a in range(1,11):
#        stoi=b*a
#        print("stoi :",a,"кг = ",stoi)
#_------------------------------------------
#a=int(input())
#su=0
#for a in range(1,a+1):
#    b=int(input())
#    if  b<0:
#        su=su+b
#print("sum =",su)
#-------------------------------
#q=0
#a=int(input())
#if a>0:
#    q=q+1
#a=int(input())
#if a>0:
#    q=q+1
#a=int(input())
#if a>0:
#    q=q+1
#print(q)
#-----------------------
#a=int(input())
#if a>0:
#    print(a+1)
#else:
#    print(a-2)
#----------------------
#a=int(input())
#print(a*100/30)
#________________________________
#a=int(input())
#q=0
#for b in range(0,a):
#    a=int(input())
#    if a%6==0 and a%10==4:
#        q=q+1
#print(q)
#------------------------------
#x=int(input())
#y=int(input())
#c=(y-x)/2
#print(c+x)
#______________________________________

#x = int(input('Введите X:'))
#y = int(input('Введитe Y:'))
#print((y*3)-(x*2))

#____________________________________

#user = input('Введи буквы: ')
#for i in range(len(user) + 1):
#    print(user[:i])
#_______________________________________
#a=int(input())
#if a%2!=0:
#    print("3")
#else:
#    print("2")
#________________________________________________
#a=int(input())
#if a==12 or a==1 or a==2:
#    print("Winter")
#elif a==3  or a==4 or a==5:
#    print("Spring")
#elif a==6  or a==7 or a==8:
#    print("Summer")
#elif a==9  or a==10 or a==11:
#    print("Autumn")
#else:
#    print("Error")
#----------------------------------------------
#a=float(input("Com ="))
#print("Dollar =",a*0.012)
#print("Euro =",a*0.010)
#==================
#a=23
#print(a%1.5)
#print(a%2)#
#_________________________________________
#a1,a2,a3=map(int,input().split())
#b=a1+a2
#c=a2+a3
#d=a1+a3
#if b==a3:
#    print("YES")
#elif c==a1:
#    print("YES")
#elif d==a2:
#    print("YES")
#else:
#    print("NO")
#____________________________________
#a = map(int,input().split())
#for a in range(0,a):
#    a=input()
#    print(a[::-1])
#----------------------------------------------------------
#a,b,c=map(int,input().split())
#print(a*b*c*2)
#_________________________
#a=int(input())
#su=0
#q=0
#while a!=0:
#    if a%2==0:
#        su=su+a
#    q=q+1
#    a=int(input())
#print(q)
#print(su)
#_____________________________
#a=int(input())
#q=[0]*a
#s=0
#for i in range(a):
#    q[i]=int(input())
#    s=s+q[i]
#print(q)
#print(s)
#--------------------------
#import random
#a=int(input())
#x=int(input())
#y=int(input())
#q=[0]*a
#for i in range (a):
#    q[i]= random.randint(x,y)
#q.sort()
#rint(q)
#______________________________
#st=input()
#c="о"
#count=0
#for i in st:
#    if i==c:
#        count=count+1
#print(count)
#------------------------------
#import random
#n=int(input())
#ch=[0]*n
#for i in range(n):
#    ch[i]=random.randint(1,100)
#print(ch)
#print(max(ch))
#print(min(ch))
#-------------------------------
#X,Y,Z=map(int,input().split())
#if X+Y<Z:
#    print("Impossible")
#else:
#    print(X+Y-Z)
#---------------------------------
#Tort
#n=int(input())#
#if n>=1:
#    if n%2==0:
#        print(int(n/2))
#    if n%2!=0:
#        print(int(n))
#else:
#    print("0")
#--------------------
#a=int(input())
#c=0
#for i in range(0,a):
#    b=int(input())
#    c+=b
#if c<=a/2:
##    print(c)
#else:
#     print(a-c)
#---------------
#a=int(input())
#c=0
#for i in range(0,a):
 #   b=int(input())
#print(b.count("0"))
#______________________________
#a1,a2,a3,b1,b2,b3=map(int,input().split())
#if a1<a2:
#    c=a1
#    a1=a2
#    a2=c
#if a2<a3:
#    c=a2
#    a2=a3
#    a3=c
#if a1<a2:
#    c=a1
#    a1=a2
#    a2=c
#if b1<b2:
#    c=b1
#    b1=b2
#    b2=c
#if b2<b3:
#    c=b2
#    b2=b3
#    b3=c
#if b1<b2:
#    c=b1
#    b1=b2
#    b2=c
#else:
#    print(a1*b1+a2*b2+a3*b3)
#__________________________________
#
#a,b,c=map(int,input().split())
#print(2*(a*b+a*c+b*c),a*b*c)
#_________________________________
#
#M,N=map(int,input().split())
#print((M-1)*(N-1))
#___________________
#c,h,o=map(int,input().split())
#c/=2
#h/=6
#print(int(min(c,h,o)))
#-----------------------------------
#n=int(input())
#m2=[]
#for i in range(0,n) :
#    m=(input().split(" "))
#    m2.append(int(m))
#max1=max(m2)
#min2=min(m2)
#m3=[]
#for i in range (min1,max1+2,2):
#    if i>max1:
#        break
#    else:
#        m3.append(i)
#h=[]
#for i in m2:
#   if i!=min1:
 #       h.append(i)
#    min1+=2
#set1=set(m3)
#set2=set(m2)
#list1=list(set1.difference(set2))
#if not list1:
#    print(*h)
#elif not h:
#    print(*list1)

#____________________________________________
#input()
#a=list(map(int,input().split()))
#b=[]
#c=[]
#for i in a:
#    if i%2==0:
#        b.append(i)
#    else:
#        c.append(i)
#print(*c)
#print(*b)
#if len(b)>=len(c):
#    print("YES")
#else:
#    print("NO")
#-------------------------------------
#a,b,c,d=list(map(int,input().split()))
#b=[]
#for i in range(-100,100):
#    if a[0]*x**3+a[1]*x**2+a[2]*x+a[3]==0:
#        b.append(x)
#print(*b)
#__________________________________
#from math import *
#a,b=map(int,input().split())
#print(int(a*b/gcd(a,b)))
#______________________________________
#a=input()
#if (a=="q") :
#    print("w")
#elif a=="w" :
#    print("e")
#elif a=="e" :
#    print("r")
#elif a=="r" :
#    print("t")
#elif a=="t" :
#    print("y")
#elif a=="y" :
#    print("u")
#elif a=="u" :
#    print("i")
#elif a=="i" :
#    print("o")
#elif a=="o" :
#    print("p")
#elif a=="p" :
#    print("a")
#elif a=="a" :
#    print("s")
#elif a=="s" :
#    print("d")
#elif a=="d" :
#    print("f")
#elif a=="f" :
#    print("g")
#elif a=="g" :
#    print("h")
#elif a=="h" :
#    print("j")
#elif a=="j" :
#    print("k")
#elif a=="k" :
#    print("l")
#elif a=="l" :
#    print("z")
#elif a=="z" :
#    print("x")
#elif a=="x" :
#    print("c")
#elif a=="c" :
#    print("v")
#elif a=="v" :
#    print("b")
#elif a=="b" :
#    print("n")
#elif a=="n" :
#    print("m")
#elif a=="m" :
#    print("q")
#______________________________________________________________
#a=int(input())
#y=0
#for i in range(a):
#    x=int(input())
#    y+=x
#y=y/a
#print(str(y))
#------------------------------------------------------------------------------
#a=int(input())
#if a>=10000:
#    print("yes")
#else:
#    print("No")
#_____________
#____________________________________

#b=[]
#for i in range(int(input())):
#    a=list(map(int,input().split()))
#    b.append(sum(a))
#print(sum(b)//2)
#____________________________________
#a=int(input())
#for i in range(a):
#    a=int(input())
#    a+=1
#print(a)

#__________________________________________________
#a=int(input())
#if a<=10000:
#    print("no")
#else:
#    print("yes")
#_________________________
#a=input()
#for i in range(len(a)+1):
#    print(a[:i])
#_________________________________________________

#n=int(input())
#for i in n:
#    n=list(map(int,input().split()))#
#)))))))))))))))))))))))))))))))))|
#s=int(input())
#minu=s//60
#sec=s%60
#print(minu,sec)
#__________________________________________
#s=int(input())
#hours=s//3600
#minu=s%3600//60
#sec=s%3600%60
#print(hours,minu,sec)
#______________________________
#l,w,h=map(int,input().split())
#s=2*(h*l+h*w)
#if s%16==0:
#    print(int(s/16))
#else:
#    print(int(s/16+1))
#________________________________________________________________________________________________________________________________________________
#s,t=map(int,input().split())#
#if t > s:
#    print(t-s)
#else:
#    print(12-s+t)
#____________________________
#def kubik(n):
#    a=[1]+[0]*n
#    for i in range (1,n+1):
#        for j in range(n,i-1,-1):
#            a[j]+=a[j-i]

#    return a[n]
#print(kubik(int(input())))
#_____________________________
#a=int(input())
#if a[0]+a[1]+a[2]==a[3]+a[4]+a[5]:
#    print("YES")
#else:
#    print("NO")
#___________________________________________________________________________________________
#from math import*
#x1,y1,x2,y2=map(int,input().split())
#c1=x2-x1
#c2=y2-y1
#c=c1*c1+c2*c2
#s=sqrt(c)
#print(s)
#________________________________________
#tr,tc=map(int,input().split())
#name=input()
#if name=="freeze":
#    print(min(tr,tc))
#elif name=="heat":
#    print(max(tr,tc))
#elif name=="auto":
#    print(tc)
#elif name=="fan":
#    print(tr)
#________________________
#a,b,c,t=map(int,input().split())
#if t<=a:
#    print(t*b)
#else:
#    print(a*b+(t-a)*c)
#____________________________
#n = int(input())
#i = 1
#while i ** 2 <= n:
#    print(i ** 2)
#    i += 1
#________________________________________
#k=int(input())
#s="GCV"
#for i in range(i,k):
#_______________________________________________
#""" zada4a "A"
#import math
#xa,ya=map(int,input().split())
#xb,yb=map(int,input().split())
#xk,yk=map(int,input().split())
#adil=math.sqrt((xa-xk)*(xa-xk)+(ya-yk)*(ya-yk))
#bael = math.sqrt((xb - xk) * (xb - xk) + (yb - yk) * (yb - yk))
#if adil>bael:
#    print("Bayel")
#elif bael > adil:
#    print("Adil")
#else:
#    print("Adil and Bayel")
"""______________________________________________________________________
#zada4a "B"
#n,m=map(int,input().split())
#for i in n:
#    for j in m:
#        n=int(input())
#        m=list(map(int,input().split()))
#______________________________________
#zada4a "C"
#n,m=map(int,input().split())
#a=n+m
#if n>0:
#    print(n+m)
#else:
#    if a<=-1:
#        print(n+m)
#    else:
#        print(a+1)
__________________________"""
'''a,b=map(int,input().split())
c=a+b
print(c)
__________________________________________________'''
#a,b=map(int,input().split())
#q=0
#for c in range(0,a):
#    a,b=list(map(int,input().split()))
#    q=q=1
#______________________________
name=input()
c="o"
nym=0
for i in name:
    if i == c:
        nym+=1
print(nym)