q = 1
for iter in range(q):
    (n, k, m) = (4,2,101000000)
    #(n, k, m) = (int(n), int(k), int(m))
    s = [int(x) for x in input().split()]

    dictOmmit = {}
    for num in s:
        t = int(m / num)
        for i in range(1, t + 1):
            dictOmmit[str(num * i)] = 0

    total = 0
    for i in range(1, m + 1):
        if str(i) in dictOmmit:
            pass
        else:
            total += i ** k
    print(total)