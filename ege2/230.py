print("x", "y", "z", "w", "f")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = int(((not(x)) and y) or (z and (not(y))) or ((not(z)) and w))
                if f == 0:
                    print(x, y, z, w, f)  # XYZW
