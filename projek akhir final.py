import os
import psycopg2 as pg
from tabulate import tabulate
import pyfiglet as pf
from colorama import Fore, Style, init

init(autoreset=True)

# ===========================
# KONEKSI DATABASE
# ===========================
conn = pg.connect(
    host="localhost",
    user="postgres",
    password="bombigaul123",
    dbname="PROJEK AKHIR",
    port="5432"
)
cur = conn.cursor()


# ===========================
# UTILITY
# ===========================
def header_judul(judul):
    os.system('cls')
    print(Fore.GREEN + Style.BRIGHT + pf.figlet_format("K'CONG"))
    print(Fore.WHITE + Style.BRIGHT + "=" * 45)
    print(f"{judul.center(45)}")
    print(Fore.WHITE + Style.BRIGHT + "=" * 45)


def pause():
    input("\nTekan ENTER untuk kembali...")


# ===========================
# LOGIN FUNCTION
# ===========================
def login_admin():
    header_judul("LOGIN ADMIN")
    username = input("Username: ")
    password = input("Password: ")

    query = """
        SELECT id_admin, nama 
        FROM admin_toko 
        WHERE username = %s AND pass = %s
    """
    cur.execute(query, (username, password))
    result = cur.fetchone()

    if result:
        print("Login berhasil!")
        menu_admin(result[0], result[1])
    else:
        print("Login gagal!")
        pause()


def login_kasir():
    header_judul("LOGIN KASIR")
    username = input("Username: ")
    password = input("Password: ")

    query = """
        SELECT id_kasir, nama_kasir 
        FROM kasir 
        WHERE username = %s AND pass = %s
    """
    cur.execute(query, (username, password))
    result = cur.fetchone()

    if result:
        print("Login berhasil!")
        menu_kasir(result[0], result[1])
    else:
        print("Login gagal!")
        pause()


def login_supplier():
    header_judul("LOGIN SUPPLIER")
    username = input("Username: ")
    password = input("Password: ")

    query = """
        SELECT id_supplier, nama_perusahaan 
        FROM supplier 
        WHERE username = %s AND pass = %s
    """
    cur.execute(query, (username, password))
    result = cur.fetchone()

    if result:
        print("Login berhasil!")
        menu_supplier(result[0], result[1])
    else:
        print("Login gagal!")
        pause()


# ===========================
# MENU UTAMA
# ===========================
def main_menu():
    while True:
        header_judul("MENU UTAMA")
        print("1. Login Admin")
        print("2. Login Kasir")
        print("3. Login Supplier")
        print("0. Keluar")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            login_admin()
        elif pilihan == "2":
            login_kasir()
        elif pilihan == "3":
            login_supplier()
        elif pilihan == "0":
            print("Keluar program...")
            break
        else:
            print("Pilihan tidak valid!")
            pause()
            
# ===========================
# ADMIN FEATURES
# ===========================
def menu_admin(id_admin, nama_admin):
    while True:
        header_judul(f"ADMIN - {nama_admin}")
        print("1. Entri Kategori")
        print("2. Entri Produk")
        print("3. Entri Stok (Tambah)")
        print("4. Update Harga")
        print("5. Request Stok (Buat Pemesanan)")
        print("6. Rekap Penjualan Harian")
        print("7. Barang Terlaris")
        print("8. Stok Menipis")
        print("9. Cek stok")
        print("10. cek kategori")
        print("11. Cek pemesanan")
        print("0. Logout")

        pilih = input("Pilih: ").strip()
        if pilih == '1':
            entri_kategori()
        elif pilih == '2':
            entri_produk(id_admin)
        elif pilih == '3':
            entrystok()
        elif pilih == '4':
            entri_harga()
        elif pilih == '5':
            request_stok(id_admin)
        elif pilih == '6':
            rekap_harian()
        elif pilih == '7':
            barang_terlaris()
        elif pilih == '8':
            stok_menipis()
        elif pilih == '9':
            tampilkan_stok_produk()
        elif pilih == '10':
            cek_kategori()
        elif pilih == '11':
            cek_pemesanan(id_admin)
        elif pilih == '0':
            print("Logout admin...")
            os.system('cls')
            break
        else:
            print("Pilihan tidak valid.")
            pause()


