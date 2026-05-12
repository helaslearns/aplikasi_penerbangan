class Tiket:
    BATAS_BAGASI_GRATIS = 30        # kg
    BIAYA_KELEBIHAN_BAGASI = 50_000 # Rp/kg
    DISKON_SEMUA_DEWASA = 0.03      # 3 %
    DISKON_ADA_ANAK     = 0.02      # 2 %
    MIN_PENUMPANG_DISKON = 3        # lebih dari 3

    sebelum_diskon = 0
    diskon = 0
    potongan_diskon = 0

    def __init__(self, **kwargs):
        self.id_pelanggan = kwargs.get("nik")
        self.penerbangan = kwargs.get("penerbangan")
        self.dewasa      = kwargs.get("dewasa", 0)
        self.anak        = kwargs.get("anak", 0)
        self.berat_bagasi = kwargs.get("berat_bagasi", 0)

    def totalPenumpang(self):
        return self.dewasa + self.anak

    def biayaBagasi(self):
        kelebihan = max(0, self.berat_bagasi - self.BATAS_BAGASI_GRATIS)
        return kelebihan * self.BIAYA_KELEBIHAN_BAGASI
    
    def kalkulasiTotal(self):
        self.sebelum_diskon = self.dewasa * self.penerbangan.tarif_dewasa + self.anak * self.penerbangan.tarif_anak if self.penerbangan is not None else 0

        if self.totalPenumpang <= self.MIN_PENUMPANG_DISKON:
            self.diskon = 0
        if self.anak == 0:
            self.diskon = self.DISKON_SEMUA_DEWASA
        else:
            self.diskon = self.DISKON_ADA_ANAK

        self.potongan_diskon = self.sebelum_diskon * self.diskon
        
        self.setelah_diskon = self.sebelum_diskon * self.potongan_diskon

        return self.setelah_diskon + self.biayaBagasi()
    
    def struk(self):
        sep = "=" * 50
        nama_pelanggan = self.pelanggan.nama if self.pelanggan else "-"
        id_flight = self.penerbangan.id_penerbangan if self.penerbangan else "-"
        rute = (f"{self.penerbangan.asal} → {self.penerbangan.tujuan}"
                if self.penerbangan else "-")
        jadwal = (f"{self.penerbangan.tanggal}  {self.penerbangan.waktu}"
                  if self.penerbangan else "-")
 
        lines = [
            sep,
            "           TIKET PENERBANGAN",
            sep,
            f"Pemesan          : {nama_pelanggan}",
            f"ID Penerbangan   : {id_flight}",
            f"Rute             : {rute}",
            f"Jadwal           : {jadwal}",
            "-" * 50,
            f"Penumpang Dewasa : {self.dewasa} orang  x  Rp {self.penerbangan.tarif_dewasa if self.penerbangan else 0:,.0f}",
            f"Penumpang Anak   : {self.anak} orang  x  Rp {self.penerbangan.tarif_anak if self.penerbangan else 0:,.0f}",
            f"Subtotal Tarif   : Rp {self.tarif_penumpang_sebelum_diskon:,.0f}",
        ]
 
        if self.diskon > 0:
            jenis = "semua dewasa" if self.anak == 0 else "ada anak"
            lines.append(f"Diskon ({int(self.diskon*100)}% – {jenis})  : -Rp {self.potongan_diskon:,.0f}")
 
        lines += [
            f"Tarif setelah diskon : Rp {self.tarif_penumpang_setelah_diskon:,.0f}",
            "-" * 50,
            f"Berat Bagasi     : {self.berat_bagasi} kg",
        ]
 
        if self.biaya_bagasi > 0:
            kelebihan = self.berat_bagasi - self.BATAS_BAGASI_GRATIS
            lines.append(f"Biaya Bagasi     : {kelebihan} kg x Rp {self.BIAYA_KELEBIHAN_BAGASI:,} = Rp {self.biaya_bagasi:,.0f}")
        else:
            lines.append("Biaya Bagasi     : Gratis (≤ 30 kg)")
 
        lines += [
            "=" * 50,
            f"TOTAL HARGA      : Rp {self.total_harga:,.0f}",
            "=" * 50,
        ]
        return "\n".join(lines)
 
    def __str__(self):
        return self.struk()