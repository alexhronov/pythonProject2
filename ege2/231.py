print("x", "y", "z", "w", "f")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = int(((not(x)) <= y) and ((not(y)) == z))
                if f == 1:
                    print(x, y, z, w, f)  # ZYXW
