a = '9' * 96
while '222222' in a or '9999' in a:
    if '222222' in a:
        a = a.replace('222222', '99', 1)
    if '9999' in a:
        a = a.replace('9999', '2', 1)
print(a)
