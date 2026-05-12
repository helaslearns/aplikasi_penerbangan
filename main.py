from Pesawat.Pesawat import Pesawat
from Penerbangan.Penerbangan import Penerbangan
from Pelanggan.Pelanggan import Pelanggan
from Tiket.Tiket import Tiket

def main():
    print("\n" + "=" * 50)
    print("          TEST KELAS PESAWAT")
    print("=" * 50)

    b737 = Pesawat(
        nama="Boeing 737-800",
        kapasitas=162,
        kecepatan=842,
        kemampuan_jelajah=5765
    )
    a320 = Pesawat(
        nama="Airbus A320",
        kapasitas=180,
        kecepatan=833,
        kemampuan_jelajah=6150
    )
    print(b737)
    print()
    print(a320)

    print("\n" + "=" * 50)
    print("          TEST KELAS PENERBANGAN")
    print("=" * 50)

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
    print(pnb1)
    print()
    print(pnb2)

    print("\n" + "=" * 50)
    print("          TEST KELAS PELANGGAN")
    print("=" * 50)

    p1 = Pelanggan(nik="3471000000000001", nama="Budi Santoso",  email="budi@email.com",  no_hp="081234567890")
    p2 = Pelanggan(nik="3471000000000002", nama="Sari Dewi",     email="sari@email.com",  no_hp="089876543210")
    p3 = Pelanggan(nik="3471000000000003", nama="Andi Wijaya",   email="andi@email.com",  no_hp="082211223344")
    print(p1)
    print()
    print(p2)
    print()
    print(p3)

    print("\n" + "=" * 50)
    print("          TEST KELAS TIKET")
    print("=" * 50)

    print("\n[Kasus 1] 4 dewasa, bagasi 35 kg — diskon 3%, kena biaya bagasi")
    tiket1 = Tiket(pelanggan=p1, penerbangan=pnb1, dewasa=4, anak=0, berat_bagasi=35)
    tiket1.kalkulasiTotal()
    print(tiket1.struk())

    print("\n[Kasus 2] 2 dewasa + 2 anak, bagasi 20 kg — diskon 2%, bagasi gratis")
    tiket2 = Tiket(pelanggan=p2, penerbangan=pnb2, dewasa=2, anak=2, berat_bagasi=20)
    tiket2.kalkulasiTotal()
    print(tiket2.struk())

    print("\n[Kasus 3] 1 dewasa, bagasi 10 kg — tanpa diskon, bagasi gratis")
    tiket3 = Tiket(pelanggan=p3, penerbangan=pnb1, dewasa=1, anak=0, berat_bagasi=10)
    tiket3.kalkulasiTotal()
    print(tiket3.struk())

    print("\n[Kasus 4] 3 dewasa, bagasi 30 kg — tepat di batas, tanpa diskon, bagasi gratis")
    tiket4 = Tiket(pelanggan=p1, penerbangan=pnb2, dewasa=3, anak=0, berat_bagasi=30)
    tiket4.kalkulasiTotal()
    print(tiket4.struk())

if __name__ == "__main__":
    main()