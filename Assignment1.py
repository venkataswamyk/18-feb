def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
count=0
n=int(input('enter the number:'))
for i in range(2,n+1):
    
    if isprime(i):
        count=count+1
print('count of prime numbers are:',count)
