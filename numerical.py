def isprime(n):
    count=0
    for i in range(2,n//2+1):
        if(n%i==0):
             count+=1    
    if count==0:
        return True
    else:
        return False