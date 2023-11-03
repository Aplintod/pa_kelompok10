import os
import json
import pwinput
from prettytable import PrettyTable
os.system('cls')

json_path_nonfiksi = 'C:/Users/ACER/Documents/Tugas/PAGACOR Revisi/nonfiksi.json'
json_path_fiksi = 'C:/Users/ACER/Documents/Tugas/PAGACOR Revisi/fiksi.json'
json_path_DataAdmin = 'C:/Users/ACER/Documents/Tugas/PAGACOR Revisi/DataAdmin.json'
json_path_DataUser = 'C:/Users/ACER/Documents/Tugas/PAGACOR Revisi/DataUser.json'

with open(json_path_nonfiksi,"r") as nonfiksi:
    nonfi = json.loads(nonfiksi.read())
with open(json_path_fiksi, "r") as fiksi:
    fi = json.loads(fiksi.read())
with open(json_path_DataAdmin,"r") as DataAdmin:
    admin = json.loads(DataAdmin.read())
with open(json_path_DataUser,"r") as DataUser:
    pengguna = json.loads(DataUser.read())
    
    
    
def clear() :
    os.system('cls')


def register():
    
    while True :
            clear
            tidakada = True
            print("Silahkan Register Terlebih Dahulu")
            username = input("Masukkan Username : ").lower().strip()
            if all (x.isspace()for x in username):
                print("Username Tidak boleh berisi spasi")
                break
            for user in pengguna :
                if username in user["username"] :
                    clear()
                    print("Username Sudah Ada")
                    tidakada = False
                    return register()
            for pengurus in admin :
                if username in pengurus["namadmin"] :
                    clear()
                    print("Username Sudah Ada")
                    tidakada = False
                    return register()
            if tidakada == True and all (x.isalpha()for x in username) :
                min_pw = 8
                max_pw = 20
                password = pwinput.pwinput("Masukkan password: ").strip()
                limit_pw = len(password)
                
                if password == "" :
                    clear()
                    print("Password Tidak Boleh Kosong")
                if all (x.isspace()for x in password):
                    clear()
                    print("Password Tidak Boleh berisi Spasi")
                if min_pw <= limit_pw <= max_pw :
                    clear()
                    print("Password Benar, Akun Berhasil Dibuat")
                    akun_baru = {"username": username, "password": password, "emoney": 0}
                    pengguna.append(akun_baru)
                    with open(json_path_DataUser, 'w') as su:
                        json.dump(pengguna, su, indent=4)
                    return menu_1()
                else :
                    clear()
                    print("Password Min 8 Max 20 Karakter")


def login():
    global username
    ada = True
    print("Login:")
    username = input("Masukkan Username: ").lower().strip()
    password = pwinput.pwinput("Masukkan Password: ")
    
    for user in pengguna :
        if username in user["username"]:
            ada = True
            if password in user["password"] :
                clear()
                print("LOGIN BERHASIL\n")
                userpage()
            else :
                print("Password salah")
        if ada == False :
            print("Akun Anda Tidak Terdaftar, Silahkan registrasi terlebih dahulu")
            
    for pengurus in admin :
        if username in pengurus["namadmin"]:
            ada = True
            if password in pengurus["pwadmin"] :
                clear()
                print("LOGIN BERHASIL\n")
                adminpage()
            else :
                print("Password salah")
            
            
def userpage():
    while True:
        try :
            print("-"*50)
            print("Menu User :\n")
            print("1. Sewa Buku")
            print("2. Lihat Saldo E-Money")
            print("3. Top Up Saldo")
            print("4. Keluar")

            print("-"*50)
            userchoice = int(input("Pilih Opsi Menu : "))
            print("-"*50)

            if userchoice == 1:
                transaksi()
            elif userchoice == 2:
                ceksaldo_emoney()
            elif userchoice == 3:
                topup_emoney()
            elif userchoice == 4:
                break
            else:
                print("Pilihan Tidak Valid, Coba Lagi!")
        except ValueError :
            print("Input Harus Berupa Angka")
        
def daftar_buku():
    table_fiksi = PrettyTable()
    table_fiksi.field_names = ["ID", "Buku Fiksi", "Penulis Buku", "Stok", "Harga Sewa Seminggu"]
    for fiksi in fi:
        table_fiksi.add_row(fiksi)
    print(table_fiksi)

    table_nf = PrettyTable()
    table_nf.field_names = ["ID", "Buku Non FIksi", "Penulis Buku", "Stok", "Harga Sewa Seminggu"]
    for nonfiksi in nonfi:
        table_nf.add_row(nonfiksi)
    print(table_nf)


