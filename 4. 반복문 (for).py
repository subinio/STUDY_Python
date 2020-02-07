# A와 B를 입력받고, A부터 B까지의 모든 수를 출력하시오.

A=int(input())
B=int(input())

for i in range(A,B+1):
  print(i)





# A와 B를 입력받고, A부터 B까지의 모든 수를 역순으로 출력하시오.

A=int(input())
B=int(input())

for i in range(B,A-1,-1):
  print(i)





# A와 B를 입력받고, A부터 B까지 출력하시오.
# 단, A<B이면 A부터 B까지의 순서 그대로 출력하고, A≥B이면 A부터 B까지 숫자가 작아지는 순서로 출력하시오.

A=int(input())
B=int(input())

if A<B:
  for i in range(A, B+1):
    print(i)
  
else:
  for i in range(A, B-1, -1):
    print(i)





# 10개의 정수를 입력받고, 10개의 합을 출력하시오.

sum=0

for i in range(0,10):
    a=int(input())
    sum=sum+a

print(sum)





# 정수 N을 입력받고, N개의 정수를 입력받아 N개의 총합을 구하여라.

N=int(input())

sum=0

for i in range(0,N):
  a=int(input())
  sum+=a
  
print(sum)





# 정수 N을 입력받고, N개의 정수를 입력하여 0의 개수를 출력한다.

N=int(input())

cnt=0

for i in range(0,N):
  a=int(input())
  if a==0:
    cnt+=1
    
print(cnt)





# 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우의 수(a,b)를 출력하고, 그 갯수를 출력하여라.

cnt=0
for i in range(0,6):
    for j in range(0,6):
        cnt+=1
        print( "(", i+1, ",", j+1, ")" )
        
print(cnt)





# n을 입력받고, 주사위 2개를 던졌을 때 합이 n이 되는 모든 경우의 수 (a,b)를 모두 구하여라.

n=int(input())

for i in range(1,7):
    for j in range(1,7):
        if (i+j==n):
            print( "(", i, ",", j, ")" )





# 9보다 작거나 같은 정수 n을 입력받고, 아래 예시와 같은 형태로 출력하시오
'''
입력예시 : 3

출력예시 : 1
           12
           123
'''

n=int(input())

sum=0

for i in range(1,n+1):
  sum=0
  for j in range(1,i+1):
    sum=sum*10
    sum=sum+j
  
  print(sum)
