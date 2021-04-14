x = input("INT = : ")

z = []

y = 1
while y <= x:
  if x % y == 0 :
    z.append(y)
    if len(z) > 2:
      break
  y += 1
  
if len(z) > 2:
  print(f"{x} Bir Asal Sayı Değildir.")
  for zitem in z:
    print(f"{x} / {zitem} = {x/zitem}")
else:
  print(f"{x} Bir Asal Sayıdır.")
  
