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
        print(f'Penerbangan Pesawat: {self.id_penerbangan}' if self.id_penerbangan != None else None)

    def tambahkanPenerbangan(self, id_penerbangan):
        self.id_penerbangan = id_penerbangan
        print(f"Penerbangan [{id_penerbangan}] Berhasil Dijadwalkan untuk Pesawat [{self.nama}]")