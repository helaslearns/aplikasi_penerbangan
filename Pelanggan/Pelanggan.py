class Pelanggan:
    def __init__(self, **kwargs):
        self.nik = kwargs.get("nik")
        self.nama = kwargs.get("nama")
        self.email = kwargs.get("email")
        self.no_hp = kwargs.get("no_hp")

    def __str__(self):
        return (
            f"NIK   : {self.nik}\n"
            f"Nama  : {self.nama}\n"
            f"Email : {self.email}\n"
            f"No HP : {self.no_hp}"
        )      