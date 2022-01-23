from time import sleep

print("="*5, "Penentuan Nilai Akhir","="*5, '\n')

#INPUT Data
NPM     = int(input('NPM\t: '))
Nama    = (input('Nama\t: '))
UAS     = int(input('UAS\t: '))
UTS     = int(input('UTS\t: '))
absensi = int(input('Absensi\t: '))

#Kerja
UAS = UAS*40/100
UTS = UTS*35/100
absensi = absensi*20/100

nilai = UAS+UTS+absensi

#output
sleep(1)
print("Nilai rata-rata\t: %.2f" %(nilai))
sleep(2)
if nilai >=85:
    print("Sealamat Kamu mendapatkan nilai: A")
elif nilai <=84 and nilai>=70:
    print("Tingkatkan lagi!, Kamu mendapatkan nilai: B")
elif nilai <=69 and nilai>=60:
    print("Tetap semangat, Kamu mendapatkan nilai: C")
elif nilai <=59 and nilai>=40:
    print("Mohon maaf, Kamu mendapatkan nilai: D")
else:
    print("Kamu mengulang semester lagi")


print("="*5, "Penentuan Nilai Akhir","="*5, '\n')