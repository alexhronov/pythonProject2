a = open("24.txt").readline()
sogl = 'BCD'
gl = 'AO'
k, b = 0, []

for i in range(1, len(a) - 1, 2):
    if a[i - 1] in sogl and a[i] in gl:
        k += 1
    else:
        b.append(k)
        k = 0

print(max(b))
