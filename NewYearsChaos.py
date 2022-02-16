def minimumBribes(q):
    # Write your code here
    bribes = t = 0
    l = len(q)
    inOrder = [i for i in range(1, l+1)]
    for i in range(l):
        tmp = q[i] - inOrder[i]
        if tmp > 2:
            print('Too chaotic')
            return
        # Count how many bribes each person has received.
        # since max bribes allowed is 2, the farthest someone could have gotten to is 
        # 2 positions before the current person's original position, q[i] in our case
        # so we check from index q[i] - 2 to our current position i for any values
        # greater than the current value's original position (q[i])
        for j in range(max(q[i] - 2, 0), i):
            if q[j] > q[i]:
                bribes += 1 
    print(bribes)
