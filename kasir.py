print("===============================================")
print("               RGG SHOP                        ")
print("===============================================")
print("Kode           Nama barang          Harga      ")
print("===============================================")
print("HT          Hoodie thrasher          Rp. 850000")
print("WT          T-shirt ACDC WT          Rp. 400000")
print("70S       Shoes Converse 70S         Rp. 850000")
print("CS         Caps converse logo        Rp. 250000")
print("===============================================")

banyak_jenis = int(input("Banyak jenis yang ingin dibeli: "))
kode_barang = []
banyak_pasang = []
nama_barang = []
harga = []
Jumlah = []

i = 0
while (i<=banyak_jenis):
    print(i)
    i +=1
    kode_barang.append(input("kode barang [HT/WT/70S/CS] : "))
    banyak_pasang.append(int(input("banyak pasang : ")))

    if kode_barang[i]=="HT" or kode_barang [i]=="HT":
        harga.append("850000")
        Jumlah.append(banyak_pasang[i]*int("850000"))
    
    elif kode_barang[i]=="WT" or kode_barang [i]=="WT":
        harga.append("400000")
        Jumlah.append(banyak_pasang[i]*int("400000"))

    elif kode_barang[i]=="70S" or kode_barang [i]=="70S":
        harga.append("850000")
        Jumlah.append(banyak_pasang[i]*int("850000"))

    elif kode_barang[i]=="CS" or kode_barang [i]=="CS":
        harga.append("250000")
        Jumlah.append(banyak_pasang[i]*int("250000"))
        break

    else:
        nama_barang.append("Tidak ditemukan")
        harga.append("0")
        Jumlah.append(banyak_pasang[i]*int("0"))\
        

i = i+1
print("=============================================================")
print("                      RGG SHOP                               ")
print("=============================================================")
print("No    Nama          Harga           Banyak         Jumlah    ")
print("    Sepatu          Satuan          Pasang         Harga     ")
print("=============================================================")

jumlah_bayar = 0
p = 0
while p<banyak_jenis:
    jumlah_bayar = jumlah_bayar+Jumlah[p]
    p = p + 1
    print("%i    %s    %s    %i"% (p+1, nama_barang[p], harga[p], banyak_pasang[p], Jumlah[p]))

print("=============================================================")
pajak = jumlah_bayar*5/100
total_bayar = jumlah_bayar * pajak
print("Jumlah bayar = Rp. ", jumlah_bayar)
print(" Total bayar = Rp. ", total_bayar)