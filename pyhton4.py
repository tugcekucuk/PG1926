myList = []
arr = [int(item) for item in input("Sayilari giriniz ").split(sep=",")]
for i in arr:
    if int(i)%2==1 :
        myList.append(i)

print("Listenin en büyük tek sayılı elemanı: ",max(myList))