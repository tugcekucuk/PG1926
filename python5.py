class Kullanici:
    def init(self,adi,soyadi, okuladi, calisanozelligi):
        print("Kullanýcý sýnýfý fonksyonu")
        self.adi = adi
        self.soyadi = soyadi
        self.calisanozelligi = calisanozelligi
 
    def giris(self):
        print("Giriþ Yapýldý")
 
    def cikis(self):
        print("Çýkýþ yapýldý")

    class Personal:
        def init(self,adi,soyadi, okuladi, calisanozelligi, subenumara):
            print("Personal sýnýfý fonksiyonu")
            self.adi = adi
            self.soyadi = soyadi
            self.calisanozelligi = calisanozelligi
            self.subenumara = subenumara

    class Ogrenci:
        def init(self,adi,soyadi, okuladi, calisanozelligi, subenumara):
            print("Ogrenci sýnýfý fonksiyonu")
            self.adi = adi
            self.soyadi = soyadi
            self.calisanozelligi = calisanozelligi
            self.subenumara = subenumara

    class Ogretmen:
        def init(self,adi,soyadi, okuladi, calisanozelligi, subenumara):
            print("Ogretmen sýnýfý fonksiyonu")
            self.adi = adi
            self.soyadi = soyadi
            self.calisanozelligi = calisanozelligi 
            self.subenumara = subenumara

Personal=Kullanici.Personal("Fatma","Taþ","AtatürkAnadolulisesi")Ogrenci = Kullanici.Ogrenci("Ayþe","Toprak","AtatürkAnadolulisesi",1234)
Ogretmen = Kullanici.Ogretmen("Mehmet","Yýldýz","AtatürkAnadolulisesi",1539527,1234)


print("Personal")
print(Personal.adi)
print(Personal.soyadi)
print(Personal.calisanozelligi)

print("Ogrenci")
print(Ogrenci.adi)
print(Ogrenci.soyadi)
print(Ogrenci.calisanozelligi)
print(Ogrenci.subenumara)

print("Ogretmen")
print(Ogrenci.adi)
print(Ogrenci.soyadi)
print(Ogrenci.calisanozelligi)
print(Ogrenci.subenumara)