def entri_kategori():
    header_judul("ENTRI KATEGORI")
    nama = input("Nama kategori: ").strip()
    des = input("Deskripsi (opsional): ").strip() or None
    try:
        cur.execute("INSERT INTO kategori (kategori, deskripsi) VALUES (%s, %s) RETURNING id_kategori;", (nama, des))
        new_id = cur.fetchone()[0]
        conn.commit()
        print(f"Kategori '{nama}' ditambahkan (id={new_id}).")
    except Exception as e:
        conn.rollback()
        print("Error entri kategori:", e)
    pause()


def entri_produk(id_admin):
    header_judul("ENTRI PRODUK")
    nama = input("Nama produk: ").strip()
    try:
        harga = int(input("Harga jual: ").strip())
        qty = int(input("Stok awal: ").strip())
    except ValueError:
        print("Harga dan stok harus angka.")
        pause()
        return

    try:
        cur.execute("SELECT id_kategori, kategori FROM kategori;")
        krows = cur.fetchall()
        print("\nKategori:")
        print(tabulate(krows, headers=["id_kategori", "kategori"], tablefmt="pretty"))

        cur.execute("SELECT id_supplier, nama_perusahaan FROM supplier;")
        srows = cur.fetchall()
        print("\nSupplier:")
        print(tabulate(srows, headers=["id_supplier", "nama_perusahaan"], tablefmt="pretty"))
    except Exception:
        pass

    try:
        id_kategori = int(input("Pilih id_kategori: ").strip())
        id_supplier = int(input("Pilih id_supplier: ").strip())
    except ValueError:
        print("ID harus angka.")
        pause()
        return

    try:
        cur.execute("""
            INSERT INTO produk (nama_produk, harga, quantity, id_kategori, id_supplier, id_admin)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_produk;
        """, (nama, harga, qty, id_kategori, id_supplier, id_admin))
        new_id = cur.fetchone()[0]
        conn.commit()
        print(f"Produk '{nama}' berhasil ditambahkan (id={new_id}).")
    except Exception as e:
        conn.rollback()
        print("Error entri produk:", e)
    pause()


def entrystok():
    header_judul("ENTRI STOK (TAMBAH)")
    try:
        cur.execute("SELECT id_produk, nama_produk, quantity FROM produk ORDER BY id_produk;")
        produk_rows = cur.fetchall()
        print("Daftar Produk:")
        print(tabulate(produk_rows, headers=["ID Produk", "Nama Produk", "Stok"], tablefmt="pretty"))
    except Exception as e:
        print("Gagal memuat produk:", e)
        pause()
        return 

    try:
        id_prod = int(input("ID Produk: ").strip())
        tambah = int(input("Jumlah tambah: ").strip())
    except ValueError:
        print("Input harus angka.")
        pause()
        return

    try:
        cur.execute("SELECT nama_produk, quantity FROM produk WHERE id_produk = %s;", (id_prod,))
        row = cur.fetchone()
        if not row:
            print("Produk tidak ditemukan.")
            pause()
            return

        prev_qty = row[1]
        cur.execute("UPDATE produk SET quantity = quantity + %s WHERE id_produk = %s;", (tambah, id_prod))
        conn.commit()
        print(f"Stok produk id {id_prod} ({row[0]}) bertambah {tambah}. "
              f"Sebelumnya {prev_qty}, sekarang {prev_qty + tambah}.")
    except Exception as e:
        conn.rollback()
        print("Error tambah stok:", e)

    pause()



def entri_harga():
    header_judul("UPDATE HARGA PRODUK")
    try:
        id_prod = int(input("ID Produk: ").strip())
        harga_baru = int(input("Harga baru: ").strip())
    except ValueError:
        print("Input harus angka.")
        pause()
        return
    try:
        cur.execute("UPDATE produk SET harga = %s WHERE id_produk = %s;", (harga_baru, id_prod))
        conn.commit()
        print("Harga berhasil diupdate.")
    except Exception as e:
        conn.rollback()
        print("Error update harga:", e)
    pause()


