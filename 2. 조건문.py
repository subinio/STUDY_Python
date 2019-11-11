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





##  
