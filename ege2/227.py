print("a", "b", "c", "d", "f")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = int(((a <= b) and (c <= d)) or (not(c)))
                if f == 0:
                    print(a, b, c, d, f)  # BDCA
                    