def request_stok(id_admin):
    header_judul("REQUEST STOK (BUAT PEMESANAN)")

    try:
        cur.execute("SELECT id_supplier, nama_perusahaan FROM supplier;")
        srows = cur.fetchall()
        print("Supplier:")
        print(tabulate(srows, headers=["id_supplier", "nama_perusahaan"], tablefmt="pretty"))
    except Exception as e:
        print("Gagal memuat supplier:", e)
        pause()
        return

    try:
        id_supplier = int(input("Pilih id_supplier: ").strip())
    except ValueError:
        print("Input harus angka.")
        pause()
        return

    try:
        cur.execute("SELECT id_produk, nama_produk FROM produk ORDER BY id_produk;")
        prows = cur.fetchall()
        print("\nDaftar Produk:")
        print(tabulate(prows, headers=["id_produk", "nama_produk"], tablefmt="pretty"))
    except Exception as e:
        print("Gagal memuat produk:", e)
        pause()
        return

    items = []
    while True:
        try:
            pid = int(input("ID Produk (0 selesai): ").strip())
        except ValueError:
            print("ID produk harus angka.")
            continue

        if pid == 0:
            break

        try:
            qty = int(input("Jumlah: ").strip())
        except ValueError:
            print("Jumlah harus angka.")
            continue

        items.append((pid, qty))

    if not items:
        print("Tidak ada item. Batal.")
        pause()
        return

    try:
        cur.execute("""
            INSERT INTO pemesanan 
                (tanggal_pemesanan, konfirmasi_pemesanan, tanggal_pesanan_sampai,
                 id_admin, id_supplier, id_jasa_pengiriman)
            VALUES 
                (CURRENT_DATE, FALSE, NULL, %s, %s, NULL)
            RETURNING id_pemesanan;
        """, (id_admin, id_supplier))

        id_pem = cur.fetchone()[0]

        for pid, qty in items:
            cur.execute("""
                INSERT INTO detail_pemesanan (id_pemesanan, id_produk, quantity, harga)
                VALUES (%s, %s, %s, NULL);
            """, (id_pem, pid, qty))

        conn.commit()
        print(f"Pemesanan dibuat dengan ID {id_pem}. Supplier akan mengisi harga & memilih jasa pengiriman.")
    except Exception as e:
        conn.rollback()
        print("Error membuat pemesanan:", e)

    pause()
    
def rekap_harian():
    header_judul("REKAP PENJUALAN HARIAN")
    try:
        cur.execute("""
           SELECT 
           t.id_transaksi,
           t.tanggal_transaksi,
           p.nama_produk,
           dt.quantity,
           dt.harga AS harga_satuan,
           (dt.quantity * dt.harga) AS total_harga
           FROM transaksi t
           JOIN detail_transaksi dt ON t.id_transaksi = dt.id_transaksi
           JOIN produk p ON p.id_produk = dt.id_produk
           WHERE t.tanggal_transaksi = CURRENT_DATE
           ORDER BY t.id_transaksi;
        """)
        rows = cur.fetchall()
        if rows:
            print(tabulate(rows, headers=[d[0] for d in cur.description], tablefmt="pretty", numalign="right"))
        else:
            print("Belum ada transaksi hari ini.")
    except Exception as e:
        print("Error rekap harian:", e)
    pause()


def barang_terlaris(limit=10):
    header_judul("BARANG TERLARIS")
    try:
        cur.execute("""
            SELECT p.id_produk, p.nama_produk, COALESCE(SUM(dt.quantity),0) AS total_terjual
            FROM produk p
            LEFT JOIN detail_transaksi dt ON dt.id_produk = p.id_produk
            GROUP BY p.id_produk, p.nama_produk
            ORDER BY total_terjual DESC
            LIMIT %s;
        """, (limit,))
        rows = cur.fetchall()
        if rows:
            print(tabulate(rows, headers=[d[0] for d in cur.description], tablefmt="pretty", numalign="right"))
        else:
            print("Belum ada data transaksi.")
    except Exception as e:
        print("Error barang terlaris:", e)
    pause()


def stok_menipis(threshold=5):
    header_judul("PRODUK STOK MENIPIS")
    try:
        cur.execute("SELECT id_produk, nama_produk, quantity FROM produk WHERE quantity <= %s ORDER BY quantity ASC;", (threshold,))
        rows = cur.fetchall()
        if rows:
            print(tabulate(rows, headers=[d[0] for d in cur.description], tablefmt="pretty", numalign="right"))
        else:
            print("Tidak ada produk dengan stok menipis.")
    except Exception as e:
        print("Error stok menipis:", e)
    pause()
    
