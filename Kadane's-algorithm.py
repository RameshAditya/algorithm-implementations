def kadane(A):
    currentsum=0
    maxsum=0
    startindex=0
    currentstartindex=0
    endindex=0
    for i in range(len(A)):
        currentsum+=A[i]
        if currentsum>maxsum:
            startindex=currentstartindex
            maxsum=currentsum
            endindex=i
        if currentsum<0:
            currentstartindex=i+1
            currentsum=0
    print(currentstartindex,maxsum)

A=[-1,-3,-5,-4,-6,-1,-2,-7,-13,-3]
kadane(A)

def kadane2(A):
    cursum=0
    maxsum=0
    isallneg=True
    for i in A:
        if i>0:
            isallneg=False
            break
    if isallneg:
        print(max(A))
    else:
        for i in range(len(A)):
            cursum+=A[i]
            if cursum>maxsum:
                maxsum=cursum
            if cursum<0:
                cursum=0
        print(maxsum)
kadane2(A)
