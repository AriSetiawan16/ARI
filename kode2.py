# contoh class
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def sapa(self):
        print(f"Halo, nama saya {self.nama}")
    
    def ulang_tahun(self):
        self.umur += 1
        print(f"Sekarang usia saya {self.umur} tahun")

# contoh inheritance
class Mahasiswa(Manusia):
    def __init__(self, nama, umur, jurusan):
        super().__init__(nama, umur)
        self.jurusan = jurusan
    
    def sapa(self):
        print(f"Halo, nama saya {self.nama} dari jurusan {self.jurusan}")

# contoh penggunaan objek
andi = Mahasiswa("Andi", 20, "Informatika")
andi.sapa()
andi.ulang_tahun()
