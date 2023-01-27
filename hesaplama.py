print("""   
      
      *****KAR-ZARAR-KOMİSYON-KDV-KARGO-MALİYET*****
      
      """)

print("""
      
1. %8 KDV'Li Alış Fiyatı

2. %18 KDV'Li Alış Fiyatı

3. Satış Fiyatı

4. Kar Tutarı

5. Kar Tutarı ("Maliyet Gideri Sabit")

6. Kar Tutarı ("%18 Komisyon 48 TL Kargo Sabit")

7. Satıştan Kar Oranı


Programdan Çıkmak İçin 'q' ya basınız.
      
      """)

kdv1 = 1.08 # kdv oranı
kdv2 = 1.18 # kdv oranı
komisyon1 = 0.20 # komisyon oranı
komisyon2 = 0.18 # komisyon oranı
komisyon3 = 0.16 # komisyon oranı
komisyon4 = 0.15 # komisyon oranı
komisyon5 = 0.12 # komisyon oranı
komisyon6 = 0.10 # komisyon oranı
komisyon7 = 0.04 # komisyon oranı
kargo1 = 6.0 # TL
kargo2 = 8.5 # TL
kargo3 = 12.0 # TL
kargo4 = 15.0 # TL
kargo5 = 48.0 # TL
maliyet = 4.0 # TL


while True:
    
    secim = input("Hangi İşlemi Yapmak İstiyorsunuz? : ")
    
    if (secim == "q"):
        print("Programdan Çıkılıyor...")
        break
    
    if (secim == "1"):
        islem1 = float(input("Alış Fiyatı: "))
        islem2 = kdv1
        print("KDV'li Alış Fiyatı: ")
        print(islem1 * islem2)
        print("TL")
        
    elif (secim == "2"):
        islem1 = float(input("Alış Fiyatı: "))
        islem2 = kdv2
        print("KDV'li Alış Fiyatı: ")
        print(islem1 * islem2)
        print("TL")
          
    if (secim == "3"):
        islem1 = float(input("KDV'li Alış Fiyatı: "))
        print("Net Satış Fiyatı: ")
        print(islem1 * 2)
        print("TL")
        
    if (secim == "4"):
        islem1 = float(input("Net Satış Fiyatı: "))
        islem2 = float(input("Komisyon Tutarı: "))
        islem3 = float(input("KDV'li Alış Fiyatı: "))
        islem4 = float(input("Kargo Tutarı: "))
        islem5 = float(input("Maliyet Gideri: "))
        print("Kar Tutarı: ")
        print(islem1 - (islem1 * islem2)-(islem3) - islem4 - islem5)
        print("TL")
        
    elif (secim == "5"):
        islem1 = float(input("Net Satış Fiyatı: "))
        islem2 = float(input("Komisyon Tutarı: "))
        islem3 = float(input("KDV'li Alış Fiyatı: "))
        islem4 = float(input("Kargo Tutarı: "))
        islem5 = maliyet
        print("Kar Tutarı: ")
        print(islem1 - (islem1 * islem2)-(islem3) - islem4 - islem5)
        print("TL")
            
    elif (secim == "6"):
        islem1 = float(input("Net Satış Fiyatı: "))
        islem2 = komisyon2
        islem3 = float(input("KDV'li Alış Fiyatı: "))
        islem4 = kargo5
        islem5 = maliyet
        print("Kar Tutarı: ")
        print(islem1 - (islem1 * islem2)-(islem3) - islem4 - islem5)
        print("TL")
        
    if (secim == "7"):
        print("Satıştan Kar Oranı: ")
        oran = float((islem1 - (islem1 * islem2)-(islem3) - islem4 - islem5)/ islem3 * 100.0)
        cevap = ""
        print(cevap.format(abs(islem1 - (islem1 * islem2)-(islem3) - islem4 - islem5)/ islem3 * 100.0,abs(oran)))
        if oran == 0:
            cevap = "Kar Yapmadınız."
        if oran < 0:
            cevap = "Satıştan %{} kadar zarar ettiniz."
        if oran > 0:
            cevap = "Satıştan %{} kadar kar ettiniz."
        print(cevap.format(abs(islem1 - (islem1 * islem2)-(islem3) - islem4 - islem5)/ islem3 * 100.0,abs(oran)))