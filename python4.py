
a=int(input("listenin birinci eleman�n� gir: "))
b=int(input("listenin ikinci eleman�n� gir: "))
c=int(input("listenin ���nc� eleman�n� gir: "))
d=int(input("listenin d�rd�nc� eleman�n� gir: "))
e=int(input("listenin be�inci eleman�n� gir: "))
f=int(input("listenin alt�nc� eleman�n� gir: "))

List=[a,b,c,d,e,f]
Liste=[]

for i in List:
  if int(i)%2==1 :
    Liste.append(i)
  
print("Listenin en b�y�k tek say�l� eleman�: ",max(Liste))

