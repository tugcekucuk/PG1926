myList = []
arr = [int(item) for item in input("Sayilari giriniz ").split()]
for i in arr:
  if i==0:
    myList.insert(0,i)
  else:
    myList.append(i)
print(myList)