class Pesawat:
    def __init__(self, **kwargs):
        self.nama = kwargs.get("nama")
        self.kapasitas = kwargs.get("kapasitas")
        self.kecepatan = kwargs.get("kecepatan")
        self.kemampuan_jelajah = kwargs.get("kemampuan_jelajah") 
        self.id_penerbangan = None
    
    def __str__(self):
        result  = f'Nama Pesawat: {self.nama}\n'
        result += f'Kapasitas Pesawat: {self.kapasitas} penumpang\n'
        result += f'Kecepatan Maksimum: {self.kecepatan}\n'
        result += f'Kemampuan Jelajah: {self.kemampuan_jelajah} liter/km'
        if self.id_penerbangan is not None: 
            result += f'\nPenerbangan Pesawat: {self.id_penerbangan}'
        return result

    def tambahkanPenerbangan(self, id_penerbangan):
        self.id_penerbangan = id_penerbangan
        print(f"Penerbangan [{id_penerbangan}] Berhasil Dijadwalkan untuk Pesawat [{self.nama}]")