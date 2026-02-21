#types of conditonal statements
#example 1
nilai = 78
if nilai >= 90:
    print("Predikat: Sangat Memuaskan")
elif nilai >= 80:
    print("Predikat: Memuaskan")
elif nilai >= 70:
    print("Predikat: Cukup")
elif nilai >= 60:
    print("Predikat: Kurang")
elif nilai >= 50:
    print("Predikat: Perlu Bimbingan")
else:
    print("Predikat: Remedial")

#Syntax of the if statement
number = 50
if number > 45:
    # Calculate square
    print(number * number)
print('Next lines of code')

#If – else statement
kode_akses = input("Masukkan kode akses: ")

if kode_akses == "CIFSIMUT":
    print("Akses diterima")
else:
    print("Akses ditolak")

#Syntax of the if-elif-else statement
def kategori_peringkat(peringkat):
    if peringkat == 1:
        print("Juara 1 - Medali Emas")
    elif peringkat == 2:
        print("Juara 2 - Medali Perak")
    elif peringkat == 3:
        print("Juara 3 - Medali Perunggu")

    else:
        print("Tidak mendapatkan peringkat")

kategori_peringkat(1)
kategori_peringkat(2)
kategori_peringkat(3)
kategori_peringkat(4)

#Menggunakan Input dari Pengguna
jumlah_barang = int(input("Masukkan jumlah barang: "))

if jumlah_barang > 3:
    print("Barang lebih dari 3")
elif jumlah_barang == 3:
    print("Barang tepat 3")
else:
    print("Barang kurang dari 3")

#Menggunakan if Bersarang (Nested If)
usia = int(input("Masukkan usia: "))

if usia >= 13:
    print("Boleh masuk bioskop")
    if usia >= 18:
        print("Boleh menonton semua film")
    else:
        print("Hanya boleh menonton film remaja")
else:
    print("Tidak boleh masuk bioskop")

#Menggunakan Operator Logika dalam if
usia = int(input("Masukkan usia: "))

if usia >= 18:
    print("Boleh masuk bioskop dan menonton semua film")
elif usia >= 13 and usia < 18:
    print("Boleh masuk bioskop, tapi hanya film remaja")
else:
    print("Tidak boleh masuk bioskop")

#Menggunakan Ternary Operator (if dalam satu baris)
total_belanja = int(input("Masukkan total belanja: "))
status = "Dapat Diskon" if total_belanja >= 50000 else "Tidak Dapat Diskon"
print(f"Status belanja: {status}")

#Variabel yang Bisa Digunakan dalam if, elif
#Boolean (bool)
lampu_menyala = True

if lampu_menyala:
    print("Lampu sedang menyala")

#Angka (int, float) 
stok = 8

if stok >= 5:
    print("Stok tersedia")
elif stok < 5:
    print("Stok hampir habis")

#String (str)
keranjang = ["Buku", "Pulpen"]

if keranjang:
    print("Keranjang tidak kosong")

#List, Tuple, Set, Dictionary (list, tuple, set, dict)
tugas = []

if tugas:
    print("Masih ada tugas yang harus dikerjakan")
else:
    print("Tidak ada tugas hari ini")

#NoneType (None)
jadwal_rapat = None

if jadwal_rapat is None:
    print("Jadwal rapat belum ditentukan")