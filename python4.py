
a=int(input("listenin birinci elemanýný gir: "))
b=int(input("listenin ikinci elemanýný gir: "))
c=int(input("listenin üçüncü elemanýný gir: "))
d=int(input("listenin dördüncü elemanýný gir: "))
e=int(input("listenin beþinci elemanýný gir: "))
f=int(input("listenin altýncý elemanýný gir: "))

List=[a,b,c,d,e,f]
Liste=[]

for i in List:
  if int(i)%2==1 :
    Liste.append(i)
  
print("Listenin en büyük tek sayýlý elemaný: ",max(Liste))

