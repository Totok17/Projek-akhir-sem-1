# sistem transaksi warung madura
import psycopg2 as pg
from tabulate import tabulate
import pyfiglet as pf
import os
import colorama

conn = pg.connect(host="localhost", user="postgres", password="bombigaul123", dbname="projekan")
cur = conn.cursor()

from colorama import init, Fore, Back, Style

# # Inisialisasi colorama
# init(autoreset=True)

# # Mengubah warna teks
# print(Fore.BLUE + "Teks ini berwarna biru.")

# # Mengubah warna latar belakang
# print(Back.CYAN + "Teks dengan latar belakang cyan.")

# # Menggabungkan warna teks dan latar belakang
# print(Fore.WHITE + Back.RED + "Teks putih di atas latar belakang merah.")

# # Menggunakan gaya (misalnya, tebal)
# print(Style.BRIGHT + Fore.YELLOW + "Ini adalah teks kuning yang tebal!")

# # Warna akan kembali normal secara otomatis berkat autoreset=True
# print("Teks ini kembali ke warna default.")

def tampilanawal():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    headerbagus = pf.figlet_format(header)
    print(headerbagus)
    print(Fore.WHITE)
    print("Online Transaction Application For Warung Madura")
    print(" ==============================================")
    print("Silahkan pilih peran anda")
    print("1. Admin")
    print("2. Kasir")
    print("3. Supplier")
    pilihan = input("Masukkan nomor pilihan anda : ")
    if pilihan == '1' or pilihan == 'admin':
        loginadmin()
    elif pilihan == '2' or pilihan == 'kasir':
        loginkasir()
    elif pilihan == '3' or pilihan == 'supplier':
        loginsupplier()
    else :
        input("KESALAHAN! tekan enter")
        tampilanawal()

def loginadmin():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    headerbagus = pf.figlet_format(header)
    print(headerbagus)
    print(Fore.WHITE)
    print("===============================================")
    print("                Selamat Datang                 ")
    print("===============================================")
    print("Silahkan Masukkan Username Dan Password")

    # minta input dan validasi kosong
    username = input("Masukkan username: ").strip()
    while not username:
        print("Username tidak boleh kosong.")
        username = input("Masukkan username: ").strip()

    password = input("Masukkan password: ").strip()
    while not password:
        print("Password tidak boleh kosong.")
        password = input("Masukkan password: ").strip()

    # coba cek di database; gunakan parameterized query
    try:
        cur.execute(
            "SELECT 1 FROM admin WHERE username = %s AND pass = %s",  # perbaiki 'passwod' -> 'password'
            (username, password)
        )
        result = cur.fetchone()
        if result:
            print("Login berhasil")
            admin()
        else:
            input("Username atau password salah. Tekan enter untuk mencoba lagi.")
            loginadmin()
    except Exception as e:
        print(f"Gagal memeriksa database: {e}")
        print("Menggunakan metode fallback. (contoh: username 'admin' / password 'admin')")
        if username == 'admin' and password == 'admin':
            print("Login berhasil (fallback)")
            admin()
        else:
            input("KESALAHAN! tekan enter")
            loginadmin()


def loginkasir():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    headerbagus = pf.figlet_format(header)
    print(headerbagus)
    print(Fore.WHITE)
    print("===============================================")
    print("                Selamat Datang                 ")
    print("===============================================")
    print("Silahkan Masukkan Username Dan Password")

    # minta input dan validasi kosong
    username = input("Masukkan username: ").strip()
    while not username:
        print("Username tidak boleh kosong.")
        username = input("Masukkan username: ").strip()

    password = input("Masukkan password: ").strip()
    while not password:
        print("Password tidak boleh kosong.")
        password = input("Masukkan password: ").strip()

    # coba cek di database
    try:
        cur.execute(
            "SELECT 1 FROM kasir WHERE username = %s AND passwod = %s",
            (username, password)
        )
        result = cur.fetchone()
        if result:
            print("Login berhasil")
            kasir()
        else:
            input("Username atau password salah. Tekan enter untuk mencoba lagi.")
            loginkasir()
    except Exception as e:
        print(f"Gagal memeriksa database: {e}")
        print("Menggunakan metode fallback. (contoh: username 'kasir' / password 'kasir')")
        if username == 'kasir' and password == 'kasir':
            print("Login berhasil (fallback)")
            kasir()
        else:
            input("KESALAHAN! tekan enter")
            loginkasir()