def tambah_buku():
    try :
        daftar_buku()
        print("Menu Tambah Buku\n")
        print("1. Tambah Buku Fiksi")
        print("2. Tambah Buku Non-Fiksi\n")
        booktype = (input("Pilih Jenis Buku : "))
        if booktype == "1" :
            bookid = input("ID Buku")
            booktitle = input("Judul Buku : ")
            bookauthor = input("Penulis Buku : ")
            bookstock = int(input("Stock Buku : "))
            price = float(input("Harga Sewa Seminggu : "))
            buku_baru = [bookid, booktitle, bookauthor, bookstock, price]
            fi.append(buku_baru)
            with open (json_path_fiksi,"w") as sn:
                json.dump(fi,sn, indent=4)
            
            print("Buku Telah Ditambahkan")

        elif booktype == "2":
            bookid = input("ID")
            booktitle = input("Judul Buku : ")
            bookauthor = input("Penulis Buku : ")
            bookstock = int(input("Stock Buku : "))
            price = float(input("Harga Sewa Seminggu : "))
            buku_baru = [bookid, booktitle, bookauthor, bookstock, price]
            nonfi.append(buku_baru)
            with open (json_path_nonfiksi,"w") as sn:
                json.dump(nonfi,sn, indent=4)
        
        else :
            print("Input Tidak Sesuai")
    except ValueError :
            print("Input Tidak Sesuai")

def lihat_buku():
    daftar_buku()

def update_buku():
    clear()
    print("Menu Update Buku\n")
    daftar_buku()
    id_buku = input("Masukkan ID Buku yang ingin diubah: ")

    for i in range(len(fi)):
        if fi[i][0] == id_buku:
            print(f"Buku Fiksi ID {id_buku} ditemukan.")
            print("Pilih informasi yang ingin diubah:")
            print("1. Judul Buku")
            print("2. Penulis Buku")
            print("3. Stok")
            print("4. Harga Sewa Seminggu")
            print("5. Kembali ke Menu Utama")
            option = input("Masukkan pilihan (1/2/3/4/5): ")

            if option == "1":
                new_title = input("Masukkan judul buku yang baru: ")
                fi[i][1] = new_title
                print("Judul buku telah diperbarui.")
            elif option == "2":
                new_author = input("Masukkan penulis buku yang baru: ")
                fi[i][2] = new_author
                print("Penulis buku telah diperbarui.")
            elif option == "3":
                new_stock = int(input("Masukkan stok buku yang baru: "))
                fi[i][3] = new_stock
                print("Stok buku telah diperbarui.")
            elif option == "4":
                new_price = float(input("Masukkan harga sewa seminggu yang baru: "))
                fi[i][4] = new_price
                print("Harga sewa buku telah diperbarui.")

            elif option == "5":
                with open(json_path_fiksi, "w") as sa:
                    json.dump(fi, sa, indent=4)
                return adminpage()
            else:
                print("Pilihan tidak valid.")

            with open(json_path_fiksi, "w") as sa:
                json.dump(fi, sa, indent=4)

            break
    else:
        for nonfiksi in nonfi:
            if nonfiksi[0] == id_buku:
                print(f"Buku Nonfiksi ID {id_buku} ditemukan.")
                print("Pilih informasi yang ingin diubah:")
                print("1. Judul Buku")
                print("2. Penulis Buku")
                print("3. Stok")
                print("4. Harga Sewa Seminggu")
                option = input("Masukkan pilihan (1/2/3/4): ")

                if option == "1":
                    new_title = input("Masukkan judul buku yang baru: ")
                    nonfiksi[1] = new_title
                    print("Judul buku telah diperbarui.")
                elif option == "2":
                    new_author = input("Masukkan penulis buku yang baru: ")
                    nonfiksi[2] = new_author
                    print("Penulis buku telah diperbarui.")
                elif option == "3":
                    new_stock = int(input("Masukkan stok buku yang baru: "))
                    nonfiksi[3] = new_stock
                    print("Stok buku telah diperbarui.")
                elif option == "4":
                    new_price = float(input("Masukkan harga sewa seminggu yang baru: "))
                    nonfiksi[4] = new_price
                    print("Harga sewa buku telah diperbarui.")
                
                elif option == "5":
                    with open(json_path_nonfiksi, "w") as sa:
                        json.dump(nonfi, sa, indent=4)
                    return adminpage()
                else:
                    print("Pilihan tidak valid.")

                with open(json_path_nonfiksi, "w") as sa:
                    json.dump(nonfi, sa, indent=4)

                break
        else:
            print(f"Buku dengan ID {id_buku} tidak ditemukan.")


