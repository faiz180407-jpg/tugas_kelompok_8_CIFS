# Iterative Statement

# perulangan menggunakan for loop (jumlah sudah pasti 30 kali)
for perulangan in range(30):
    print("perulangan ke-", perulangan)

for i in range(30):
    print("Perulangan ke-", i)

# perulangan menggunakan while loop
i = 0
while i < 8:
    print("Perulangan ke-", i)
    i += 1

# Kontrol dalam Perulangan
# 1. break
for perulangan in range(60):
    if perulangan == 33:
        break
    print(perulangan)

# 2. continue
for perulangan in range(25):
    if perulangan == 14:
        continue
    print(perulangan)

# 3. Else pada loop
for angka in range(15):
    print(angka)
else:
    print("Loop selesai, tidak ada break")

# 4. Nested pada loop (perulangan bersarang)
for perulangan_pertama in range(14):
    for perulangan_kedua in range(10):
        for perulangan_ketiga in range (6):
            print(perulangan_pertama, perulangan_kedua, perulangan_ketiga)

# Membuat pola bintang
for baris in range(10):
    for kolom in range(baris+1):
        print("*", end="")
    print()

# Aplikasi literasi dalam algoritma
# 1. Menghitung jumlah total
data = [20, 45, 15, 30, 50]
jumlah = 0
for nilai in data:
    jumlah += nilai

print("Total:", jumlah)

# 2. Menghitung faktorial
n = 7
faktorial = 1

for i in range(1, n+1):
    faktorial *= i

print("Faktorial:", faktorial)

# 3. Validasi Input dengan while
angka = -5
while angka < 0:
    angka = int(input("Masukkan bilangan positif: "))

print("Input sudah diterima")