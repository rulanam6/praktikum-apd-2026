import os

from colorama import Fore, Style, init
init(autoreset=True)

CLEAR_CMD = "cls" if os.name == "nt" else "clear"

def bersihkan_layar():
    os.system(CLEAR_CMD)

def tampilkan_header(judul, lebar=45):
    print(Fore.CYAN + "=" * lebar)
    print(Fore.CYAN + Style.BRIGHT + f"  {judul}")
    print(Fore.CYAN + "=" * lebar)

def jeda():
    try:
        input(Style.DIM + "Tekan Enter untuk lanjut...")
    except EOFError:
        pass

def pesan_sukses(teks):
    print(Fore.GREEN + teks)

def pesan_error(teks):
    print(Fore.RED + teks)

def pesan_info(teks):
    print(Fore.YELLOW + teks)

def format_rupiah(angka):
    return "Rp" + f"{angka:,}".replace(",", ".")

def input_teks_wajib(label):
    while True:
        try:
            teks = input(label).strip()
            if teks == "":
                raise ValueError("Input tidak boleh kosong!")
        except ValueError as e:
            pesan_error(str(e))
        else:
            return teks

def input_harga(label, boleh_kosong=False):
    while True:
        try:
            teks = input(label).strip()
            if teks == "" and boleh_kosong:
                return None
            harga = int(teks)
            if harga <= 0:
                raise ValueError
        except ValueError:
            pesan_error("Harga harus berupa angka bulat lebih dari 0!")
        else:
            return harga

def hitung_total_rekursif(daftar_harga, indeks=0):
    if indeks >= len(daftar_harga):
        return 0
    return daftar_harga[indeks] + hitung_total_rekursif(daftar_harga, indeks + 1)