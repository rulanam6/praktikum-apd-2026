def login(username, password):
    print(f"Memverifikasi akun {username}...")
    if username == "admin" and password == "123":
        return True
    return False

if __name__ == "__main__":
    print("Menguji fungsi login:", login("admin", "123"))