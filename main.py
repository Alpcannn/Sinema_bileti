#haftanın günlerine ve öğrenci sayısına göre değişkenlik gösteren sinema biletini en ucuza nasıl alırız hesaplaması.
servis_bedeli = 200
gun = str(input("lütfen hafta içi mi hafta sonu mu katılmaz istersiniz belirtin. "))
ogrenci_sayısı = int(input("lütfen kaç öğreci ile katılım sağlayacaksınız yazınız. "))
if ((ogrenci_sayısı < 10) and (gun == "haftaiçi")):
    print("bilet parası kişi başı 10 TL dir.")
elif ((ogrenci_sayısı < 10) and (gun == "haftasonu")):
    print("bilet parası kişi başı 15 dir.")
    bilet_ücreti = 15
elif ((ogrenci_sayısı > 10) and (gun == "haftaiçi")):
    print("bilet parası kişi başı 8 TL dir.")
    bilet_ücreti = 8
elif ((ogrenci_sayısı > 10) and (gun == "haftasonu")):
    print("bilet parası kişi başı 12.5 TL dir.")
    bilet_ücreti = 12.5
else:
  print("bilgileri doğru giriniz")



