angka = 6

if angka < 10: 
    print("Angka kurang dari 10")

umur = int(input("Masukkan umur: "))

if umur >= 17:
    print("Kamu sudah bisa membuat KTP")
else:
    print("Kamu belum bisa membuat KTP")

kendaraan = input("Masukkan jenis kendaraan anda: ").lower()

if kendaraan == "mobil": 
    tarif_parkir = 10000 
elif kendaraan == "motor": 
    tarif_parkir = 5000 
else: 
    tarif_parkir = 15000

print("Tarif parkir yang harus dibayar:", tarif_parkir)

umur = 20 
status = "Dewasa" if umur >= 18 else "Belum Dewasa"
print("Status:", status)

nilai= int(input("Masukkan nilai: "))

if nilai >= 10:
    if nilai >= 20:
        if nilai >= 30:
            print("Angka besar")
        print("Angka sedang")
    print("Angka kecil")

