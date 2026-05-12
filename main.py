from Pelanggan import Pelanggan
from Penerbangan import Penerbangan
from Pesawat import Pesawat
from Tiket import Tiket


def main():
        # --- Data pesawat ---
    b737 = Pesawat(
        nama="Boeing 737-800",
        kapasitas=162,
        kecepatan=842,
        kemampuan_jelajah=5765,
    )
    a320 = Pesawat(
        nama="Airbus A320",
        kapasitas=180,
        kecepatan=833,
        kemampuan_jelajah=6150,
    )
 
    print("=== Data Pesawat ===")
    print(b737)
    print()
    print(a320)
    print()
 
    # --- Data penerbangan ---
    pnb1 = Penerbangan(
        id_penerbangan="GA-101",
        asal="Jakarta (CGK)",
        tujuan="Surabaya (SUB)",
        pesawat=b737,
        tanggal="2025-08-01",
        waktu="08:00",
        tarif_dewasa=750_000,
        tarif_anak=500_000,
    )
    pnb2 = Penerbangan(
        id_penerbangan="QZ-202",
        asal="Jakarta (CGK)",
        tujuan="Bali (DPS)",
        pesawat=a320,
        tanggal="2025-08-05",
        waktu="14:30",
        tarif_dewasa=900_000,
        tarif_anak=600_000,
    )
 
    print("\n=== Data Penerbangan ===")
    print(pnb1)
    print()
    print(pnb2)
    print()
 
    # --- Pemesanan tiket ---
    pelanggan1 = Pelanggan(
        nik="3471234567890001",
        nama="Budi Santoso",
        email="budi@email.com",
        no_hp="081234567890",
    )
 
    # Contoh 1: 4 dewasa, bagasi 35 kg  → diskon 3%, kena biaya bagasi
    tiket1 = Tiket(
        pelanggan=pelanggan1,
        penerbangan=pnb1,
        dewasa=4,
        anak=0,
        berat_bagasi=35,
    )
 
    pelanggan2 = Pelanggan(
        nik="3471234567890002",
        nama="Sari Dewi",
        email="sari@email.com",
        no_hp="089876543210",
    )
 
    # Contoh 2: 2 dewasa + 2 anak, bagasi 20 kg → diskon 2%, bagasi gratis
    tiket2 = Tiket(
        pelanggan=pelanggan2,
        penerbangan=pnb2,
        dewasa=2,
        anak=2,
        berat_bagasi=20,
    )
 
    print("\n=== Struk Tiket 1 ===")
    print(tiket1)
 
    print("\n=== Struk Tiket 2 ===")
    print(tiket2)

if __name__=="main":
    main()