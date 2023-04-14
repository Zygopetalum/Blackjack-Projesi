############## Blackjack Projesi ##################
from Blackjack_art import logo
import random
################### İpuçları ###################

# İpucu 4: Rastgele bir kart *döndürmek* için aşağıdaki Listeyi kullanan bir deal_card() işlevi oluşturun.
def rastgele_kart():
    kartlar = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    kart = random.choice(kartlar)
    return kart

# İpucu 6: Bir Kart Listesini girdi olarak alan hesapla_skor() adlı bir işlev oluşturun
def hesapla_skor(kartlar):
    # İpucu 7: hesapla_skor() içinde blackjack olup olmadığını kontrol edin (yalnızca 2 kartlı bir el: as + 10) ve gerçek puan yerine 0 döndürün.
    # 0, oyunumuzda bir blackjack'i temsil edecektir.
    if sum(kartlar) == 21 and len(kartlar) == 2:
        return 0

    # Bunu yapmana yardımcı olması için sum() işlevine bak.
    # İpucu 8: Compare_score() içinde 11 (as) olup olmadığını kontrol edin.
    # Skor zaten 21'in üzerindeyse, 11'i kaldırın ve 1 ile değiştirin. Append() ve remove()'a bakmanız gerekebilir.
    if 11 in kartlar and sum(kartlar) > 21:
        kartlar.remove(11)
        kartlar.append(1)
    return sum(kartlar)


# İpucu 13: Karşılaştırmak() adlı bir işlev oluşturun ve kullanıcı_toplam_skoru ve bilgisayar_toplam_skoru değerlerini girin.
# Hem bilgisayar hem de kullanıcı aynı puana sahipse, bu bir beraberliktir.
## Bilgisayarda blackjack (0) varsa, kullanıcı kaybeder.Kullanıcının blackjack'i (0) varsa, kullanıcı kazanır.user_score 21'in üzerindeyse kullanıcı kaybeder.
## Computer_score 21'in üzerindeyse, bilgisayar kaybeder.
## Yukarıdakilerden hiçbiri olmazsa, en yüksek puana sahip oyuncu kazanır.
def Karşılaştırmak(kullanıcı_toplam_skoru, bilgisayar_toplam_skoru):
    # Bug düzeltme. Hem siz hem de bilgisayar bittiyse, kaybedersiniz.
    if bilgisayar_toplam_skoru > 21 and kullanıcı_toplam_skoru > 21:
        return "Sen kaybettin 😤\nBilgisayar kazandı😃"

    if kullanıcı_toplam_skoru == bilgisayar_toplam_skoru:
        return "Beraberlik 🙃 "

    elif bilgisayar_toplam_skoru == 0:
        return "Sen kaybettin😵‍\nBilgisayar kazandı😎 "
    elif bilgisayar_toplam_skoru > 21:
        return "Sen Kazandın😁\nBilgisayar Kaybetti😭 "

    elif kullanıcı_toplam_skoru == 0:
        return "Sen Kazandın😎\nBilgisayar Kaybetti😵  "
    elif kullanıcı_toplam_skoru > 21:
        return "Sen kaybettin😭\nBilgisayar kazandı😁  "

    elif kullanıcı_toplam_skoru > bilgisayar_toplam_skoru:
        return "Sen kazandı 😃\nBilgisayar kaybetti😤  "
    else:
        return "Sen kaybettin😤\nBilgisayar kazandı 😃 "


# İpucu 5: rastgele_kart() ve append() kullanarak kullanıcıya ve bilgisayara 2'şer kart dağıtın.
def oyun_baslangıcı():
    print(logo)
    kullanıcı_kartları = []
    bilgisayar_kartları = []
    oyun_bittisi = False

    for _ in range(2):
        kullanıcı_kartları.append(rastgele_kart())
        bilgisayar_kartları.append(rastgele_kart())
    # İpucu 11: Skorun çekilen her yeni kartla yeniden kontrol edilmesi gerekecek ve İpucu 9'daki kontrollerin oyun bitene kadar tekrarlanması gerekecek.

    while not oyun_bittisi:
        # İpucu 9: hesapla_skor() öğesini çağırın.  Bilgisayar veya kullanıcının blackjack'i (0) varsa veya kullanıcının puanı 21'in üzerindeyse oyun sona erer.
        kullanıcı_toplam_skoru = hesapla_skor(kullanıcı_kartları)
        bilgisayar_toplam_skoru = hesapla_skor(bilgisayar_kartları)
        print(f"   Kullanıcının kartları: {kullanıcı_kartları}, Kullanıcının skoru: {kullanıcı_toplam_skoru}")
        print(f"   Bilgisayarın ilk kartı: {bilgisayar_kartları[0]}")

        if kullanıcı_toplam_skoru == 0 or bilgisayar_toplam_skoru == 0 or kullanıcı_toplam_skoru > 21:
            oyun_bittisi = True
        else:
            # İpucu 10: Oyun bitmediyse kullanıcıya başka bir kart çekmek isteyip istemediğini sorun.  Evet ise, user_cards Listesine başka bir kart eklemek için deal_card() işlevini kullanın.
            ##Hayır ise, oyun sona ermiştir.
            ek_kart = input(
                "Ek kart istiyor musunuz ?'E','H':").lower()
            if ek_kart == "e":
                kullanıcı_kartları.append(rastgele_kart())
            else:
                oyun_bittisi = True

    # İpucu 12: Kullanıcının işi bittiğinde, bilgisayarın oynamasına izin verme zamanı.  Bilgisayar, 17'den düşük bir puana sahip olduğu sürece kart çekmeye devam etmelidir.
    while bilgisayar_toplam_skoru != 0 and bilgisayar_toplam_skoru < 17:
        bilgisayar_kartları.append(rastgele_kart())
        bilgisayar_toplam_skoru = hesapla_skor(bilgisayar_kartları)

    print(f"   Kullanıcının Toplam kartları: {kullanıcı_kartları}, Kullanıcının Toplam skoru: {kullanıcı_toplam_skoru}")
    print(f"   Bilgisayarın Toplam kartları: {bilgisayar_kartları},Bilgisayarın Toplam skoru:{bilgisayar_toplam_skoru}")
    print(Karşılaştırmak(kullanıcı_toplam_skoru, bilgisayar_toplam_skoru))


# İpucu 14: Kullanıcıya oyunu yeniden başlatmak isteyip istemediğini sorun. Evet cevabı verirlerse, konsolu boşaltın ve yeni bir blackjack oyunu başlatın ve art.py'den logoyu gösterin.
the_end=False
while not the_end:
    oyun_baslasınmı=input("Bir Blackjack oyunu oynamak ister misiniz? 'E' veya 'H' yazın?🤔: ").lower()
    if oyun_baslasınmı =="e":
        oyun_baslangıcı()
    elif oyun_baslasınmı== "h":
        print("Oyun Sonlandı....")
        the_end=True