def tampilkan_stok_produk():
    os.system('cls')
    print(Fore.GREEN + pf.figlet_format("DAFTAR STOK") + Fore.WHITE)

    query = """
        SELECT 
            p.id_produk,
            p.nama_produk,
            k.kategori,
            p.harga,
            p.quantity
        FROM produk p
        JOIN kategori k ON k.id_kategori = p.id_kategori
        ORDER BY p.id_produk;
    """

    cur.execute(query)
    data = cur.fetchall()

    headers = ["ID", "Nama Produk", "Kategori", "Harga", "Quantity"]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
    input("\nTekan Enter untuk kembali...")

def cek_kategori():
    os.system('cls')
    print(Fore.GREEN + pf.figlet_format("CEK KATEGORI") + Fore.WHITE)

    query = """
        SELECT 
            id_kategori,
            kategori,
            deskripsi
        FROM kategori
        ORDER BY id_kategori;
    """

    cur.execute(query)
    data = cur.fetchall()

    headers = ["ID Kategori", "Kategori", "Deskripsi"]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
    input("\nTekan Enter untuk kembali...")

def cek_pemesanan(id_supplier):
    import os
    os.system('cls')
    print(Fore.GREEN + pf.figlet_format("CEK PEMESANAN") + Fore.WHITE)

    query = """
        SELECT 
            p.id_pemesanan,
            TO_CHAR(p.tanggal_pemesanan, 'YYYY-MM-DD') AS tanggal_pesan,
            COALESCE(TO_CHAR(p.tanggal_pesanan_sampai, 'YYYY-MM-DD'), '-') AS tanggal_sampai,
            pr.nama_produk,
            dp.quantity AS quantity_dipesan,
            COALESCE(dp.harga, 0) AS harga_per_unit,
            (dp.quantity * COALESCE(dp.harga, 0)) AS total_harga,
            CASE 
                WHEN dp.harga IS NULL THEN 'BELUM DIKONFIRMASI'
                ELSE 'SUDAH DIKONFIRMASI'
            END AS status
        FROM pemesanan p
        JOIN supplier s ON s.id_supplier = p.id_supplier
        JOIN detail_pemesanan dp ON dp.id_pemesanan = p.id_pemesanan
        JOIN produk pr ON pr.id_produk = dp.id_produk
        WHERE p.id_supplier = %s AND p.tanggal_pesanan_sampai > tanggal_pemesanan
        ORDER BY p.tanggal_pemesanan DESC;
    """

    try:
        cur.execute(query, (id_supplier,))
        rows = cur.fetchall()

        headers = [
            "ID Pemesanan",
            "Tgl Pesan",
            "Tgl Sampai",
            "Nama Produk",
            "Qty",
            "Harga / Unit",
            "Total Harga",
            "Status"
        ]

        if rows:
            print(tabulate(rows, headers=headers, tablefmt="fancy_grid", numalign="left"))
        else:
            print("Tidak ada pemesanan untuk supplier ini.")

    except Exception as e:
        print("Error mengambil data pemesanan:", e)

    input("\nTekan Enter untuk kembali...")
# ===========================
# KASIR FEATURES
# ===========================
def menu_kasir(id_kasir, nama_kasir):
    while True:
        header_judul(f"KASIR - {nama_kasir}")
        print("1. Transaksi Penjualan")
        print("2. Barang Terlaris")
        print("3. Stok Menipis")
        print("0. Logout")
        pilih = input("Pilih: ").strip()
        if pilih == '1':
            transaksi_kasir(id_kasir)
        elif pilih == '2':
            barang_terlaris()
        elif pilih == '3':
            stok_menipis()
        elif pilih == '0':
            break
        else:
            print("Pilihan tidak valid.")
            pause()


