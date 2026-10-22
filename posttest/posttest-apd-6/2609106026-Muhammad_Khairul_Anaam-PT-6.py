import os

users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "herul": {"password": "herul123", "role": "User"},
}

koleksi = {
    1: {"nama": "Si Kucing Hoki", "jenis": "Hewan", "harga": 15000},
    2: {"nama": "Dino Imut", "jenis": "Hewan", "harga": 20000},
    3: {"nama": "Sepatu Mini", "jenis": "Miniatur", "harga": 12000},
}
id_terakhir = 3

clear_cmd = "cls" if os.name == "nt" else "clear"

program_jalan = True

while program_jalan:
    os.system(clear_cmd)
    print("=" * 45)
    print("         Koleksi Gantungan Kunci      ")
    print("=" * 45)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3):  ").strip()

    if pilihan == "1":
        os.system(clear_cmd)
        print("===== LOGIN =====")
        user_aktif = None
        role_aktif = None
        percobaan = 0

        while percobaan < 3 and user_aktif is None:
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            if username in users and users[username]["password"] == password:
                user_aktif = username
                role_aktif = users[username]["role"]

            else:
                percobaan += 1
                print(f"Username atau Password anda salah! Sisa percobaan anda: {3 - percobaan}")

        if user_aktif is None:
            print("Mohon maaf, anda gagal login, silahkan kembali ke menu utama")
            input("Tekan Enter untuk lanjut...")

        elif role_aktif == "Admin":
            admin_jalan = True
            while admin_jalan:
                os.system(clear_cmd)
                print("=" * 45)
                print(f"  Halo admin! Mau ngapain nih hari ini")
                print("=" * 45)
                print("1. Tambahkan Gantungan Kunci")
                print("2. Lihat Semua Koleksi")
                print("3. Ubah Koleksi")
                print("4. Hapus Koleksi")
                print("5. Logout")
                menu = input("Pilih menu (1-5): ").strip()

                if menu == "1":
                    os.system(clear_cmd)
                    print("===== TAMBAH GANTUNGAN KUNCI =====")
                    
                    nama_valid = False
                    while not nama_valid:
                        nama = input("Nama gantungan kunci: ").strip()
                        if nama == "":
                            print("Nama tidak boleh kosong!")
                        else:
                            sudah_ada = False
                            for data in koleksi.values():
                                if data["nama"] .lower() == nama.lower():
                                    sudah_ada = True
                            if sudah_ada:
                                print("Nama itu sudah di dalam koleksi")
                            else:
                                nama_valid = True

                    jenis = ""
                    while jenis == "":
                        jenis = input("Jenis gantungan kunci:   ").strip()
                        if jenis == "":
                            print("Jenis tidak boleh kosong")

                    harga_valid = False
                    while not harga_valid:
                        harga_input = input("Harga gantungan kunci: ").strip()
                        if harga_input.isdigit() and int(harga_input) > 0:
                            harga = int(harga_input)
                            harga_valid = True
                        else:
                            print("Harga harus berupa angka lebih dari 0!")

                    id_terakhir += 1
                    koleksi[id_terakhir] = {"nama": nama, "jenis": jenis, "harga": harga}
                    print(f"YEYY! '{nama}' berhasil masuk ke koleksi")
                    input("Tekan Enter untuk lanjut...")

                elif menu == "2":
                    os.system(clear_cmd)
                    print("===== DAFTAR KOLEKSI =====")
                    if len(koleksi) == 0:
                        print("Koleksi masih kosong, yuk belanja dulu")
                    else:
                        print(f"{'ID':<4}{'Nama':<22}{'Jenis':<14}{'Harga':>12}")
                        print("-" * 52)
                        total = 0
                        for id_item, data in koleksi.items():
                            harga_teks = f"{data['harga']:,}".replace(",", ".")
                            print(f"{id_item:<4}{data['nama']:<22}{data['jenis']:<14}Rp{harga_teks:>10}")
                            total += data["harga"]
                        print("-" * 52)
                        print(f"Total Koleksi: {len(koleksi)} buah")
                        print("Total nilai  : Rp" + f"{total:,}".replace(",", "."))
                    input("Tekan Enter untuk lanjut...")

                elif menu == "3":
                    os.system(clear_cmd)
                    print("===== UBAH KOLEKSI =====")
                    if len(koleksi) == 0:
                        print("Belum ada koleksi yang di ubah")
                    else:
                        for id_item, data in koleksi.items():
                            harga_teks = f"{data['harga']:,}".replace(",", ".")
                            print(f"{id_item}. {data['nama']} | {data['jenis']} | Rp{harga_teks}")

                        nomor = input("ID yang mau diubah: ").strip()
                        if nomor.isdigit() and int(nomor) in koleksi:
                            idx = int(nomor)
                            print("(Kosongkan lalu Enter jika tidak ingin mengubah)")

                            nama_baru = input(f"Nama baru  [{koleksi[idx]['nama']}]: ").strip()
                            if nama_baru != "":
                                nama_kembar = False
                                for id_item, data in koleksi.items():
                                    if id_item != idx and data["nama"].lower() == nama_baru.lower():
                                        nama_kembar = True
                                if nama_kembar:
                                    print("Nama itu sudah dipakai, nama tidak diubah")
                                else:
                                    koleksi[idx]["nama"] = nama_baru

                            jenis_baru = input(f"Jenis baru [{koleksi[idx]['jenis']}]: ").strip()
                            if jenis_baru != "":
                                koleksi[idx]["jenis"] = jenis_baru

                            harga_selesai = False
                            while not harga_selesai:
                                harga_baru = input(f"Harga baru [{koleksi[idx]['harga']}]: ").strip()
                                if harga_baru == "":
                                    harga_selesai = True
                                elif harga_baru.isdigit() and int(harga_baru) > 0:
                                    koleksi[idx]["harga"] = int(harga_baru)
                                    harga_selesai = True
                                else:
                                    print("Harga harus angka lebih dari 0")

                            print("Data berhasil di perbarui")
                        else:
                            print("ID tidak valid")
                    input("Tekan Enter untuk lanjut...")

                elif menu == "4":
                    os.system(clear_cmd)
                    print("===== HAPUS KOLEKSI =====")
                    if len(koleksi) == 0:
                        print("Tidak ada koleksi yang bisa di hapus")
                    else:
                        for id_item, data in koleksi.items():
                            harga_teks = f"{data['harga']:,}".replace(",", ".")
                            print(f"{id_item}. {data['nama']} | {data['jenis']} | Rp{harga_teks}")

                        nomor = input("ID yang mau dihapus: ").strip()
                        if nomor.isdigit() and int(nomor) in koleksi:
                            idx = int(nomor)
                            yakin = input(f"Yakin hapus '{koleksi[idx]['nama']}'? (y/n): ").strip().lower()
                            if yakin == "y":
                                terhapus = koleksi.pop(idx)
                                print(f"'{terhapus['nama']}' sudah di hapus, babayy~")
                            else:
                                print("gajadi di hapus, aman kok!")
                        else:
                            print("ID tidak valid")
                    input("Tekan Enter untuk lanjut...")

                elif menu == "5":
                    admin_jalan = False
                    print("Logout berhasil!")
                    input("Tekan Enter untuk lanjut...")

                else:
                    print("Menu tidak ada, pilih 1-5 yaa!")
                    input("Tekan Enter untuk lanjut...")

        else:
            user_jalan = True
            while user_jalan:
                os.system(clear_cmd)
                print("=" * 45)
                print(f"   Halo {user_aktif}! selamat melihat lihat!")
                print("=" * 45)
                print("1. Lihat Koleksi Gantungan Kunci")
                print("2. Logout")
                menu = input("Pilih menu (1-2): ").strip()

                if menu == "1":
                    os.system(clear_cmd)
                    print("===== KOLEKSI GANTUNGAN KUNCI =====")
                    if len(koleksi) == 0:
                        print("Koleksi masih kosong.")
                    else:
                        print(f"{'ID':<4}{'Nama':<22}{'Jenis':<14}{'Harga':>12}")
                        print("-" * 52)
                        for id_item, data in koleksi.items():
                            harga_teks = f"{data['harga']:,}".replace(",", ".")
                            print(f"{id_item:<4}{data['nama']:<22}{data['jenis']:<14}Rp{harga_teks:>10}")
                    input("Tekan Enter untuk lanjut...")

                elif menu == "2":
                    user_jalan = False
                    print("Sampai jumpa lagi!")
                    input("Tekan Enter untuk lanjut...")

                else:
                    print("menu tidak ada, pilih 1-2 yaa!")
                    input("Tekan Enter untuk lanjut...")

    elif pilihan == "2":
        os.system(clear_cmd)
        print("===== REGISTER AKUN BARU =====")
        username_baru = input("Username baru: ").strip()

        sudah_dipakai = False
        for nama_akun in users:
            if nama_akun.lower() == username_baru.lower():
                sudah_dipakai = True

        if username_baru == "":
            print("username tidak boleh kosong!")
        elif " " in username_baru:
            print("username tidak boleh mengandung spasi!")
        elif sudah_dipakai:
            print("Username telah di pakai, cari yang lain ya!")
        else:
            password_baru = input("Password baru: ").strip()
            if len(password_baru) < 4:
                print("Password minimal 4 karakter!")
            else:
                users[username_baru] = {"password": password_baru, "role": "User"}
                print(f"Akun '{username_baru}' berhasil dibuat! silahkan login")
        input("Tekan Enter untuk lanjut...")

    elif pilihan == "3":
        os.system(clear_cmd)
        print("Terima kasih sudah mampir! Jaga koleksimu ya")
        program_jalan = False

    else:
        print("Pilihan tidak valid, pilih 1-3 ya!")
        input("Tekan Enter untuk lanjut...")