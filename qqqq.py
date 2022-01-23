print("Selamat Datang di ATM Rangga")
print("Pilih option : ")
print("1. Check Saldo saya")
print("2. Ambil Uang saya")
option=int(input("Silahkan pilih option : "))
if option==1: 
    print("Uang kamu berjumlah Rp.200.000")
elif option==2:
    print("Uang kamu berjumlah Rp.200.000, mau ambil berapa?")
    print("1. Rp.100.000")
    print("2. Rp.200.000")
    uang_kamu=200000
    option2=int(input("Option :"))
    if option2==1:
        hasil=uang_kamu-100000
        print("Uang kamu Sekarang berjumlah :", hasil)
    elif option2==2:
        hasil2=uang_kamu-200000
        print("Uang kamu sekarang berjumlah", hasil2)
    else:
        print("Keyword anda salah")