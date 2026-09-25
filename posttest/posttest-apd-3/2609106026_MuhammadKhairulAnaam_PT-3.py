print("----- Program Transaksi Pengisian BBM di SPBU -----")
nama_pelanggan  = input("Masukkan nama panggilan anda: ").lower()
nim             = input("Masukkan 2 digit terakhir NIM anda: ")

if nama_pelanggan != "herul" or nim != "26":
    print("Mohon maaf login anda gagal. Silahkan periksa kembali.")
else:
    print("Selamat datang, herul! Login anda berhasil. \n")
    print("===========================================")
    print("----- Jenis BBM yang tersedia di SPBU -----")
    print("1. Pertalite         = Rp. 10.000/liter")
    print("2. Pertamax          = Rp. 12.500/liter")
    print("3. Pertamax Turbo    = Rp. 15.000/liter")
    print("=========================================== \n")

pilihan_bbm = int(input("Masukkan pilihan jenis BBM yang ingin dibeli: "))
liter       = float(input("Masukkan jumlah liter BBM yang ingin dibeli: "))

if pilihan_bbm == 1:
    harga_per_liter = 10000
    jenis_bbm = "Pertalite"
    status = True
elif pilihan_bbm == 2:
    harga_per_liter = 12500
    jenis_bbm = "Pertamax"
    status = True
elif pilihan_bbm == 3:
    harga_per_liter = 15000
    jenis_bbm = "Pertamax Turbo"
    status = True
else:
    print("Pilihan jenis BBM tidak valid.")
    status = False

if status:
    total_harga = liter * harga_per_liter
    if liter >= 10:
        persen_diskon = 0.1
    elif liter >= 5:
        persen_diskon = 0.05
    else:
        persen_diskon = 0.0
    diskon_pembelian = persen_diskon * total_harga
    member = input("Apakah anda seorang member SPBU? (iya/tidak): ").lower()
    if member == "iya":
        diskon_member = 0.02 * total_harga
    else:
        diskon_member = 0.0
    total_diskon = diskon_pembelian + diskon_member
    total_bayar = total_harga - total_diskon 

    print("====================================================== \n")
    print("                   Rincian Transaksi                     ")
    print("======================================================")
    print("Nama pelanggan               =", nama_pelanggan)
    print("NIM pelanggan                =", nim)
    print("Jenis BBM yang dibeli        =", jenis_bbm)
    print("Jumlah liter yang dibeli     =", liter, "liter")
    print("Harga per liter              = Rp.", harga_per_liter)
    print("Total harga sebelum diskon   = Rp.", total_harga)
    print("Diskon pembelian             = Rp.", diskon_pembelian)
    print("Diskon member                = Rp.", diskon_member)
    print("Total diskon                 = Rp.", total_diskon)
    print("Total yang harus dibayar     = Rp.", total_bayar)
    print("====================================================== \n")
    print("Terima kasih telah bertransaksi di SPBU kami. Semoga hari anda menyenangkan!")

else:
    print("Transaksi tidak dapat diproses karena pilihan jenis BBM tidak valid.")