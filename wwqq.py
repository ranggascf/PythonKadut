def kalkulasi_kembalian(uang_bayar: int, harga_bayar: int)-> any:
    if uang_bayar <= harga_bayar:
        print(f"Uang bayar harus diatas {harga_bayar}")
        return None

    return uang_bayar - harga_bayar
def garis():
    print("=========================================================")

list_susu = [
    {
        "kode": "DC"or "dc",
        "merk": "Dancow",
        "ukuran": ["S", "B"],
        "harga": {
            "S": 25000,
            "B": 50000,
        }
    },
    {
        "kode": "MG"or "mg",
        "merk": "Morinaga",
        "ukuran": ["S", "B"],
        "harga": {
            "S": 40000,
            "B": 100000,
        }
    },
]


nama_pembeli = input("Masukan nama pembeli : ")
nama_kasir = input("Masukan nama kasir : ")

kode_susu = input("Masukan kode(DC/MG) : ").upper()
jumlah_beli = int(input("Jumlah beli : "))
ukuran_susu = input("Masukan kode ukuran(S/B) : ").upper()

item_yg_dibeli = [susu for susu in list_susu if susu["kode"] == kode_susu][0]

subtotal = item_yg_dibeli['harga'][ukuran_susu] * jumlah_beli

print('Nama Pembeli = ', nama_pembeli)
print('Nama Kasir = ', nama_kasir)
garis()
print("\t\t\tPembelian Susu")
garis()
print(f"Kode susu = {item_yg_dibeli['kode']}")
print(f"Merk susu = {item_yg_dibeli['merk']}")
print(f"Harga susu = {item_yg_dibeli['harga'][ukuran_susu]}")
print(f"Jumlah beli = {jumlah_beli}")
print(f"Subtotal = {subtotal}")
garis() 

kembalian= None
while kembalian is None:
    bayar =int(input("masukan uang bayar :"))
    kembalian = kalkulasi_kembalian(bayar, subtotal)
print(f"kembalian :{kembalian}")

garis()
print("Terimakasih sudah belanja di Rangboy.")
garis()