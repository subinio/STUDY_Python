# while문을 사용해 1부터 100까지의 자연수 중 3의 배수를 출력하여라.

i = 1

while i <= 100:
    if i % 3 == 0: 
        print(i)
    i += 1





# 정수 N을 입력받고 N보다 작은 제곱수를 모두 출력하여라.

N = int(input())

i = 1
while i*i <= N:
   print(i*i)
   i += 1





# 1보다 큰 정수 N을 입력받고, N을 나눌 수 있는 1이 아닌 가장 작은 수를 출력하여라.

a = int(input())

i=2
while i<=a:
  if a%i==0:
    print(i)
    break
  else:
    i=i+1





# 정수 X를 입력받고, X보다 작거나 같은 최대 정수 2ⁿ 을 구하고, n과 2ⁿ 을  출력하여라.

X = int(input())

n=0
while 2**n <= X:
  n+=1
  
print(n-1, 2**(n-1))





# 음이 아닌 정수를 계속 입력받고, 입력이 0일때 입력을 멈춘다.
# 입력된 정수의 개수를 구하여라.(0은 세지 않는다.)

cnt=0

a=int(input())

while a!=0:
  cnt+=1
  a=int(input())


print(cnt)





# 0일때 까지 정수를 입력받고, 입력받은 정수들의 총합을 구하시오.

sum=0

a = int(input())

while a!=0:
  sum+=a
  a = int(input())
  
print(sum)





# 0일때 까지 정수를 입력받고, 입력받은 정수들의 평균을 구하시오.

sum=0
cnt=0

a=int(input())
while a!=0:
  sum+=a
  cnt+=1
  a=int(input())

print(sum/cnt)





# 0일때 까지 정수를 입력받고, 입력받은 정수들 중 가장 큰 값을 구하시오.

max=0

a=int(input())

while a!=0:
  if a>max:
    max=a
    
  a=int(input())
  
print(max)





# 0일때 까지 정수를 입력받고, 입력받은 정수들 중 가장 큰 값의 위치를 구하시오.

a=int(input())

max=0
i=0

while a!=0:
  i+=1
  if a>max:
    max=a
    index=i
  a=int(input())
  
print(index)





# 0일때 까지 정수를 입력받고, 입력받은 정수들 중 짝수의 개수를 출력하시오.

cnt=0

a=int(input())

while a!=0:
  if a%2==0:
    cnt+=1
  a=int(input())
    
print(cnt)





# N을 입력받고, 1부터 N까지 3의 배수를 제외하고 출력하여라.(continue문 사용)

N=int(input())

i=1
while i<=N:
  if i%3==0:
    i=i+1
    continue

  print(i)
  i=i+1





# while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해보자.
'''
*
**
***
****
*****

'''
  
i = 0

while True:
    i += 1 
    if i > 5:
        break     
    
    print ('*' * i)










