a = [10, 1, 10, 2, 3, 4, 3.56, "Hello", [34, 56, [45,100]]]

print(a[8][2][1])

print(a)

a += 45, "Symon"   # a = a + [45, 67, 77]
a.append(45)

print(a)

if 10 in a:
    print('10 is in list a')