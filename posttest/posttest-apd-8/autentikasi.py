from getpass import getpass 

try:
    import pwinput  
except ImportError:
    pwinput = None

import data
from utilitas import (
    bersihkan_layar,
    pesan_error,
    pesan_sukses,
    tampilkan_header,
)

def _baca_password(label):
    try:
        if pwinput is not None:
            return pwinput.pwinput(prompt=label, mask="*").strip()
        return getpass(label).strip()
    except (EOFError, KeyboardInterrupt):
        raise
    except Exception:
        return input(label).strip()

def proses_login(sisa):
    if sisa == 0:
        return None
    username = input("Username: ").strip()
    password = _baca_password("Password: ")
    akun = data.users.get(username)
    if akun is not None and akun["password"] == password:
        return username, akun["role"]
    pesan_error(f"Username atau Password anda salah! Sisa percobaan anda: {sisa - 1}")
    return proses_login(sisa - 1)

def login():
    bersihkan_layar()
    tampilkan_header("LOGIN")
    return proses_login(data.MAKS_PERCOBAAN)

def register():
    bersihkan_layar()
    tampilkan_header("REGISTER AKUN BARU")
    username_baru = input("Username baru: ").strip()

    sudah_dipakai = any(u.lower() == username_baru.lower() for u in data.users)
    if username_baru == "":
        pesan_error("username tidak boleh kosong!")
    elif " " in username_baru:
        pesan_error("username tidak boleh mengandung spasi!")
    elif sudah_dipakai:
        pesan_error("Username telah di pakai, cari yang lain ya!")
    else:
        password_baru = _baca_password("Password baru: ")
        if len(password_baru) < 4:
            pesan_error("Password minimal 4 karakter!")
        else:
            data.users[username_baru] = {"password": password_baru, "role": "User"}
            pesan_sukses(f"Akun '{username_baru}' berhasil dibuat! silahkan login")