def transaksi_kasir(id_kasir):
    os.system("cls")
    header_judul("TRANSAKSI PENJUALAN")

    print("\n=== Daftar Produk ===")
    try:
        cur.execute("""
            SELECT id_produk, nama_produk, harga, quantity
            FROM produk
            ORDER BY id_produk;
        """)
        rows = cur.fetchall()
        print(tabulate(rows, headers=["ID", "Nama Produk", "Harga", "Stok"], tablefmt="pretty"))
    except Exception as e:
        print("Error mengambil produk:", e)
        pause()
        return

    nama_pelanggan = input("\nNama Pelanggan: ").strip()

    keranjang = []
    total = 0

    while True:
        try:
            id_prod = int(input("\nID Produk (0 untuk selesai): ").strip())
        except ValueError:
            print("Masukkan angka yang valid.")
            continue

        if id_prod == 0:
            break

        cur.execute("SELECT nama_produk, harga, quantity FROM produk WHERE id_produk = %s;", (id_prod,))
        prod = cur.fetchone()

        if not prod:
            print("Produk tidak ditemukan.")
            continue

        nama_p, harga_p, stok_p = prod

        print(f"Nama Produk : {nama_p}")
        print(f"Harga       : {harga_p}")
        print(f"Stok        : {stok_p}")

        try:
            qty = int(input("Jumlah Beli: ").strip())
        except ValueError:
            print("Jumlah harus angka.")
            continue

        if qty > stok_p:
            print(f"Stok tidak cukup!, Stok tersedia: {stok_p}")
            continue

        subtotal = harga_p * qty
        total += subtotal

        keranjang.append((id_prod, nama_p, qty, harga_p, subtotal))

        print(f"Ditambahkan! Subtotal: Rp{subtotal}")

    if not keranjang:
        print("\nTidak ada barang dibeli. Transaksi dibatalkan.")
        pause()
        return

    print("\n=== RINGKASAN PEMBELIAN ===")
    print(tabulate(keranjang, headers=["ID", "Produk", "Qty", "Harga", "Subtotal"], tablefmt="pretty"))
    print(f"TOTAL AKHIR: Rp {total}")

    konfirmasi = input("\nProses transaksi? (y/n): ").lower()
    if konfirmasi != "y":
        print("Transaksi dibatalkan.")
        pause()
        return

    try:
        cur.execute("""
            INSERT INTO transaksi (tanggal_transaksi, nama_pelanggan, id_kasir)
            VALUES (CURRENT_DATE, %s, %s) RETURNING id_transaksi;
        """, (nama_pelanggan, id_kasir))

        id_trans = cur.fetchone()[0]

        for item in keranjang:
            id_prod, nama_p, qty, harga_p, subtotal = item

            cur.execute("""
                INSERT INTO detail_transaksi (id_transaksi, id_produk, quantity, harga)
                VALUES (%s, %s, %s, %s);
            """, (id_trans, id_prod, qty, harga_p))

            cur.execute("""
                UPDATE produk
                SET quantity = quantity - %s
                WHERE id_produk = %s;
            """, (qty, id_prod))

        conn.commit()
        print(f"\n✔ Transaksi berhasil! ID Transaksi: {id_trans}")

    except Exception as e:
        conn.rollback()
        print("Error menyimpan transaksi:", e)

    pause()
    
    

# ===========================
# SUPPLIER FEATURES
# ===========================
def menu_supplier(id_supplier, nama_supplier):
    while True:
        header_judul(f"MENU SUPPLIER - {nama_supplier}")
        print("1. Lihat Request Pemesanan")
        print("2. Konfirmasi Request & Input Harga + Pilih Jasa")
        print("0. Logout")
        pilih = input("Pilih menu: ")

        if pilih == '1':
            supplier_lihat_request(id_supplier)
        elif pilih == '2':
            supplier_input_harga(id_supplier) 
        elif pilih == '0':
            break
        else:
            print("Pilihan tidak valid.")
            
def supplier_lihat_request(id_supplier):
    header_judul("DAFTAR REQUEST MASUK")
    cur.execute(""" 
        SELECT p.id_pemesanan, pr.nama_produk,
        TO_CHAR(p.tanggal_pemesanan, 'YYYY-MM-DD') AS tanggal_request,
        COALESCE(TO_CHAR(p.tanggal_pesanan_sampai, 'YYYY-MM-DD'), '-') AS tanggal_terima,
        CASE WHEN p.konfirmasi_pemesanan = TRUE THEN 'TRUE' ELSE 'FALSE' END AS status
        FROM pemesanan p JOIN detail_pemesanan dp ON p.id_pemesanan = dp.id_pemesanan 
        JOIN produk pr ON dp.id_produk = pr.id_produk 
        WHERE p.id_supplier = %s 
        ORDER BY p.id_pemesanan; 
    """, (id_supplier,)) 
    
    rows = cur.fetchall() 
    print(tabulate(rows, headers=["ID", "Produk", "Tgl Request", "Tgl Terima", "Status"], tablefmt="pretty")) 
    pause()
    
    
    
