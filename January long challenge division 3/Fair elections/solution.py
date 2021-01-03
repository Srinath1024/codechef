T = int(input())
if 1<=T and T<=1000:
    for i in range(T):
        N,M = map(int,input().split())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        count=0
        if len(A)==N and len(B)==M:
            for i in range(max(N,M)):
                if sum(A)>sum(B):
                    print(count)
                    break
                elif sum(A)<=sum(B):
                    min_index = A.index(min(A))
                    max_index = B.index(max(B))
                    A[min_index],B[max_index] = B[max_index],A[min_index]
                    count=count+1
            if count==max(N,M) and sum(A)<sum(B):
                print(-1)
