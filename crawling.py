#INTRODUCTION
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

response = requests.get("https://www.youtube.com/")
print(response.status_code)
print(response.text)

#perhitungan matematika
import math

print(math.sqrt(50))
print(math.pi)

#library random

import random

nomor_antrian = random.randint(1, 10)
print("antrian :", nomor_antrian)

import requests

#penggunaan library random dan if
import random

undian = random.randint(50, 100)
print("Nomor :", undian)

if undian >= 85:
    print("selamat anda beruntung")
else:
    print("anda belum beruntung")


nilai = random.randint(0, 100)
print("Nilai Mahasiswa:", nilai)

if nilai >= 85:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
elif nilai >= 65:
    print("Grade C")
else:
    print("Grade D")

#LIBRARY TIME
from datetime import datetime

waktu = datetime.now()
print("Tanggal dan Waktu sekarang:", waktu)