def kekosongan(x, y):
    x = input(f'{y}: ')
    while len(x.strip()) == 0:
        print(f"{y} tidak boleh kosong atau spasi")
        x = input(f'{y}: ')
        if not len(x.strip()) == 0:
            break
    return x
    

def loginsupplier():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    headerbagus = pf.figlet_format(header)
    print(headerbagus)
    print(Fore.WHITE)
    print("===============================================")
    print("                Selamat Datang                 ")
    print("===============================================")
    print("Silahkan Masukkan Username Dan Password")
    
    username = input("Masukkan username: ").strip()
    while not username:
        print("Username tidak boleh kosong.")
        username = input("Masukkan username: ").strip()

    password = input("Masukkan password: ").strip()
    while not password:
        print("Password tidak boleh kosong.")
        password = input("Masukkan password: ").strip()

    # coba cek di database
    try:
        cur.execute(
            "SELECT 1 FROM supplier WHERE username = %s AND pass = %s",
            (username, password)
        )
        result = cur.fetchone()
        if result:
            print("Login berhasil")
            supplier()
        else:
            input("Username atau password salah. Tekan enter untuk mencoba lagi.")
            loginsupplier()
    except Exception as e:
        print(f"Gagal memeriksa database: {e}")
        print("Menggunakan metode fallback. (contoh: username 'supplier' / password 'supplier')")
        if username == 'supplier' and password == 'supplier':
            print("Login berhasil (fallback)")
            supplier()
        else:
            input("KESALAHAN! tekan enter")
            loginsupplier()

def admin():
    os.system('cls')
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    headerbagus = pf.figlet_format(header)
    print(headerbagus)
    print(Fore.WHITE)
    print(" ==============================================")
    print("                   HALO ADMIN                  ")
    print(" ==============================================")
    print("Silahkan pilih fitur")
    print("1. Rekap Transaksi")
    print("2. Manajemen Produk")
    print("3. Restock")
    print("4. Keluar")
    pilihanadmin = input("Masukkan nomor pilihan anda : ")
    if pilihanadmin == '1':
        rekaptransaksi()
    elif pilihanadmin == '2':
        manajemenproduk()
    elif pilihanadmin == '3':
        restock()
    elif pilihanadmin == '4':
        keluar = input("Apakah Anda Ingin Keluar Aplikasi (y/t) ?")
        if keluar == 'y':
            input("Selamat Tinggal, tekan enter")
            os.system('cls')
        elif keluar == 't':
            admin()
        else:
            admin()
    else :
        input("KESALAHAN! tekan enter")
        admin()

def rekaptransaksi():
    os.system('cls')
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    headerbagus = pf.figlet_format(header)
    print(headerbagus)
    print(Fore.WHITE)
    print(" ==============================================")
    print("                 REKAP TRANSAKSI               ")
    print(" ==============================================")
    print("Silahkan pilih fitur")
    print("1. Rekap Penjualan")
    print("2. Rekap Keuntungan")
    print("3. Barang Terlaris")
    print("4. Kembali")
    print("5. Keluar")
    pilihanrekap = input("Masukkan nomor pilihan anda: ")
    if pilihanrekap == '1':
        rekappenjualan()
    elif pilihanrekap == '2':
        rekapkeuntungan()
    elif pilihanrekap == '3':
        barangterlaris()
    elif pilihanrekap == '4':
        admin()
    elif pilihanrekap == '5':
        keluar = input("Apakah Anda Ingin Keluar Aplikasi (y/t) ?")
        if keluar == 'y':
            input("Selamat Tinggal, tekan enter")
            os.system('cls')
        elif keluar == 't':
            rekaptransaksi()
    else :
        input("KESALAHAN! tekan enter")
        rekaptransaksi()

# def rekappenjualan():
#     if

# def rekapkeuntungan():
#     if

# def barangterlaris():
#     if


