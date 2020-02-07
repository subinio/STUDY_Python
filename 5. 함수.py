# a와 b를 넣으면 a+b를 내보내는 함수를 만들고
# a와 b를 입력받고, 해당 함수를 이용하여 a와 b의 합을 출력하여라.

def sum(a,b):
    return a+b

a = int(input())
b = int(input())

print(sum(a,b))





# a를 입력받아 a가 짝수면 "짝수입니다", 홀수면 "홀수입니다" 를 출력하는 함수를 만들고, 사용하여라.

def check_odd_even(num):
    if num%2==0:
        print("짝수입니다")
    else:
        print("홀수입니다")

a=int(input())
check_odd_even(a)





# 정수 n을 입력받고, n까지의 합을 구하는 함수를 작성하시오.

def sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
        
    return sum

n = int(input())
print(sum(n))
