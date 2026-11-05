from prettytable import PrettyTable

import data
from utilitas import format_rupiah, hitung_total_rekursif, pesan_info

def hitung_total_nilai():
    daftar_harga = [item["harga"] for item in data.koleksi.values()]
    return hitung_total_rekursif(daftar_harga)

def tampilkan_menu(daftar_menu):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Menu"]
    for nomor, teks in enumerate(daftar_menu, start=1):
        tabel.add_row([nomor, teks])
    tabel.align["Menu"] = "l"
    print(tabel)

def tampilkan_koleksi(dengan_total=False):
    if len(data.koleksi) == 0:
        pesan_info("Koleksi masih kosong, yuk belanja dulu")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Jenis", "Harga"]
    for id_item, item in data.koleksi.items():
        tabel.add_row([id_item, item["nama"], item["jenis"], format_rupiah(item["harga"])])
    tabel.align["Nama"] = "l"
    tabel.align["Jenis"] = "l"
    tabel.align["Harga"] = "r"
    print(tabel)

    if dengan_total:
        ringkasan = PrettyTable()
        ringkasan.header = False
        ringkasan.add_row(["Total Koleksi", f"{len(data.koleksi)} buah"])
        ringkasan.add_row(["Total Nilai", format_rupiah(hitung_total_nilai())])
        ringkasan.align = "l"
        print(ringkasan)