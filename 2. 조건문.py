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
