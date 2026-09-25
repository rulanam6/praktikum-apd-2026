umur = int(input("Masukkan umur anda: "))

if umur >= 16:
    print("Selamat, anda dapat mengikuti event Genshin Impact!")
else:
    print("Maaf, anda belum cukup umur untuk mengikuti event Genshin Impact.")

total_pembelian = int(input("Masukkan total pembelian anda: "))
if total_pembelian >= 200000:
    print("Selamat, anda mendapatkan diskon 30%!")
elif total_pembelian > 100000:
    print("Selamat, anda mendapatkan diskon 10%!")
else:
    print("Maaf, anda tidak mendapatkan diskon.")

