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
  




## 14
