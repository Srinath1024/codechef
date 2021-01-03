T = int(input())
for test_case in range(T):
    N = int(input())
    s = input()
    arr = [s[i:i+4] for i in range(0,N,4)]
    ans = ""
    for ele in arr:
        if ele=='0000':
            ans = ans + 'a'
        elif ele=='0001':
            ans = ans+'b'
        elif ele=='0010':
            ans=ans+'c'
        elif ele=='0011':
            ans = ans + 'd'
        elif ele=='0100':
            ans = ans + 'e'
        elif ele=='0101':
            ans = ans + 'f'
        elif ele=='0110':
            ans = ans + 'g'
        elif ele=='0111':
            ans = ans + 'h'
        elif ele=='1000':
            ans = ans + 'i'
        elif ele=='1001':
            ans=ans+'j'
        elif ele=='1010':
            ans=ans+'k'
        elif ele=='1011':
            ans=ans+'l'
        elif ele=='1100':
            ans=ans+'m'
        elif ele=='1101':
            ans=ans+'n'
        elif ele=='1110':
            ans=ans+'o'
        elif ele=='1111':
            ans=ans+'p'
    print(ans)