def manajemenproduk():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    headerbagus = pf.figlet_format(header)
    print(headerbagus)
    print(Fore.WHITE)
    print(" ==============================================")
    print("                MANAJEMEN PRODUK               ")
    print(" ==============================================")
    print("Silahkan pilih fitur")
    print("1. Cek Stok")
    print("2. Kategori Produk")
    print("3. Perbarui Produk")
    print("4. Kembali")
    print("5. Keluar")
    pilihanmanajemen = input("Masukkan nomor pilihan anda: ")
    if pilihanmanajemen == '1':
        cekstok()
    elif pilihanmanajemen == '2':
        kategoriproduk()
    elif pilihanmanajemen == '3':
        perbaruiproduk()
    elif pilihanmanajemen == '4':
        admin()
    elif pilihanmanajemen == '5':
        keluar = input("Apakah Anda Ingin Keluar Aplikasi (y/t) ?")
        if keluar == 'y':
            input("Selamat Tinggal, tekan enter")
            os.system('cls')
        elif keluar == 't':
            manajemenproduk()
    else :
        input("KESALAHAN! tekan enter")
        manajemenproduk()

def cekstok():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    print(pf.figlet_format(header))
    print(Fore.WHITE)
    print(" ==============================================")
    print("                   CEK STOK                    ")
    print(" ==============================================")
    try:
        cur.execute("SELECT id_produk, nama_product, harga, quantity FROM produk ORDER BY id_produk")
        rows = cur.fetchall()
        if not rows:
            print("Tidak ada data produk.")
        else:
            cols = [desc[0] for desc in cur.description]
            print(tabulate(rows, headers=cols, tablefmt="pretty", numalign="right"))
    except Exception as e:
        print(f"Error saat mengambil stok: {e}")
    input("Tekan enter untuk kembali...")
    manajemenproduk()

def kategoriproduk():
    os.system('cls')
    print(" ==============================================")
    print("                KATEGORI PRODUK                ")
    print(" ==============================================")
    print("Silahkan pilih fitur")
    print("1. Cek Kategori")
    print("2. Tambah Kategori")
    print("3. Kembali")
    print("4. Keluar")
    pilihankproduk = input("Masukkan nomor pilihan anda: ")
    if pilihankproduk == '1':
        cekkategori()
    elif pilihankproduk == '2':
        tambahkategori()
    elif pilihankproduk == '3':
        manajemenproduk()
    elif pilihankproduk == '4':
        keluar = input("Apakah Anda Ingin Keluar Aplikasi (y/t) ?")
        if keluar == 'y':
            input("Selamat Tinggal, tekan enter")
            os.system('cls')
        elif keluar == 't':
            kategoriproduk()
    else :
        input("KESALAHAN! tekan enter")
        kategoriproduk()

def cekkategori():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    print(pf.figlet_format(header))
    print(Fore.WHITE)
    print(" ==============================================")
    print("                   CEK KATEGORI                ")
    print(" ==============================================")
    try:
        cur.execute("SELECT id_kategori, kategori, deskripsi FROM kategori ORDER BY id_kategori")
        rows = cur.fetchall()
        if not rows:
            print("Tidak ada data kategori.")
        else:
            cols = [desc[0] for desc in cur.description]
            print(tabulate(rows, headers=cols, tablefmt="pretty", numalign="right"))
    except Exception as e:
        print(f"Error saat mengecek kategori: {e}")
    input("Tekan enter untuk kembali...")
    kategoriproduk()

def tambahkategori():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    print(pf.figlet_format(header))
    print(Fore.WHITE)
    print(" ==============================================")
    print("                 TAMBAH KATEGORI               ")
    print(" ==============================================")
    try:
        id_kategori = int(input("Masukkan id: ").strip())
        nama_kategori = input("Masukkan nama kategori: ").strip()
        deskripsi = input("Masukkan deskripsi kategori: ").strip()

        if not nama_kategori:
            print("Nama kategori tidak boleh kosong.")
            input("Tekan enter untuk coba lagi...")
            return tambahkategori()

        cur.execute(
            "INSERT INTO kategori (id_kategori, kategori, deskripsi) VALUES (%s, %s, %s)",
            (id_kategori, nama_kategori, deskripsi)
        )
        conn.commit()
        print("Kategori berhasil ditambahkan.")
        input("Tekan enter untuk kembali...")
        kategoriproduk()

    except ValueError:
        print("ID harus berupa angka.")
        input("Tekan enter untuk coba lagi...")
        tambahkategori()
    except Exception as e:
        print(f"Error: {e}")
        input("Tekan enter untuk kembali...")
        kategoriproduk()