# Fungsi sewa buku ni aku bingung co masih anj, soalnya klo ID nya pake angka biasa 1,2,3 ntar ID fiksi sm non fiksi sama dong
# Mau nda mau nnti buat if suruh pilih mau liat/beli buku fiksi ato non fiksi

def sewa_buku():
    while True:
        print("Daftar Buku Perpustakaan Gacor\n")
        daftar_buku()
    
        idsewa = input("Masukkan ID Buku Yang Ingin Disewa : ")
        qtysewa = input("Masukkan Jumlah Buku Yang Ingin Disewa : ")
        hargasewa = input("Mau Sewa Berapa Minggu? : ")

        for fiksi in fi:
            if fiksi[0] == idsewa:
                if qtysewa > fiksi[3]:
                    print("Maaf Stok Buku Tidak Mencukupi :(")
                    break
        
        else:
            for i in range(len(fi)):
                if fi[i][0] == idsewa:
                    fi[i][3] -= qtysewa
                    
                    
        
        for nonfiksi in nonfi:
            if nonfiksi[0] == idsewa:
                if qtysewa > nonfiksi[3]:
                    print("Maaf Stok Buku Tidak Mencukupi :(")
                    break
        
        else:
            for i in range(len(nonfi)):
                if nonfi[i][0] == idsewa:
                    nonfi[i][3] == qtysewa
                    nonfi[i][4] == hargasewa

def hapus_buku():
    # input id item yang ingin dihapus
    id_item = input("Masukkan ID fi yang ingin dihapus: ")
    for i in range(len(fi)):
        if fi[i][0] == id_item:
            # menghapus item sesuai input id
            fi.pop(i)
            
            # menampilkan daftar item yang terbaru
            daftar_buku()
            break
    else:
        print("fi tidak ditemukan")
    
    for i in range(len(nonfi)):
        if nonfi[i][0] == id_item:
            # menghapus item sesuai input id
            fi.pop(i)
            
            # menampilkan daftar item yang terbaru
            daftar_buku()
            break
    else:
        print("fi tidak ditemukan")
        
def adminpage():
        while True:
            print("-"*50)
            print("Menu Admin :\n")
            print("1. Tambah Buku")
            print("2. Lihat Buku")
            print("3. Update Buku")
            print("4. Hapus Buku")
            print("5. Kembali ke Menu Login")

            print("-"*50)
            adminchoice = input("Pilih Opsi Menu : ")
            print("-"*50)

            if adminchoice == '1':
                tambah_buku()
            elif adminchoice == '2':
                lihat_buku()
            elif adminchoice == '3':
                update_buku ()
            elif adminchoice == '4':
                hapus_buku()
            elif adminchoice == '5':
                menu_1()
            else:
                print("Pilihan Tidak Valid, Coba Lagi!")

