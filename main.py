class Pesawat:
    def __init__(self, **kwargs):
        self.nama = kwargs.get("nama")
        self.kapasitas = kwargs.get("kapasitas")
        self.kecepatan = kwargs.get("kecepatan")
        self.kemampuan_jelajah = kwargs.get("kemampuan jelajah")
        self.id_penerbangan = None
    
    def __str__(self):
        print(f'Nama Pesawat: {self.nama}')
        print(f'Kapasitas Pesawat: {self.kapasitas} penumpang')
        print(f'Kecepatan Maksimum: {self.kecepatan}')
        print(f'Kemampuan Jelajah: {self.kemampuan_jelajah} liter/km')
        print(f'Penerbangan Pesawat: {self.id_penerbangan}' if self.id_penerbangan != None)

    def tambahkanPenerbangan(self, id_penerbangan):
        self.id_penerbangan = id_penerbangan
        print(f"Penerbangan [{id_penerbangan}] Berhasil Dijadwalkan untuk Pesawat [{self.nama}]")

class Tiket:
    BATAS_BAGASI_GRATIS = 30        # kg
    BIAYA_KELEBIHAN_BAGASI = 50_000 # Rp/kg
    DISKON_SEMUA_DEWASA = 0.03      # 3 %
    DISKON_ADA_ANAK     = 0.02      # 2 %
    MIN_PENUMPANG_DISKON = 3        # lebih dari 3

    def __init__(self, **kwargs):
        self.id_pelanggan = kwargs.get("nik")
        self.dewasa      = kwargs.get("dewasa", 0)
        self.anak        = kwargs.get("anak", 0)
        self.berat_bagasi = kwargs.get("berat_bagasi", 0)

    def totalPenumpang(self):
        return self.dewasa + self.anak

    def biayaBagasi(self):
        kelebihan = max(0, self.berat_bagasi - self.BATAS_BAGASI_GRATIS)
        return kelebihan * self.BIAYA_KELEBIHAN_BAGASI


class Pelanggan:
    def __init__(self, **kwargs):
        pass

class Penerbangan:
    def __init__(self, **kwargs):
        pass


def main():
    exit()

if __name__=="main":
    main()