print("x", "y", "z", "w", "f")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = int((w or x or y) <= (((y or z) and x) or (y and (w or z))))
                if f == 0:
                    print(x, y, z, w, f)  # YWZX
