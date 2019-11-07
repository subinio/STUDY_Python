## 홍길동씨의 주민등록번호는 881120-1068234이다.
## 홍길동씨의 주민등록번호를 연원일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.

pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)  # 881120 출력
print(num)       # 1068234 출력





## 다음과 같은 문자열 a:b:c:d가 있다.
## 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.

a = "a:b:c:d"
b = a.replace(":", "#")
print(b)





## Can you change it so it can read and sum three number?

a = int(input())
b = int(input())
c = int(input())
print(a + b + c)





## Write a program that greets the user by printing the word “Hello”, a comma, the name of the user and an exclamation make after it.

a = input()

print("Hello, "+a+"!")





## N students take K apples and distribute them among each other evenly.
## The remaining (the indivisible) part remains in the basket.
## How many apples will each single student get?
## How many apples will remain in the basket?

n = int(input())
k = int(input())

print(k // n)
print(k % n)





## Given the integer N - the number of seconds that is passed since midnight - how many full hours and full minutes are passed since midnight?

second = int(input())

print(second//(60*60), second//60)




## Given two timestamps of the same day: a number of hours, minutes and seconds for both of the timestamps.
## The moment of the first timestamp happened before the moment of the second one. Calculate how many seconds passed between them.

hour1 = int(input())
min1 = int(input())
sec1 = int(input())

hour2 = int(input())
min2 = int(input())
sec2 = int(input())

second1 = hour1*(60*60)+ min1*60 + sec1 

second2 = hour2*(60*60)+ min2*60 + sec2 

print(second2-second1)





## Given a two-digit integer, print its left digit(a tens digit) and then its right digit(a ones digit).
## Use the operator of integer division for obtaining the tens digit and the operator of taking remainder for obtaining the ones digit.

n = int(input())

print(n//10, n%10)





## Given a two-digit integer, swap its digits and print the result.

n = int(input())

print( (n%10)*10 + (n//10))





## Given and integer greater than 9, print its last two digit.

a = int(input())

print(a%100)





## Given an integer, print its tens digit.

a = int(input())

print((a//10) %10)





## Given a three-digit number. Find the sum of its digits.

a = int(input())

sum = 0

sum += a/10
a = a%10

sum += a/10
a = a%10

sum += a/10

print(sum)





## Given a positive real number, print its first digit to the right of the decimal point.

a = float(input())

print(int((a*10)%10))





## A car can cover distance of N kilometers per day.
## How many days will it take to cover a route of length M kilometers?
## The program gets two numbers? The program gets two numbers: N and M.

N = int(input())
M = int(input())

print((M+(N-1))//N)





## Given a year (as a positive integer), find the respective number of the century.
## Note that, for example, 20th century began with the year 1901.

a = int(input())

print(((a-1)//100)+1)





## A cupcake costs A dollars and B cents.
## Determine, how many dollars and cents should one pay for N cupcakes.
## A program gets three numbers. A, B, N.
## It should print two numbers: total cost in dollars and cents.

A = int(input())
B = int(input())
N = int(input())

dollars = A*N + (B*N)//100
cents = (B*N)%100

print(dollars, cents)





## Days of week are numbered as: 
## 0 : Sunday,    1 : Monday,    2 : Tuesday, … 6 : Saturday.
## An integer K in the range 1 to 365 is given.
## Find the number of day of week for K-th day of year provided that in this year January 1 was Thursday. 

K = int(input())

print((K%7+3)%7)





## Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
## For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am. So the program should print 2 30.

a = int(input())

hour = a//60
min = a%60

print(hour, min)





## A school decided to replace the desks in three classrooms.
## Each desk sits two students.
## Given the number of students in each class, print the smallest possible number of desks that can be purchased.

## The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

a = int(input())
b = int(input())
c = int(input())

a_need = (a+1)//2
b_need = (b+1)//2
c_need = (c+1)//2

print(a_need+b_need+c_need)





## 두 숫자를 입력받아 두 수를 더한값, 곲한값, 나눈값을 출력하세요.
a = int(input())
b= int(input())

sum = a+b
mul = a*b
div = a/b

print(sum, mul, div)





## 두 변수 a,b 에 자연수를 입력 받고 두 변수 값을 Swap(교환) 하는 프로그램을 작성하라.

a = int (input("a ="))
b = int (input("b ="))

tmp = b
a = n2
b = tmp

print("a =", a)
print("b =", b)





## 변수 a, b, c에 자연수를 입력 받고 세 변수 값을 Swap(교환) 하는 프로그램을 작성하라. 
## (단 a->b, b->c, c->a 으로 치환하라.)


a = int (input("a = "))
b = int (input("b = "))
c = int (input("c = "))

tmp = c
c = b
b = a
a = tmp

print("a =", a)
print("b =", b)
print("c =", c)


