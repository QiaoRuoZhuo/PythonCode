
def fun1(n)
    t = list(range(1,n+1))
    if n % 2 == 1:
        t.append(0)
        n += 1
    for i in range(1, n):
        print(f'{i}:', end=" ")
        for j in range(n):
            print(f'{(t[j]}-{t[n-1-j])}', end=" ")
        print()
        temp = t[n-1]
        for j in range(n-1, 1, -1):
            t[j] = t[j-1]
        t[1] = temp

for i in range(1, n):
    print(f'{i}:', end=" ")

