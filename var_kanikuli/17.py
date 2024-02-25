a = [int(i) for i in open("17.txt")]
k, b = 0, []
m = min(a)
for i in range(1, len(a) - 1):
    if a[i] % 117 == m or a[i - 1] % 117 == m:
        k += 1
        b.append(a[i] + a[i - 1])
print(k, max(b))