def perbaruiproduk():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    headerbagus = pf.figlet_format(header)
    print(headerbagus)
    print(Fore.WHITE)
    print(" ==============================================")
    print("                PERBARUI PRODUK                ")
    print(" ==============================================")
    try:
        id_produk = int(input("Masukkan id produk: "))
        nama_produk = input("Masukkan nama produk: ").strip()
        harga = int(input("Masukkan harga: "))
        kuantitas = int(input("Masukkan kuantitas: "))
        id_supplier = int(input("Masukkan id supplier: "))
        id_kategori = int(input("Masukkan id kategori: "))
        id_admin = int(input("Masukkan id admin: "))
        
        if not nama_produk:
            print("Nama produk tidak boleh kosong.")
            input("Tekan enter untuk coba lagi...")
            perbaruiproduk()
            return
        
        cur.execute(
            """INSERT INTO produk (id_produk, nama_product, harga, quantity, id_supplier, id_kategori, id_admin)
               VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (id_produk, nama_produk, harga, kuantitas, id_supplier, id_kategori, id_admin)
        )
        conn.commit()
        print("Produk berhasil ditambahkan.")
        input("Tekan enter untuk kembali...")
        manajemenproduk()
    except ValueError:
        print("Input tidak valid. ID, harga, dan kuantitas harus berupa angka.")
        input("Tekan enter untuk coba lagi...")
        perbaruiproduk()
    except Exception as e:
        print(f"Error: {e}")
        input("Tekan enter untuk kembali...")
        manajemenproduk()



def restock():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    headerbagus = pf.figlet_format(header)
    print(headerbagus)
    print(Fore.WHITE)
    print(" ==============================================")
    print("                    RESTOCK                    ")
    print(" ==============================================")
    print("Silahkan pilih fitur")
    print("1. Tambah Stok")
    print("2. Konfirmasi Stok")
    print("3. Kembali")
    print("4. Keluar")
    pilihanrestock = input("Masukkan nomor pilihan anda: ")
    if pilihanrestock == '1':
        tambahstok()
    elif pilihanrestock == '2':
        konfirmasistok()
    elif pilihanrestock == '3':
        admin()
    elif pilihanrestock == '4':
        keluar = input("Apakah Anda Ingin Keluar Aplikasi (y/t) ?")
        if keluar == 'y':
            input("Selamat Tinggal, tekan enter")
            os.system('cls')
        elif keluar == 't':
            restock()
    else :
        input("KESALAHAN! tekan enter")
        restock()
    
def tambahstok():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    headerbagus = pf.figlet_format(header)
    print(headerbagus)
    print(Fore.WHITE)
    print(" ==============================================")
    print("                  TAMBAH STOK                  ")
    print(" ==============================================")
    try:
        id_produk = int(input("Masukkan id produk: "))
        tambah_qty = int(input("Masukkan jumlah stok yang ditambahkan: "))
        tanggal_restock = input("Masukkan tanggal restock (format: YYYY-MM-DD): ").strip()
        id_supplier = int(input("Masukkan id supplier: "))
        id_admin = int(input("Masukkan id admin: "))
        
        if tambah_qty <= 0:
            print("Jumlah stok harus lebih dari 0.")
            input("Tekan enter untuk coba lagi...")
            tambahstok()
            return
        
        # Update quantity di tabel produk
        cur.execute(
            "UPDATE produk SET quantity = quantity + %s WHERE id_produk = %s",
            (tambah_qty, id_produk)
        )
        
        # Insert ke tabel restock (jika ada)
        cur.execute(
            "INSERT INTO restock (id_produk, jumlah_restock, tanggal_restock, id_supplier, id_admin) VALUES (%s, %s, %s, %s, %s)",
            (id_produk, tambah_qty, tanggal_restock, id_supplier, id_admin)
        )
        conn.commit()
        print(f"Stok produk {id_produk} berhasil ditambahkan sebanyak {tambah_qty} unit.")
        input("Tekan enter untuk kembali...")
        restock()
    except ValueError:
        print("Input tidak valid. ID, jumlah stok harus berupa angka.")
        input("Tekan enter untuk coba lagi...")
        tambahstok()
    except Exception as e:
        print(f"Error: {e}")
        input("Tekan enter untuk kembali...")
        restock()

def konfirmasistok():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    headerbagus = pf.figlet_format(header)
    print(headerbagus)
    print(Fore.WHITE)
    print(" ==============================================")
    print("                KONFIRMASI STOK                ")
    print(" ==============================================")

def kasir():
    os.system('cls')
    print(" ==============================================")
    print("                   HALO KASIR                  ")
    print(" ==============================================")
    print("Silahkan pilih fitur")
    print("1. Konfirmasi Transaksi")
    print("2. Riwayat Transaksi")
    print("3. Keluar")
    pilihankasir = input("Masukkan nomor pilihan anda : ")
    if pilihankasir == '1':
        konfirmasitransaksi()
    elif pilihankasir == '2':
        riwayattransaksi()
    elif pilihankasir == '3':
        keluar = input("Apakah Anda Ingin Keluar Aplikasi (y/t) ?")
        if keluar == 'y':
            input("Selamat Tinggal, tekan enter")
            os.system('cls')
        elif keluar == 't':
            kasir()
        else:
            kasir()
    else :
        input("KESALAHAN! tekan enter")
        kasir()

# def konfirmasitransaksi():
#     os.system('cls')
#     header = "K'CONG"
#     print(Fore.GREEN)
#     print(pf.figlet_format(header))
#     print(Fore.WHITE)
#     print(" ==============================================")
#     print("                   TRANSAKSI                   ")
#     print(" ==============================================")
#     try:
#         id_transaksi = int(input("Masukkan id transaksi: "))
#         tanggal_transaksi = input("Masukkan tanggal (yyyy mm dd): ")
#         nama_pelanggan = input("Masukkan nama pelanggan: ").strip()
#         diskon = float(input("Masukkan diskon (persen, 0-100): "))
#         id_kasir = int(input("Masukkan id kasir: "))
        
#         if  not nama_pelanggan or not tanggal_transaksi:
#             print("Nama pelanggan dan tanggal tidak boleh kosong.")
#             input("Tekan enter untuk coba lagi...")
#             konfirmasitransaksi()
#             return
        
#         # Insert ke database
#         cur.execute(
#             "INSERT INTO transaksi (id_transaksi, tanggal_transaksi, nama_pelanggan, diskon, id_kasir) VALUES (%s, %s, %s, %s, %s)",
#             (id_transaksi, tanggal_transaksi, nama_pelanggan, diskon, id_kasir)
#         )
#         conn.commit()
#         print(f"\nTransaksi berhasil!")
#         input("Tekan enter untuk kembali...")
#         kasir()
#     except ValueError:
#         print("Input tidak valid. Pastikan kuantitas, harga, diskon adalah angka.")
#         input("Tekan enter untuk coba lagi...")
#         konfirmasitransaksi()
#     except Exception as e:
#         print(f"Error: {e}")
#         input("Tekan enter untuk kembali...")
#         kasir()
    
def konfirmasitransaksi():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    print(pf.figlet_format(header))
    print(Fore.WHITE)
    print(" ==============================================")
    print("                   TRANSAKSI                   ")
    print(" ==============================================")
    try:
        id_transaksi = int(input("Masukkan id transaksi: ").strip())
        tanggal_transaksi = input("Masukkan tanggal (yyyy-mm-dd): ").strip()
        nama_pelanggan = input("Masukkan nama pelanggan: ").strip()
        diskon = float(input("Masukkan diskon (persen, 0-100): ").strip() or 0)
        id_kasir = int(input("Masukkan id kasir: ").strip())

        if not nama_pelanggan or not tanggal_transaksi:
            print("Nama pelanggan dan tanggal tidak boleh kosong.")
            input("Tekan enter untuk coba lagi...")
            return konfirmasitransaksi()

        # insert transaksi awal dengan total 0 (akan diupdate setelah semua item)
        cur.execute(
            "INSERT INTO transaksi (id_transaksi, tanggal_transaksi, nama_pelanggan, diskon, id_kasir, total) VALUES (%s, %s, %s, %s, %s, %s)",
            (id_transaksi, tanggal_transaksi, nama_pelanggan, diskon, id_kasir, 0)
        )

        items = []
        while True:
            id_produk = int(input("Masukkan id produk (atau 0 untuk selesai): ").strip())
            if id_produk == 0:
                break

            # ambil info produk (nama, harga, stok)
            cur.execute("SELECT nama_product, harga, quantity FROM produk WHERE id_produk = %s", (id_produk,))
            produk = cur.fetchone()
            if not produk:
                print("Produk tidak ditemukan. Coba lagi.")
                continue

            nama_product_db, harga_db, stok_db = produk
            print(f"Produk: {nama_product_db} | Harga: {harga_db} | Stok: {stok_db}")
            kuantitas = int(input("Masukkan kuantitas: ").strip())

            if kuantitas <= 0:
                print("Kuantitas harus > 0.")
                continue
            if kuantitas > stok_db:
                print(f"Stok tidak cukup (tersedia {stok_db}). Kurangi kuantitas atau pilih produk lain.")
                continue

            subtotal = kuantitas * harga_db
            items.append((id_produk, nama_product_db, harga_db, kuantitas, subtotal))

            lagi = input("Tambah barang lain? (y/n): ").strip().lower()
            if lagi != 'y':
                break

        if not items:
            print("Tidak ada item transaksi. Batal.")
            # hapus transaksi sementara yang dibuat
            cur.execute("DELETE FROM transaksi WHERE id_transaksi = %s", (id_transaksi,))
            conn.commit()
            input("Tekan enter untuk kembali...")
            return kasir()

        # hitung total dan terapkan diskon
        subtotal_total = sum(i[4] for i in items)
        potongan = subtotal_total * (diskon / 100)
        total = subtotal_total - potongan

        # simpan tiap item ke tabel detail transaksi dan kurangi stok produk
        try:
            for id_p, nama_p, harga_p, qty_p, sub_p in items:
                cur.execute(
                    "INSERT INTO transaksi_items (id_transaksi, id_produk, nama_product, kuantitas, harga, subtotal) VALUES (%s, %s, %s, %s, %s, %s)",
                    (id_transaksi, id_p, nama_p, qty_p, harga_p, sub_p)
                )
                cur.execute(
                    "UPDATE produk SET quantity = quantity - %s WHERE id_produk = %s",
                    (qty_p, id_p)
                )

            # update total transaksi
            cur.execute(
                "UPDATE transaksi SET total = %s WHERE id_transaksi = %s",
                (total, id_transaksi)
            )
            conn.commit()
        except Exception as e_detail:
            conn.rollback()
            print(f"Terjadi error saat menyimpan item transaksi: {e_detail}")
            input("Tekan enter untuk kembali...")
            return kasir()

        # tampilkan ringkasan
        print("\nTransaksi berhasil!")
        print(f"Pelanggan : {nama_pelanggan}")
        print(f"Tanggal   : {tanggal_transaksi}")
        print("Rincian:")
        for it in items:
            print(f"- {it[1]} x{it[3]} @ {it[2]} = {it[4]:,.0f}")
        print(f"Subtotal  : Rp {subtotal_total:,.0f}")
        print(f"Diskon    : {diskon}% (-Rp {potongan:,.0f})")
        print(f"TOTAL     : Rp {total:,.0f}")

        input("Tekan enter untuk kembali...")
        kasir()

    except ValueError:
        print("Input tidak valid. Pastikan id/angka diisi dengan benar.")
        input("Tekan enter untuk coba lagi...")
        konfirmasitransaksi()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        input("Tekan enter untuk kembali...")
        kasir()

def riwayattransaksi():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    print(pf.figlet_format(header))
    print(Fore.WHITE)
    print(" ==============================================")
    print("               RIWAYAT TRANSAKSI               ")
    print(" ==============================================")
    try:
        cur.execute("SELECT id_transaksi, tanggal_transaksi, nama_pelanggan, diskon, id_kasir FROM transaksi ORDER BY tanggal_transaksi DESC")
        rows = cur.fetchall()
        if not rows:
            print("Tidak ada riwayat transaksi.")
        else:
            cols = [desc[0] for desc in cur.description]
            print(tabulate(rows, headers=cols, tablefmt="pretty", numalign="right"))
    except Exception as e:
        print(f"Error saat melihat riwayat transaksi: {e}")
    input("Tekan enter untuk kembali...")
    kasir()

def supplier():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    print(pf.figlet_format(header))
    print(Fore.WHITE)
    print(" ==============================================")
    print("                 HALO SUPPLIER                 ")
    print(" ==============================================")
    print("Silahkan pilih fitur")
    print("1. Konfirmasi Request")
    print("2. Pilih Jasa Pengiriman")
    print("3. Keluar")
    pilihankasir = input("Masukkan nomor pilihan anda : ")
    if pilihankasir == '1':
        konfirmasirequest()
    elif pilihankasir == '2':
        pilihjasapengiriman()
    elif pilihankasir == '3':
        keluar = input("Apakah Anda Ingin Keluar Aplikasi (y/t) ?")
        if keluar == 'y':
            input("Selamat Tinggal, tekan enter")
            os.system('cls')
        elif keluar == 't':
            supplier()
        else:
            supplier()
    else :
        input("KESALAHAN! tekan enter")
        supplier()

def konfirmasirequest():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    print(pf.figlet_format(header))
    print(Fore.WHITE)
    print(" ==============================================")
    print("               KONFIRMASI REQUEST              ")
    print(" ==============================================")
    try:
        id_pemesanan = int(input("Masukkan id pemesanan: "))
        tanggal_pemesanan = input("Masukkan tanggal pemesanan (contoh '25-11-2025'): ").strip()
        konfirmasi_pemesanan = int(input("Berikan konfirmasi (1 atau 0): ")).__bool__
        id_admin = input("Masukkan id admin: ")
        id_supplier = input("Masukkan id supplier: ") 
        id_jasa_pengiriman = input("Masukkan id jasa pengiriman: ")

        if not konfirmasi_pemesanan:
            print("Konfirmasi pemesanan tidak boleh kosong")
            input("Tekan enter untuk coba lagi...")
            konfirmasirequest()
            return

        cur.execute("""INSERT INTO pemesanan (id_pemesanan, tanggal_pemesanan, konfirmasi_pemesanan, id_admin, id_supplier, id_jasa_pengiriman)
                    VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""",
                    (id_pemesanan, tanggal_pemesanan, konfirmasi_pemesanan, id_admin, id_supplier, id_jasa_pengiriman))
        
        conn.commit()
        print("Konfirmasi berhasil ditambahkan.")
        input("Tekan enter untuk kembali...")
        supplier()
    except ValueError:
        print("Input tidak valid. ID, dan tanggal harus berupa angka, konfirmasi harus berupa boolean.")
        input("Tekan enter untuk coba lagi...")
        konfirmasirequest()
    except Exception as e:
        print(f"Error: {e}")
        input("Tekan enter untuk kembali...")
        konfirmasirequest()

def pilihjasapengiriman():
    os.system('cls')
    header = "K'CONG"
    print(Fore.GREEN)
    print(pf.figlet_format(header))
    print(Fore.WHITE)
    print(" ==============================================")
    print("             PILIH JASA PENGIRIMAN             ")
    print(" ==============================================")
    try:
        cur.execute("SELECT id_jasa_pengiriman, nama_jasa, tarif FROM jasa_pengiriman ORDER BY id_jasa_pengiriman")
        rows = cur.fetchall()
        if not rows:
            print("Tidak ada jasa pengiriman tersedia.")
        else:
            cols = [desc[0] for desc in cur.description]
            print(tabulate(rows, headers=cols, tablefmt="pretty", numalign="right"))
            
            id_jasa = int(input("\nMasukkan id jasa pengiriman yang dipilih: "))
            id_pemesanan = int(input("Masukkan id pemesanan: "))
            
            cur.execute(
                "UPDATE pemesanan SET id_jasa_pengiriman = %s WHERE id_pemesanan = %s",
                (id_jasa, id_pemesanan)
            )
            conn.commit()
            print("Jasa pengiriman berhasil dipilih.")
            input("Tekan enter untuk kembali...")
            supplier()
    except ValueError:
        print("Input tidak valid. ID harus berupa angka.")
        input("Tekan enter untuk coba lagi...")
        pilihjasapengiriman()
    except Exception as e:
        print(f"Error: {e}")
        input("Tekan enter untuk kembali...")
        supplier()

tampilanawal()


