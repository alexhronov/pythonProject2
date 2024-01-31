a = '4' + '6' * 125 + '4'
while '63' in a or '664' in a or '6665' in a:
    if '63' in a:
        a = a.replace('63', '4', 1)
    else:
        if '664' in a:
            a = a.replace('664', '5', 1)
        else:
            if '6665' in a:
                a = a.replace('6665', '3', 1)

print(a)