T = int(input())
for test_case in range(T):
    N,K,D = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    total_problems = sum(arr)
    per_day = int(total_problems/K)
    if per_day>D:
        print(D)
    else:
        print(per_day)
