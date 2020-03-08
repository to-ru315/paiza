M, N, K = (int(x) for x in input().split())

ans = []
for ini in range(M+1):
    ans.append(0)
    
for i in range(K):
    a = int(input())
    if N > 0:
        N -= 1
        ans[a] += 1
    for j in range(M+1):
        if ans[j] > 0:
            ans[j] -= 1
            ans[a] += 1
            
maxIndex = [i for i, x in enumerate(ans) if x == max(ans)]
[print(i) for i in maxIndex]


        