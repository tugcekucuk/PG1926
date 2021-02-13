List=[]
while True:
  sayi= int(input("sayı gir:"))
  if sayi==0:
    List.insert(0,sayi)
  else:
    List.append(sayi)
  print(List)
  if len(List)==7:
    break