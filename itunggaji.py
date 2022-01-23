menu = ["Aplikasi potong gaji", "Angka genap 1-100 habis dibagi 3" , "Angka genap 5-200"]
print(menu)

for i in range (3):
    print(f"[{i+1}], {menu[i]}")

pilihan = int(input("Pilihan anda : "))

while pilihan not in [1,2,3]:
    print("hanya menerima input 1/2/3")
    pilihan = int(input("Pilihan anda : "))

if pilihan == 1: 
    # IV Gaji Pegawai
    gaji = 5000000
    potongan = 0
    tidak_hadir = int(input("Jumlah tidak hadir : "))

    if tidak_hadir > 5:
        potongan = tidak_hadir * 25000

    pajak = round((gaji-potongan) * 2.5 / 100)

    print(f"Total Gaji Per Bulan  : Rp {gaji}")
    print(f"Potongan Absen        : Rp {potongan}")
    print(f"Pajak                 : Rp {pajak}")
    print("------------------")
    print(f"Gaji Bersih           : Rp {gaji-potongan-pajak}")


elif pilihan == 2:
    print("\n\n Angka genap yang habis dibagi 3 dari 1-100")
    for i in range (1, 100):
        if i % 2 == 0 and i % 3 == 0:
            print(i, end=" ")

elif pilihan == 3:
    print("\n\nAngka genap 5 - 200 :")
    for i in range(5, 200):
        if i % 2 == 0:
            print(i, end=" ")