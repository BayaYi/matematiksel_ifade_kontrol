# Kullanıcıdan denklemi alıp karakterler isimli diziye atama
denklem = input("Kontrol etmek istediğiniz mateatiksel ifadeyi giriniz.")
karakterler = list(denklem)
print(karakterler)
operatorler = ["+", "-", "*", "/"]
parantezSayaci = 0

def parantez_kontrol(karakterler):
  """Bir karakter dizisindeki parantezleri kontrol eder ve bozuk olup olmadigini belirler.

  Args:
    karakterler: Kontrol edilecek karakter dizisi.

  Returns:
    Dizi dengeliyse True, değilse False.
  """
  parantezSayaci = 0

  for karakter in karakterler:
    if karakter == "(":
      parantezSayaci += 1
    elif karakter == ")":
      parantezSayaci -= 1

    if parantezSayaci < 0:
      print("Bozuk")
      return False

  if parantezSayaci == 0:
    return True
  else:
    print("Bozuk")
    return False


sonuc = parantez_kontrol(karakterler)

if sonuc:
  print("Dizi dengeli.")
else:
  print("Dizi dengesiz.")