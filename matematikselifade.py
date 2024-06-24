# Kullanıcıdan denklemi alıp karakterler isimli diziye atama
denklem = input("Kontrol etmek istediğiniz mateatiksel ifadeyi giriniz.")
karakterler = list(denklem)
print(karakterler)
operatorler = ["+", "-", "*", "/"]
parantes_isareti = ["(",")"]
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
    else :
      parantezSayaci += 0

    if parantezSayaci < 0:
      return False

  if parantezSayaci == 0:
    return True
  else :
    return False
  

def karsilastir(dizi):
  """Bir diziyi karşılaştırır ve True/False döndürür.

  Args:
    dizi: Karşılaştırılacak elemanları içeren dizi.
    operator: Karşılaştırma operatörlerini içeren dizi.

  Returns:
    Karşılaştırma sonucu True veya False.
  """
  for i in range(1, len(dizi) - 1):
    if len(dizi) == 1:
      return True
    elif dizi[i] in operatorler:
      if dizi[i+1] not in operatorler:
        return True
      elif dizi[i+1] in parantes_isareti:
        if dizi[i+2] not in operatorler:
          return True
      else:
        return False
    else:
      return True
  
def ardArdaOperatorVarMi(parametreDizi):
  """
  Parametredeki dizide ard arda operatör olup olmadığını kontrol eder.

  Parametreler:
    parametreDizi: Kontrol edilecek öğeleri içeren bir dizi.
    operatorler: Arandık operatörlerin bir listesi.

  Dönüş değeri:
    Ard arda operatör varsa True, yoksa False.
  """

  for i in range(len(parametreDizi) - 1):
    if parametreDizi[i] in operatorler and parametreDizi[i+1] in operatorler:
      return False
  return True

def tanimsizOge(dizi):
  izinVerilenler = operatorler + parantes_isareti
  for eleman in dizi:
    if eleman not in izinVerilenler:
      if eleman.isdigit():
        return True
    else :
      return False

parantez = parantez_kontrol(karakterler)
operator_cakismasi = karsilastir(karakterler)
operator_kontrol = ardArdaOperatorVarMi(karakterler)
ayrik_oge = tanimsizOge(karakterler)

sonuc = [parantez,operator_cakismasi,operator_kontrol,ayrik_oge]
if all(sonuc) == True:
  print("Matematiksel ifade doğrudur.")
else:
  print("Matematiksel ifade yanlıştır.")
