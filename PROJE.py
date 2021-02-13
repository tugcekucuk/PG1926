#aklından bir sayı tut oyunu
#aklımdan tuttuğum sayıyı bilgisayar tahmin ediyor.
import random

enKucukDeger=1
enBuyukDeger=100
tahminSayisi=1
cevap="h"
while cevap!="e":
  print("ek-{} , eb-{}".format(enKucukDeger,enBuyukDeger))
  bilgisayarinTahminEttigiSayi=random.randint(enKucukDeger,enBuyukDeger)
  cevap=input("{} senin tuttuğun sayı mı? [e]vet / daha [b]üyük olmalı / [k]üçük olmalı: ".format(bilgisayarinTahminEttigiSayi))
  if cevap=="e":
    print("Oley!! {} tahminde bildim".format(tahminSayisi))
  elif cevap=="b":
    enKucukDeger=bilgisayarinTahminEttigiSayi+1
  else:
    enBuyukDeger=bilgisayarinTahminEttigiSayi-1
  tahminSayisi+=1