def transaksi():
    while True:
        clear()  # You need to implement the clear_screen() function.
        # Display a list of available "fi" items.
        print("Daftar Buku Yang Tersedia")
        daftar_buku()  # Define the daftar_buku() function to list available items.
        
        try:
            id_item = input("Masukkan ID fi yang ingin dibeli : ")
            qty = int(input("Masukkan jumlah yang ingin dibeli : "))
            lamasewa = int(input("Masukkan Waktu Sewa: "))
            
            # Check if the selected item is available and if the quantity is in stock.
            for user_dict in pengguna:
                if user_dict['username'] == username:
                    item_found = False
                    for i in range(len(fi)):
                        if fi[i][0] == id_item:
                            item_found = True
                            if qty > fi[i][3]:
                                print("Maaf, stok barang tidak mencukupi!")
                                break
                            else:
                                nama_fi = fi[i][1]
                                harga_sewa = int(fi[i][4])
                                harga_sewa *= lamasewa
                                
                                if harga_sewa > user_dict['emoney']:
                                    print("Maaf, Uang Anda Tidak Cukup")
                                    break
                                else:
                                        if user_dict['username'] == username:
                                            user_dict["emoney"] -= harga_sewa
                                            nonfi[i][3] -= qty

                                    
                                            print("=" * 60)
                                            print("                 Struk Pembelian Buku Fiksi")
                                            print("=" * 60)
                                            print(f"""
                                    fi : {nama_fi}
                                    Jumlah  : {qty}
                                    Total   : Rp {harga_sewa}
                                    Kembalian : Rp {user_dict["emoney"]}
                                    
                                            """)
                                            print("=" * 60)
                                            print("       Terima Kasih Telah Membeli fi di Toko Kami :)")
                                            print("=" * 60)
                                            with open(json_path_fiksi, 'w') as su:
                                                json.dump(fi, su, indent=4)

                                            with open(json_path_DataUser, 'w') as su:
                                                json.dump(pengguna, su, indent=4)
                                
                                        while True:
                                            pilihan = input("Apakah Ingin Membeli Lagi? (y/t): ").lower()
                                            if pilihan == "t":
                                                return
                                            elif pilihan == "y":
                                                break
                                            else:
                                                print("Pilihan tidak tersedia")
            
            if not item_found:
                print("Item tidak ditemukan. Silakan masukkan ID yang valid.")
                
            for user_dict in pengguna:
                if user_dict['username'] == username:
                    item_found = False
                    for i in range(len(nonfi)):
                        if nonfi[i][0] == id_item:
                            item_found = True
                            if qty > nonfi[i][3]:
                                print("Maaf, stok barang tidak mencukupi!")
                                break
                            else:
                                nama_nonfi = nonfi[i][1]
                                harga_sewa = int(fi[i][4])
                                harga_sewa *= lamasewa
                                
                                if harga_sewa > user_dict['emoney']:
                                    print("Maaf, Uang Anda Tidak Cukup")
                                    break
                                else:
                                        if user_dict['username'] == username:
                                            user_dict["emoney"] -= harga_sewa
                                            nonfi[i][3] -= qty
                                    
                                            print("=" * 60)
                                            print("                 Struk Pembelian Buku Fiksi")
                                            print("=" * 60)
                                            print(f"""
                                    fi : {nama_nonfi}
                                    Jumlah  : {qty}
                                    Total   : Rp {harga_sewa}
                                    Kembalian : Rp {user_dict["emoney"]}
                                    
                                            """)
                                            print("=" * 60)
                                            print("       Terima Kasih Telah Membeli fi di Toko Kami :)")
                                            print("=" * 60)

                                            with open(json_path_nonfiksi, 'w') as su:
                                                json.dump(nonfi, su, indent=4)

                                            with open(json_path_DataUser, 'w') as su:
                                                json.dump(pengguna, su, indent=4)
                                
                                        while True:
                                            pilihan = input("Apakah Ingin Membeli Lagi? (y/t): ").lower()
                                            if pilihan == "t":
                                                return
                                            elif pilihan == "y":
                                                break
                                            else:
                                                print("Pilihan tidak tersedia")
            
            
            if not item_found:
                print("Item tidak ditemukan. Silakan masukkan ID yang valid.")
                
        except ValueError:
            print("Invalid input. Pastikan jumlah dan waktu sewa adalah angka.")


def topup_emoney():
    while True:
        try:
            print("Berikut Nominal Top Up Yang Tersedia")
            print("1. 10.000")
            print("2. 25.000")
            print("3. 50.000")
            print("4. 100.000")
            print("5. Kembali")
            topupem = input("Pilih Nominal Top Up : ")
            
            if topupem == "1":
                nominal = 10000
            elif topupem == "2":
                nominal = 25000
            elif topupem == "3":
                nominal = 50000
            elif topupem == "4":
                nominal = 100000
            elif topupem == "5":
                clear()
                userpage()
                return
            else:
                print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.")
                continue

            for user_dict in pengguna:
                if user_dict['username'] == username and "emoney" in user_dict:
                    user_dict["emoney"] += nominal
                    print(f"Selamat Top Up Anda Berhasil. Saldo E-Money sekarang: {user_dict['emoney']}")
                    with open(json_path_DataUser, 'w') as su:
                        json.dump(pengguna, su, indent=4)
                    return
            print("Akun tidak ditemukan atau tidak memiliki saldo E-Money.")
        except ValueError:
            print("Input Anda Tidak Valid")

# You might want to define the 'clear' and 'userpage' functions somewhere in your code.
                
def ceksaldo_emoney():
    for user_dict in pengguna:
        if user_dict['username'] == username:
            ceksaldo = user_dict["emoney"]
            print("SALDO E-Money Anda Tersisa", ceksaldo)
            break
    
def menu_1():
    while True:
        print("-"*50)
        print("\tSelamat Datang di Perpustakaan Gacor\n")
        print("-"*50)
        print("1. Login")
        print("2. Register")
        print("3. Log Out")
        
        
        menu_awal = input("Silahkan Pilih Menu Dibawah ini :")
        
        #login akan langsung menentukan pembeli atau admin
        if menu_awal == "1" :
            login() #jika username dan password yang di input bukan akun admin maka program pembeli akan muncul
        elif menu_awal == "2":
            register()
        elif menu_awal == "3":
            break
        else:
            print("Input Anda Tidak Valid")
            
menu_1()