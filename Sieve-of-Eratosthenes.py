A=[]
n=int(input())
for i in range(n):  #creating the array of sieving
    A.append(0)

def sieve(n):
    global A
    ct=0    #number of factors
    for i in range(2,int(n//2+1)):
        if A[i]==1:     #checking sieve if already done
            continue
        elif n%i!=0:    #if not, sieve it
            for j in range(i,n//2+1,i):
                A[j]=1
        elif n%i==0:    #if not prime
            print("Not prime")
            ct=1
            break
    if ct==0:
        print("Prime")

sieve(n)
print(A)
