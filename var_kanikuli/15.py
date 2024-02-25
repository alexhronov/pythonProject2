for A in range(1, 1000):
    k = 0
    for x in range(1, 1000):
        a = (x % 2 == 0) <= ((not (x % 3 == 0)) or (x + A >= 80))
        if not a:
            break
        k += 1
    if k == 999:
        print(A)

