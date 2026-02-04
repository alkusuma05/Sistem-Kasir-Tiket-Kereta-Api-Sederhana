def main():
    # Harga berdasarkan Tujuan dan Kelas
    PRICELIST = {
        "1": {
            "tujuan": "Jakarta - Bandung",
            "Eksekutif": 250000, "Bisnis": 150000, "Ekonomi": 80000
        },
        "2": {
            "tujuan": "Jakarta - Yogyakarta",
            "Eksekutif": 550000, "Bisnis": 350000, "Ekonomi": 180000
        },
        "3": {
            "tujuan": "Jakarta - Surabaya",
            "Eksekutif": 750000, "Bisnis": 450000, "Ekonomi": 250000
        }
    }

    daftar_penumpang = []

    print("=" * 65)
    print(f"{'SISTEM TIKET KERETA API MULTI-RUTE':^65}")
    print("=" * 65)

    try:
        jumlah = int(input("Masukkan jumlah penumpang: "))
    except ValueError:
        print("❌ Error: Masukkan angka yang valid!")
        return

    for i in range(1, jumlah + 1):
        print(f"\n--- Data Penumpang ke-{i} ---")
        nama = input("Nama Penumpang    : ")

        # Menu Tujuan
        print("\nPilih Tujuan:")
        print(" 1. Jakarta - Bandung")
        print(" 2. Jakarta - Yogyakarta")
        print(" 3. Jakarta - Surabaya")
        pilih_tujuan = input("Masukkan pilihan rute (1/2/3): ")

        # Menu Kelas
        print("\nPilih Kelas Kereta:")
        print(" 1. Eksekutif")
        print(" 2. Bisnis")
        print(" 3. Ekonomi")
        pilih_kelas = input("Masukkan pilihan kelas (1/2/3): ")

        # Mendapatkan data rute (jika salah input, default ke rute 1)
        rute_data = PRICELIST.get(pilih_tujuan, PRICELIST["1"])
        rute_nama = rute_data["tujuan"]

        # Memetakan angka pilihan kelas
        mapping_kelas = {"1": "Eksekutif", "2": "Bisnis", "3": "Ekonomi"}
        nama_kelas = mapping_kelas.get(pilih_kelas, "Ekonomi")

        # harga akhir
        harga_akhir = rute_data[nama_kelas]

        # Simpan ke daftar
        daftar_penumpang.append({
            "nama": nama,
            "tujuan": rute_nama,
            "kelas": nama_kelas,
            "harga": harga_akhir
        })

    # OUTPUT DAFTAR
    print("\n" + "=" * 85)
    print(f"{'LAPORAN DAFTAR PENUMPUANG':^85}")
    print("=" * 85)
    print(f"{'No':<3} | {'Nama':<18} | {'Rute Tujuan':<25} | {'Kelas':<12} | {'Harga':>12}")
    print("-" * 85)

    total_bayar = 0
    for no, p in enumerate(daftar_penumpang, 1):
        total_bayar += p['harga']
        print(f"{no:<3} | {p['nama']:<18} | {p['tujuan']:<25} | {p['kelas']:<12} | Rp{p['harga']:>10,}")

    print("-" * 85)
    print(f"{'TOTAL PENERIMAAN':<67} : Rp{total_bayar:>10,}")
    print("=" * 85)

if __name__ == "__main__":
    main()