from datetime import datetime

import koleksi
from tampilan import tampilkan_menu
from utilitas import bersihkan_layar, jeda, pesan_error, pesan_info, tampilkan_header

def _waktu_sekarang():
    return datetime.now().strftime("%d/%m/%Y %H:%M")

def menu_admin():
    while True:
        bersihkan_layar()
        tampilkan_header("Halo admin! Mau ngapain nih hari ini")
        pesan_info(f"Waktu login: {_waktu_sekarang()}")
        tampilkan_menu([
            "Tambahkan Gantungan Kunci",
            "Lihat Semua Koleksi",
            "Ubah Koleksi",
            "Hapus Koleksi",
            "Logout",
        ])
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            koleksi.tambah_koleksi()
        elif pilihan == "2":
            koleksi.lihat_koleksi(dengan_total=True)
        elif pilihan == "3":
            koleksi.ubah_koleksi()
        elif pilihan == "4":
            koleksi.hapus_koleksi()
        elif pilihan == "5":
            pesan_info("Logout berhasil!")
            jeda()
            return
        else:
            pesan_error("Menu tidak ada, pilih 1-5 yaa!")
        jeda()

def menu_user(nama_user):
    while True:
        bersihkan_layar()
        tampilkan_header(f"Halo {nama_user}! selamat melihat lihat!")
        pesan_info(f"Waktu login: {_waktu_sekarang()}")
        tampilkan_menu([
            "Lihat Koleksi Gantungan Kunci",
            "Logout",
        ])
        pilihan = input("Pilih menu (1-2): ").strip()

        if pilihan == "1":
            koleksi.lihat_koleksi(judul="KOLEKSI GANTUNGAN KUNCI")
        elif pilihan == "2":
            pesan_info("Sampai jumpa lagi!")
            jeda()
            return
        else:
            pesan_error("menu tidak ada, pilih 1-2 yaa!")
        jeda()