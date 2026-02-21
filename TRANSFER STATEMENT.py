def proses_transaksi(batas_pembeli):
    stok_awal = 25
    stok_sisa = stok_awal
    total_terjual = 0

    for pembeli in range(1, batas_pembeli + 1):
        print("Pembeli ke-", pembeli)

        # Placeholder: tidak melakukan apa-apa untuk pembeli ke-4
        if pembeli == 4:
            pass  

        # Lewati pembeli kelipatan 3
        if pembeli % 3 == 0:
            print("Dilewati (kelipatan 3)")
            continue  

        # Hentikan proses jika stok sudah kritis
        if stok_sisa <= 5:
            print("Stok kritis, transaksi dihentikan.")
            break  

        # Jumlah pembelian berbeda berdasarkan nomor pembeli
        if pembeli % 2 == 0:
            jumlah_beli = 2
        else:
            jumlah_beli = 3

        # Kurangi stok
        stok_sisa -= jumlah_beli
        total_terjual += jumlah_beli

        print("Jumlah dibeli:", jumlah_beli)
        print("Sisa stok:", stok_sisa)
        print("-" * 25)

    return total_terjual


# Memanggil fungsi
hasil = proses_transaksi(12)
print("Total barang terjual:", hasil)