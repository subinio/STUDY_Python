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





## 