def supplier_input_harga(id_supplier):
    header_judul("KONFIRMASI REQUEST & INPUT HARGA")

    # Tampilkan daftar pesanan yang belum dikonfirmasi
    print("📌 DAFTAR REQUEST YANG BELUM DIKONFIRMASI")
    cur.execute("""
        SELECT p.id_pemesanan, pr.nama_produk, dp.quantity, 
               TO_CHAR(p.tanggal_pemesanan, 'YYYY-MM-DD') AS tgl_request
        FROM pemesanan p
        JOIN detail_pemesanan dp ON p.id_pemesanan = dp.id_pemesanan
        JOIN produk pr ON dp.id_produk = pr.id_produk
        WHERE p.id_supplier = %s
          AND p.konfirmasi_pemesanan = FALSE
        ORDER BY p.id_pemesanan;
    """, (id_supplier,))
    pending = cur.fetchall()

    if not pending:
        print("Tidak ada request yang menunggu konfirmasi.")
        pause()
        return  # kembali ke menu sebelumnya

    print(tabulate(pending, headers=["ID Pemesanan", "Produk", "Qty", "Tgl Request"], tablefmt="pretty"))

    # Input ID pemesanan
    try:
        id_pem = int(input("\nMasukkan ID Pemesanan yang ingin dikonfirmasi: ").strip())
    except ValueError:
        print("❌ ID harus berupa angka!")
        pause()
        return

    # Cek apakah ID valid & memang belum dikonfirmasi
    cur.execute("""
        SELECT 1 FROM pemesanan 
        WHERE id_pemesanan = %s AND id_supplier = %s AND konfirmasi_pemesanan = FALSE
    """, (id_pem, id_supplier))
    if not cur.fetchone():
        print("❌ ID Pemesanan tidak valid atau sudah dikonfirmasi sebelumnya.")
        pause()
        return

    # Ambil item dalam pemesanan
    cur.execute("""
        SELECT dp.id_produk, pr.nama_produk, dp.quantity
        FROM detail_pemesanan dp
        JOIN produk pr ON dp.id_produk = pr.id_produk
        WHERE dp.id_pemesanan = %s;
    """, (id_pem,))
    items = cur.fetchall()

    print("\n📦 ITEM DALAM PEMESANAN")
    print(tabulate(items, headers=["ID Produk", "Produk", "Qty"], tablefmt="pretty"))

    # Input harga masing-masing produk
    for pid, nama, qty in items:
        try:
            harga = int(input(f"Harga per unit untuk {nama} (qty {qty}): ").strip())
            cur.execute("""
                UPDATE detail_pemesanan
                SET harga = %s
                WHERE id_pemesanan = %s AND id_produk = %s;
            """, (harga, id_pem, pid))
        except Exception:
            conn.rollback()
            print("❌ Input harga tidak valid, transaksi dibatalkan.")
            pause()
            return

    # Pilih jasa pengiriman
    print("\n--- PILIH JASA PENGIRIMAN ---")
    cur.execute("SELECT id_jasa_pengiriman, nama_jasa FROM jasa_pengiriman;")
    jasa = cur.fetchall()
    print(tabulate(jasa, headers=["ID Jasa", "Nama Jasa"], tablefmt="pretty"))

    try:
        id_jasa = int(input("Pilih jasa: ").strip())
        cur.execute("SELECT 1 FROM jasa_pengiriman WHERE id_jasa_pengiriman = %s", (id_jasa,))
        if not cur.fetchone():
            raise ValueError
    except:
        conn.rollback()
        print("❌ ID Jasa tidak valid, transaksi dibatalkan.")
        pause()
        return

    est = input("Estimasi tanggal sampai (YYYY-MM-DD): ").strip()

    try:
        cur.execute("""
            UPDATE pemesanan
            SET konfirmasi_pemesanan = TRUE,
                id_jasa_pengiriman = %s,
                tanggal_pesanan_sampai = %s
            WHERE id_pemesanan = %s AND id_supplier = %s;
        """, (id_jasa, est, id_pem, id_supplier))
    except:
        conn.rollback()
        print(" Tanggal tidak valid, transaksi dibatalkan.")
        pause()
        return

    conn.commit()
    print("\n✅ Request berhasil dikonfirmasi & harga tersimpan.")
    pause()

# ===========================
# PROGRAM ENTRY POINT (override main_menu to use)
# ===========================
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nKeluar (Ctrl+C).")
    finally:
        try:
            cur.close()
            conn.close()
        except Exception:
            pass