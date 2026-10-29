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
MAKS_PERCOBAAN = 3

def bersihkan_layar():
    """Prosedur tanpa parameter: membersihkan layar."""
    os.system(clear_cmd)

def tampilkan_header(judul, lebar=45):
    """Prosedur dengan parameter: mencetak judul berbingkai."""
    print("=" * lebar)
    print(f"  {judul}")
    print("=" * lebar)

def jeda():
    """Prosedur: menunggu Enter (aman dari EOFError)."""
    try:
        input("Tekan Enter untuk lanjut...")
    except EOFError:
        pass

def tampilkan_koleksi(dengan_total=False):
    """Prosedur: mencetak tabel koleksi."""
    if len(koleksi) == 0:
        print("Koleksi masih kosong, yuk belanja dulu")
        return
    print(f"{'ID':<4}{'Nama':<22}{'Jenis':<14}{'Harga':>12}")
    print("-" * 52)
    for id_item, data in koleksi.items():
        print(f"{id_item:<4}{data['nama']:<22}{data['jenis']:<14}{format_rupiah(data['harga']):>12}")
    if dengan_total:
        print("-" * 52)
        print(f"Total Koleksi: {len(koleksi)} buah")
        print(f"Total nilai  : {format_rupiah(hitung_total_nilai())}")

def buat_id_baru():
    """Fungsi tanpa parameter: menaikkan id global lalu mengembalikannya."""
    global id_terakhir
    id_terakhir += 1
    return id_terakhir

def hitung_total_nilai():
    """Fungsi tanpa parameter: total harga semua koleksi (memakai rekursi)."""
    daftar_harga = [data["harga"] for data in koleksi.values()]
    return hitung_total_rekursif(daftar_harga, 0)

def pilih_id():
    """Fungsi tanpa parameter: meminta ID valid, None jika tidak valid."""
    try:
        nomor = int(input("Masukkan ID: ").strip())
        if nomor not in koleksi:
            raise KeyError(nomor)
    except ValueError:
        print("ID harus berupa angka!")
    except KeyError:
        print("ID tidak ditemukan di koleksi!")
    else:
        return nomor  # else: hanya jalan jika try sukses tanpa error
    return None

def format_rupiah(angka):
    """Fungsi dengan parameter: 15000 -> 'Rp15.000'."""
    return "Rp" + f"{angka:,}".replace(",", ".")

def nama_sudah_ada(nama, abaikan_id=None):
    """Fungsi dengan parameter: cek nama kembar (opsional abaikan 1 ID)."""
    for id_item, data in koleksi.items():
        if id_item != abaikan_id and data["nama"].lower() == nama.lower():
            return True
    return False

def input_teks_wajib(label):
    """Fungsi dengan parameter: input teks yang tidak boleh kosong."""
    while True:
        try:
            teks = input(label).strip()
            if teks == "":
                raise ValueError("Input tidak boleh kosong!")
        except ValueError as e:
            print(e)
        else:
            return teks

def input_harga(label, boleh_kosong=False):
    """Fungsi dengan parameter: input harga bilangan bulat > 0."""
    while True:
        try:
            teks = input(label).strip()
            if teks == "" and boleh_kosong:
                return None
            harga = int(teks)  # ValueError otomatis jika bukan angka
            if harga <= 0:
                raise ValueError("Harga harus lebih dari 0!")
        except ValueError:
            print("Harga harus berupa angka bulat lebih dari 0!")
        else:
            return harga

def hitung_total_rekursif(daftar_harga, indeks):
    """Rekursif: menjumlahkan daftar harga dari indeks ke akhir."""
    if indeks >= len(daftar_harga):  # base case
        return 0
    return daftar_harga[indeks] + hitung_total_rekursif(daftar_harga, indeks + 1)

def proses_login(sisa):
    """Rekursif: login diulang sampai berhasil atau percobaan habis."""
    if sisa == 0:  # base case: percobaan habis
        return None
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    akun = users.get(username)
    if akun is not None and akun["password"] == password:
        return username, akun["role"]
    print(f"Username atau Password anda salah! Sisa percobaan anda: {sisa - 1}")
    return proses_login(sisa - 1)

def tambah_koleksi():
    bersihkan_layar()
    tampilkan_header("TAMBAH GANTUNGAN KUNCI")

    while True:
        nama = input_teks_wajib("Nama gantungan kunci: ")
        if nama_sudah_ada(nama):
            print("Nama itu sudah di dalam koleksi")
        else:
            break
    jenis = input_teks_wajib("Jenis gantungan kunci: ")
    harga = input_harga("Harga gantungan kunci: ")

    id_baru = buat_id_baru()
    koleksi[id_baru] = {"nama": nama, "jenis": jenis, "harga": harga}
    print(f"YEYY! '{nama}' berhasil masuk ke koleksi")

