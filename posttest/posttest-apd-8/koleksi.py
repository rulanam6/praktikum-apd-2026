import data
from tampilan import tampilkan_koleksi
from utilitas import (
    bersihkan_layar,
    input_harga,
    input_teks_wajib,
    pesan_error,
    pesan_info,
    pesan_sukses,
    tampilkan_header,
)

def buat_id_baru():
    data.id_terakhir += 1
    return data.id_terakhir


def nama_sudah_ada(nama, abaikan_id=None):
    for id_item, item in data.koleksi.items():
        if id_item != abaikan_id and item["nama"].lower() == nama.lower():
            return True
    return False

def pilih_id():
    try:
        nomor = int(input("Masukkan ID: ").strip())
        if nomor not in data.koleksi:
            raise KeyError(nomor)
    except ValueError:
        pesan_error("ID harus berupa angka!")
    except KeyError:
        pesan_error("ID tidak ditemukan di koleksi!")
    else:
        return nomor
    return None

def lihat_koleksi(dengan_total=False, judul="DAFTAR KOLEKSI"):
    bersihkan_layar()
    tampilkan_header(judul)
    tampilkan_koleksi(dengan_total=dengan_total)

def tambah_koleksi():
    bersihkan_layar()
    tampilkan_header("TAMBAH GANTUNGAN KUNCI")

    while True:
        nama = input_teks_wajib("Nama gantungan kunci: ")
        if nama_sudah_ada(nama):
            pesan_error("Nama itu sudah di dalam koleksi")
        else:
            break
    jenis = input_teks_wajib("Jenis gantungan kunci: ")
    harga = input_harga("Harga gantungan kunci: ")

    id_baru = buat_id_baru()
    data.koleksi[id_baru] = {"nama": nama, "jenis": jenis, "harga": harga}
    pesan_sukses(f"YEYY! '{nama}' berhasil masuk ke koleksi")

def ubah_koleksi():
    bersihkan_layar()
    tampilkan_header("UBAH KOLEKSI")
    if len(data.koleksi) == 0:
        pesan_info("Belum ada koleksi yang di ubah")
        return
    tampilkan_koleksi()
    idx = pilih_id()
    if idx is None:
        return

    item = data.koleksi[idx]
    print("(Kosongkan lalu Enter jika tidak ingin mengubah)")
    nama_baru = input(f"Nama baru  [{item['nama']}]: ").strip()
    if nama_baru != "":
        if nama_sudah_ada(nama_baru, abaikan_id=idx):
            pesan_error("Nama itu sudah dipakai, nama tidak diubah")
        else:
            item["nama"] = nama_baru

    jenis_baru = input(f"Jenis baru [{item['jenis']}]: ").strip()
    if jenis_baru != "":
        item["jenis"] = jenis_baru

    harga_baru = input_harga(f"Harga baru [{item['harga']}]: ", boleh_kosong=True)
    if harga_baru is not None:
        item["harga"] = harga_baru
    pesan_sukses("Data berhasil di perbarui")

def hapus_koleksi():
    bersihkan_layar()
    tampilkan_header("HAPUS KOLEKSI")
    if len(data.koleksi) == 0:
        pesan_info("Tidak ada koleksi yang bisa di hapus")
        return
    tampilkan_koleksi()
    idx = pilih_id()
    if idx is None:
        return
    yakin = input(f"Yakin hapus '{data.koleksi[idx]['nama']}'? (y/n): ").strip().lower()
    if yakin == "y":
        terhapus = data.koleksi.pop(idx)
        pesan_sukses(f"'{terhapus['nama']}' sudah di hapus, babayy~")
    else:
        pesan_info("gajadi di hapus, aman kok!")