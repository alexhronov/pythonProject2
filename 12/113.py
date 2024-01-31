a = '5' * 65
while '333' in a or '555' in a:
    if '555' in a:
        a = a.replace('555', '3', 1)
    else:
        a = a.replace('333', '5', 1)

print(a)