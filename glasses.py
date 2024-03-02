t = int(input())

for i in range(t):
    n = int(input())
    glasses = list(map(int, input().split()))
    needed = int(sum(glasses)/n)
    ok = True
    for i in range(n-1):
        if glasses[i] >= needed:
            add = glasses[i]-needed
            glasses[i] -= add
        else:
            print("NO")
            ok = False
            break
        glasses[i+1] += add
    if ok == True:
        print("YES")
        
        
        