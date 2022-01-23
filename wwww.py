angka = 10
listAngka = [i for i in range(1, angka+1)]
for i in range(angka, 0, -1):
    print(*listAngka[:i])
for i in range(angka):
    print(*listAngka[:i+1])