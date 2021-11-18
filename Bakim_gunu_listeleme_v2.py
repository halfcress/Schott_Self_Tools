import datetime as dt
aylar = {
    1:"Ocak", 2:"Şubat", 3:"Mart", 4:"Nisan", 5:"Mayıs", 6:"Haziran", 7:"Temmuz", 8:"Ağustos", 9:"Eylül", 10:"Ekim", 11:"Kasım", 12:"Aralık"
    }
ozel_gunler = {
    "2022-01-01":"Yılbaşı","2022-04-23":"23 Nisan Ulusal Egemenlik ve Çocuk Bayramı","2022-05-01":"1 Mayıs İşçi Bayramı","2022-05-02":"Ramazan Bayramı","2022-05-03":"Ramazan Bayramı","2022-05-19":"19 Mayıs Atatürk'ü Anma Gençlik ve Spor Bayramı","2022-06-09":"Kurban Bayramı","2022-06-10)":"Kurban Bayramı","2022-06-11)":"Kurban Bayramı","2022-06-12)":"Kurban Bayramı","2022-06-15":"15 Temmuz","2022-07-30":"30 Ağustos Zafer Bayramı","2022-10-29":"29 Ekim Cumhuriyet Bayramı"
    }
print("Her Haftanın Bakım Gününü Listeleme")
print("===================================")
print("""
Listesini istediğiniz hattın "en son" rutin bakımı yapıldığı günün;
Önce yıl, sonra ay, sonra günü şeklinde SAYISAL olarak giriniz.
""")
print("===================================")
liste = list()
girdi1 = int(input("Yil giriniz:"))
girdi2 = int(input("Ay giriniz:"))
girdi3 = int(input("Gün giriniz: "))
mevcut = dt.date(girdi1,girdi2,girdi3)
bugun = dt.date.today()
print("Bugün = {}".format(bugun))
print("===================================")

for i in range(0,59):
    sali = mevcut + dt.timedelta(7)
    mevcut = sali
    ay = sali.month
    x = str(mevcut)
    
    if x in ozel_gunler:
        print("{} {} {}|| {}.hafta || {} günü ile çakışıyor. Ertelenebilir.".format(sali.day,aylar[ay],sali.year,sali.strftime("%W"),ozel_gunler[x]))
    if x not in ozel_gunler:
        print("{} {} {}|| {}.hafta ||".format(sali.day,aylar[ay],sali.year,sali.strftime("%W"),))
        

