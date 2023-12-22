#Banka ATM 'si olturulsun ilk olarak kart girip girilmedigini konrol etsin
#Kart girilirse ekranda "Para Cekme" "Karta Para Yatırma" "Kart Bilgileri" "Kart iadesi"
#Kart iadesi basılana kadar ana menuye tekrar donsun
#Para Cekme 'de ucret istensin ne kadar miktarda para cekilecegini
#Karta Para Yatırma da Kart Bilgileri istensin

print("--Banka Islemlerine Hosgeldiniz--")
var_yok = input("Kartin Girilip Girilmedigi (e) ise kart girilmistir -- (h ise kart yoktur): ")
i = 0
j = 1

while (i < 3 and j == 1):
    if var_yok == "e":
        sifre = int(input("Lutfen Sifrenizi Giriniz: "))
        ad = "Atakan"
        soyad = "Canbakis"
        sifre1 = 123
        bakiye = 200
        if  sifre == sifre1:
            while j == 1:
                a = int(input("""
                1-Para Cekme
                2-Karta Para Yatirma
                3-Kart Bilgiler
                4-Kart Iade
                """))
                if a == 1:
                    cekilen_miktar = float(input("Para Cekilecegi Miktari Giriniz: "))
                    if cekilen_miktar <=bakiye:
                        bakiye = bakiye - cekilen_miktar
                        continue
                    else:
                        print(f"Yetersiz Bakiye (Bakiyeniz:{bakiye}TL)")
                        continue
                elif a == 2:
                    yatirma_miktari = float(input("Yatıracaginiz Para Miktarini Giriniz: "))
                    bakiye = bakiye + yatirma_miktari
                    continue
                elif a == 3:
                    print("Adi: ",ad,"\n","Soyadi: ",soyad,"\n","Bakiye: ",str(bakiye) + "TL")
                    continue
                elif a == 4:
                     j = input("devam etmek icin  2 'yi tuslayin:")
        else:
            print("Bilgileriniz Hatali")
            i = i + 1
    else:
        break
if i == 3:
     print("Kartiniz Bloke Oldu")
else:
  print("Lutfen Kartinizi Aliniz")

