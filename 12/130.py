a = '8' * 18 + '5' * 3
while '555' in a or '888' in a:
    if '555' in a:
        a = a.replace('555', '8', 1)
    while '888' in a:
        a = a.replace('888', '5', 1)
    if '555' in a:
        a = a.replace('555', '8', 1)

print(a)