def ubah_koleksi():
    bersihkan_layar()
    tampilkan_header("UBAH KOLEKSI")
    if len(koleksi) == 0:
        print("Belum ada koleksi yang di ubah")
        return
    tampilkan_koleksi()
    idx = pilih_id()
    if idx is None:
        return

    print("(Kosongkan lalu Enter jika tidak ingin mengubah)")
    nama_baru = input(f"Nama baru  [{koleksi[idx]['nama']}]: ").strip()
    if nama_baru != "":
        if nama_sudah_ada(nama_baru, abaikan_id=idx):
            print("Nama itu sudah dipakai, nama tidak diubah")
        else:
            koleksi[idx]["nama"] = nama_baru

    jenis_baru = input(f"Jenis baru [{koleksi[idx]['jenis']}]: ").strip()
    if jenis_baru != "":
        koleksi[idx]["jenis"] = jenis_baru

    harga_baru = input_harga(f"Harga baru [{koleksi[idx]['harga']}]: ", boleh_kosong=True)
    if harga_baru is not None:
        koleksi[idx]["harga"] = harga_baru
    print("Data berhasil di perbarui")

def hapus_koleksi():
    bersihkan_layar()
    tampilkan_header("HAPUS KOLEKSI")
    if len(koleksi) == 0:
        print("Tidak ada koleksi yang bisa di hapus")
        return
    tampilkan_koleksi()
    idx = pilih_id()
    if idx is None:
        return
    yakin = input(f"Yakin hapus '{koleksi[idx]['nama']}'? (y/n): ").strip().lower()
    if yakin == "y":
        terhapus = koleksi.pop(idx)
        print(f"'{terhapus['nama']}' sudah di hapus, babayy~")
    else:
        print("gajadi di hapus, aman kok!")

def menu_admin():
    while True:
        bersihkan_layar()
        tampilkan_header("Halo admin! Mau ngapain nih hari ini")
        print("1. Tambahkan Gantungan Kunci")
        print("2. Lihat Semua Koleksi")
        print("3. Ubah Koleksi")
        print("4. Hapus Koleksi")
        print("5. Logout")
        menu = input("Pilih menu (1-5): ").strip()

        if menu == "1":
            tambah_koleksi()
        elif menu == "2":
            bersihkan_layar()
            tampilkan_header("DAFTAR KOLEKSI")
            tampilkan_koleksi(dengan_total=True)
        elif menu == "3":
            ubah_koleksi()
        elif menu == "4":
            hapus_koleksi()
        elif menu == "5":
            print("Logout berhasil!")
            jeda()
            return
        else:
            print("Menu tidak ada, pilih 1-5 yaa!")
        jeda()

def menu_user(nama_user):
    while True:
        bersihkan_layar()
        tampilkan_header(f"Halo {nama_user}! selamat melihat lihat!")
        print("1. Lihat Koleksi Gantungan Kunci")
        print("2. Logout")
        menu = input("Pilih menu (1-2): ").strip()

        if menu == "1":
            bersihkan_layar()
            tampilkan_header("KOLEKSI GANTUNGAN KUNCI")
            tampilkan_koleksi()
        elif menu == "2":
            print("Sampai jumpa lagi!")
            jeda()
            return
        else:
            print("menu tidak ada, pilih 1-2 yaa!")
        jeda()

def register():
    bersihkan_layar()
    tampilkan_header("REGISTER AKUN BARU")
    username_baru = input("Username baru: ").strip()

    sudah_dipakai = any(u.lower() == username_baru.lower() for u in users)
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

def login():
    bersihkan_layar()
    tampilkan_header("LOGIN")
    hasil = proses_login(MAKS_PERCOBAAN)
    if hasil is None:
        print("Mohon maaf, anda gagal login, silahkan kembali ke menu utama")
        jeda()
        return
    user_aktif, role_aktif = hasil
    if role_aktif == "Admin":
        menu_admin()
    else:
        menu_user(user_aktif)

def main():
    while True:
        bersihkan_layar()
        tampilkan_header("Koleksi Gantungan Kunci")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilihan = input("Pilih menu (1-3): ").strip()
        if pilihan == "1":
            login()
        elif pilihan == "2":
            register()
            jeda()
        elif pilihan == "3":
            bersihkan_layar()
            print("Terima kasih sudah mampir! Jaga koleksimu ya")
            return
        else:
            print("Pilihan tidak valid, pilih 1-3 ya!")
            jeda()

try:
    main()
except KeyboardInterrupt:
    print("\nProgram dihentikan paksa (Ctrl+C). Sampai jumpa!")
except EOFError:
    print("\nInput terputus. Program ditutup.")
finally:
    print("Program selesai.")