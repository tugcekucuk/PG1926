class Kullanici:
    def init(self,adi,soyadi, okuladi, calisanozelligi):
        print("Kullan�c� s�n�f� fonksyonu")
        self.adi = adi
        self.soyadi = soyadi
        self.calisanozelligi = calisanozelligi
 
    def giris(self):
        print("Giri� Yap�ld�")
 
    def cikis(self):
        print("��k�� yap�ld�")

    class Personal:
        def init(self,adi,soyadi, okuladi, calisanozelligi, subenumara):
            print("Personal s�n�f� fonksiyonu")
            self.adi = adi
            self.soyadi = soyadi
            self.calisanozelligi = calisanozelligi
            self.subenumara = subenumara

    class Ogrenci:
        def init(self,adi,soyadi, okuladi, calisanozelligi, subenumara):
            print("Ogrenci s�n�f� fonksiyonu")
            self.adi = adi
            self.soyadi = soyadi
            self.calisanozelligi = calisanozelligi
            self.subenumara = subenumara

    class Ogretmen:
        def init(self,adi,soyadi, okuladi, calisanozelligi, subenumara):
            print("Ogretmen s�n�f� fonksiyonu")
            self.adi = adi
            self.soyadi = soyadi
            self.calisanozelligi = calisanozelligi 
            self.subenumara = subenumara

Personal=Kullanici.Personal("Fatma","Ta�","Atat�rkAnadolulisesi")Ogrenci = Kullanici.Ogrenci("Ay�e","Toprak","Atat�rkAnadolulisesi",1234)
Ogretmen = Kullanici.Ogretmen("Mehmet","Y�ld�z","Atat�rkAnadolulisesi",1539527,1234)


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