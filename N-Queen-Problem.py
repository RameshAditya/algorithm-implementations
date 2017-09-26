from datetime import datetime
def printboard(A):
    for i in range(len(A)):
        for j in range(len(A)):
            print(A[i][j],end=' ')
        print()
def issafe(A,row,col):
    for i in range(col):
        if A[row][i]==1:
            return False
    i=row
    j=col
    while i>=0 and j>=0:
        if A[i][j]==1:
            return False
        else:
            i-=1
            j-=1
    i=row
    j=col
    while i<len(A) and j>=0:
        if A[i][j]==1:
            return False
        else:
            i+=1
            j-=1

    return True

def solveboard(A,col):
    if col>=len(A):
        return True
    for i in range(len(A)):
        if issafe(A,i,col):
            A[i][col]=1
            if solveboard(A,col+1):
                return True
            else:
                A[i][col]=0
    #return False

n=int(input())
A=[]
for i in range(n):
    B=[]
    for j in range(n):
        B.append(0)
    A.append(B)
start=datetime.now()
solveboard(A,0)
if solveboard(A,0)==False:
    print('No soln')
else:
    stop=datetime.now()
    printboard(A)
    print('time taken',stop-start)
        
