## Given an integer, print "odd" if it's odd and print "even" otherwise.

a = int(input())

if a%2 ==1:
  print("odd")
else:
  print("even")





## Given the two integers, print the least of them.

a = int(input())
b = int(input())

if a>b:
  print(b)
else:
  print(a)




## For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
## Try to use the cascade if-elif-else for it.

X = int(input())

if X<0:
  print(-1)
  
elif X==0:
  print(0)
  
else:
  print(1)





## Given an integer, print "YES" if it's a three-digit number and print "NO" otherwise.

a = int(input())

if a>=100 and a<1000:
  print("YES")
else:
  print("NO")





## Given two non-zero integers, print "YES" if exactly one of them is positive and print "NO" otherwise.

a = int(input())
b = int(input())

if (a>0 and b<0) or (a<0 and b>0):
  print("YES")

else:
  print("NO")





## Given a three-digit integer X consisting of three different digits, print "YES" if its three digits are going in an ascending order from left to right and print "NO" otherwise.

a =int(input())

hud = a//100 #백의자리
a = a%100

ten = a//10  #십의자리
a = a%10

one = a//1   #일의자리

if hud<ten and ten<one:
  print("YES")
  
else:
  print("NO")





## Let's call an integer a palindrome if it remains the same after reading its digits from right to left. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise. 

## 입력이 4자리 수라고 아예 조건에 명시되어 있으므로 해당 방법으로 회문 검사
## 그러나 원래는 반복문을 통한 회문검사

a = int(input())

ths = a//1000
a = a%1000

hud = a//100
a = a%100

ten = a//10
a = a%10

one = a//1

if ths==one and hud==ten:
  print("YES")

else:
  print("NO")





## Given three integers, print the least of them.

a = int(input())
b = int(input())
c = int(input())

if a<b:
  if a<c:
    print(a)
  else:
    print(c)

elif b<c:
  if b<a:
    print(b)
  else:
    print(a)
    
elif c<a:
  if c<b:
    print(c)
  else:
    print(b)





## Given a month - an integer from 1 to 12, print the number of days in it in the year 2017.

a = int(input())

if a==2:
  print(28)
  
elif a<8:
  if a%2:
    print(31)
  else:
    print(30)
    
else:
  if a%2:
    print(30)
  else:
    print(31)





## Given three integers. Determine how many of them are equal to each other.
## The program must print one of the numbers: 3 (if all are same), 2 (if two of them are equal to each other and the third one is different) or 0 (if all numbers are different).

a = int(input())
b = int(input())
c = int(input())

cnt=0

if a==b:
  cnt=2
  if a==c:
    cnt=3
    
if b==c:
  cnt=2
  if b==a:
    cnt=3
  
if c==a:
  cnt=2
  if c==b:
    cnt=3
  
print(cnt)




  
## Given three integers, in which two are equal to each other and the third one is different.
## Print the order number of this different one - 1, 2 or 3.

a = int(input())
b = int(input())
c = int(input())

if a==b:
  print(3)
  
if a==c:
  print(2)

if b==c:
  print(1)





## Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
## a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
## a year is always a leap year if its number is exactly divisible by 400

a = int(input())

if (a%4 == 0 and a%100 != 0) or (a%400 == 0):
  print ("LEAP")

else:
  print("COMMON")
  




## Given a month (an integer from 1 to 12) and a day in it (an integer from 1 to 31) in the year 2017, print the month and the day of the next day to it.

month = int(input())
day = int(input())

if month==12:
  if day==31:
    month=1
    day=1
  else:
    day+=1

elif month==2:
  if day==28:
    month+=1
    day=1
  else:
    day+=1

elif month<8:
  if month%2:
    if day==31:
      month+=1
      day=1
    else:
      day+=1
  else:
    if day==30:
      month+=1
      day=1
    else:
      day+=1

else: 
  if month%2:
    if day==30:
      month+=1
      day=1
    else:
      day+=1
  else:
    if day==31:
      month+=1
      day=1
    else:
      day+=1
  

print(month)
print(day)





## Write a program that solves a linear equation ax = b in integers.
## Given two integers a and b (a may be zero), print a single integer root if it exists and print "no solution" or "many solutions" otherwise.

a=int(input())
b=int(input())

if a==0 and b==0:
  print("many solutions")

elif a==0:
  print("no solution")
  
elif b==0:
  print(0)
  
else:
  if b/a==int(b/a):
    print(int(b/a))
  else:
    print("no solution")





# Given integer coordinates of three vertices of a rectangle whose sides are parallel to coordinate axes, find the coordinates of the fourth vertex of the rectangle.

ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())
cx = int(input())
cy = int(input())

if ax == bx:
  dx = cx
elif bx == cx:
  dx = ax
else:
  dx = bx

if ay == by:
  dy = cy
elif by == cy:
  dy = ay
else:
  dy = by
  
print(dx)
print(dy)





# Given three integers, print them in ascending order.

a = int(input())
b = int(input())
c = int(input())

if a>b :
  tmp=a
  a=b
  b=tmp
  
if a>c:
  tmp=a
  a=c
  c=tmp
  
if b>c:
  tmp=b
  b=c
  c=tmp
  
print(a)
print(b)
print(c)
  
  
  


# 변수 a,b에 정수 값을 입력 받고, 최대값을 구하는 프로그램을 작성하라.

a = int(input())
b = int(input())

max = a
if b> max:
    max=b
print(max)





# 변수 a,b에 정수 값을 입력 받고, 최소값을 구하는 프로그램을 작성하라.

a = int(input())
b = int(input())

min = a
if b< min:
    min=b
print(min)





# 변수 a,b,c에 정수 값을 입력 받고, 최대값을 구하는 프로그램을 작성하라.

a = int(input())
b = int(input())
c = int(input())

max = a
if b>max:
    max=b

if c>max:
    max=c

print(min)





# 변수 a와 b에 정수 값을 입력 받고, a가 b보다 크면 교환한다. 최종결과 a,b를 출력하여라.

a = int(input())
b = int(input())

if a>b:
        tmp=a
        a=b
        b=tmp

print(a,b)





# 변수 a와 b에 정수 값을 입력 받고, 크기순으로 출력하여라.

a = int(input())
b = int(input())

if a>=b:
	print(a, b)
else:
	print(b,a)





# 화물량이 2 이하인 경우 값을 1증가시켜주고, 그 외의 값은 1 감소하는 프로그램을 작성하라.
a =int (input())

if a <= 2:
        a = a + 1
else :
        a = a- 1
        
print(a)





# 출발 화물량을 입력받고 2 이하면 울산역에 경유하고 출발 화물량 값을 1 만큼 증가시키는 프로그램을 작성하라.
a =int (input())

print("서울역 출발")

if a <= 2 :
        print("울산역 도착")
        a = a + 1

print("부산역 도착")
print("도착 화물량 =",a)
