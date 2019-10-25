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





