class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __strx__(self):
        return f"Persegi Panjang dengan panjang {self.panjang} dan lebar {self.lebar}"

panjang = int(input("Masukkan panjang : "))
lebar = int(input("Masukkan lebar : "))

persegi_panjang = PersegiPanjang(panjang, lebar)

print(persegi_panjang)

keliling = persegi_panjang.hitung_keliling()
luas = persegi_panjang.hitung_luas()

print(f"Keliling: {keliling} cm")
print(f"Luas: {luas} cm")

