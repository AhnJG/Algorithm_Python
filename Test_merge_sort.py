def merge(a):
    n = len(a)
    if n <= 1:
        return
    mid = n // 2

    a1 = a[:mid]
    a2 = a[mid:]

    merge(a1)
    merge(a2)

    i = 0
    while a1 and a2:
        if a1[0] > a2[0]:
            a[i] = a2.pop(0)
        else:
            a[i] = a1.pop(0)
        i += 1

    while a1:
        a[i]= a1.pop(0)
        i += 1

    while a2:
        a[i] = a2.pop(0)
        i += 1

    print(a)

a = [1, 4, 3, 2, 6, 5, 7, 4]
merge(a)

