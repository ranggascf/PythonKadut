def tambah(a, b):
    tambah = float(a) + float (b)
    return tambah

def kurang(a, b):
    kurang = float (a) - float (b)
    return kurang

def kali(a, b):
    kali = float (a) * float (b)
    return kali

def bagi(a, b):
    bagi = float (a) / float (b)
    return bagi

while True:
    print('\n\n\t\t========== KALKULATOR SEDERHANA ==========\n\n')
    a = input('Masukan bilangan 1: ')
    b = input('Masukan bilangan 2: ')
    print('\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n.4 Pembagian\n.5 Batal')
    C = input('\npilih 1-5: ')
    if C == '1':
        print('Hasilnya adalah: ', tambah(a, b))
    elif C == '2':
        print('Hasilnya adalah: ', kurang(a, b))
    elif C == '3':
        print('Hasilnya adalah: ', kali(a, b))
    elif C == '4':
        print('Hasilnya adalah: ', bagi(a, b))
    elif C == '5':
        break
    else:
        print("operasi tidak dikenal.")