def Sn(n,a,d=1):
    return (n*(2*a+(n-1)*d))//2  # Generate sum of arithmetic series or progression

def bonetrousle(n, k, b):
    lower = Sn(b,1)  # Find lowest possible sum from 1 with b elements in the arithmetic series
    upper = Sn(b,k-b+1)  # Find the largest possible sum from k-b+1 with b elements in the arithmetic series
    if n<lower or n>upper:
        return [-1]
    total = Sn(b,1)  # Start from lowest sum
    arr = list(range(1,b+1))  # i.e 1, 2, 3, 4 for b=4
    while total<n:
        add = min(k-arr[b-1],n-total)  # find the largest number we can add for each array element to get total to reach n. Constrains are has to be less than k and each element must be unique
        arr[b-1]+=add
        total+=add
        b-=1  # start from rightmost array element and move left till we get to the smallest element
        k-=1  # reduce value of k to ensure each element is unique
    return (i for i in arr)
