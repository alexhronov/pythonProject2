a = '5' * 200
while '555' in a or '333' in a:
    if '555' in a:
        a = a.replace('555', '3', 1)
    else:
        a = a.replace('333', '5', 1)

print(sum(map(int, a)))
