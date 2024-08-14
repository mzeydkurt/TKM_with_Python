import random

secimler = ["taş", "kağıt", "makas"]

def tas_kagit_makas_Muhammed_Zeyd_KURT():
    print("Taş Kağıt Makas Oyununa Hoşgeldiniz!")
    print("Kurallar: Taş makası kırar, Makas kağıdı keser, Kağıt taşı sarar.")
    print("İki turu kazanan oyunu kazanır.")

    def bilgisayar_secimi():
        return random.choice(secimler)

    def kullanici_secim():
        while True:
            secim = input("Taş, Kağıt veya Makas seçin: ").lower()
            if secim in secimler:
                return secim
            else:
                print("Geçersiz seçim! Lütfen Taş, Kağıt veya Makas seçin.")

    def puan_hesaplama(secim, bilgisayar_secim):
        if secim == bilgisayar_secim:
            print("Beraberlik")
            return 0, 0
        elif (secim == "taş" and bilgisayar_secim == "makas") or \
             (secim == "kağıt" and bilgisayar_secim == "taş") or \
             (secim == "makas" and bilgisayar_secim == "kağıt"):
            print("Kullanıcı Turu Kazandı!")
            return 1, 0
        else:
            print("Bilgisayar Turu Kazandı!")
            return 0, 1

    def oyun_galibini_belirle(puan_kullanici, puan_bilgisayar):
        if puan_kullanici == 2:
            return "Kullanıcı"
        elif puan_bilgisayar == 2:
            return "Bilgisayar"
        else:
            return None

    while True:
        kullanıcı_puan = 0
        bilgisayar_puan = 0

        while kullanıcı_puan < 2 and bilgisayar_puan < 2:
            print("\nYeni Tur Başladı")
            secim = kullanici_secim()
            secim_bilgisayar = bilgisayar_secimi()
            print(f"Seçiminiz: {secim}")
            print(f"Bilgisayarın Seçimi: {secim_bilgisayar}")

            puan_k, puan_b = puan_hesaplama(secim, secim_bilgisayar)
            kullanıcı_puan += puan_k
            bilgisayar_puan += puan_b

            print(f"Oyun Skoru - Kullanıcı: {kullanıcı_puan}, Bilgisayar: {bilgisayar_puan}")

        galip = oyun_galibini_belirle(kullanıcı_puan, bilgisayar_puan)
        if galip:
            print(f"Oyunun Galibi {galip} oldu. Tebrikler!")
        else:
            print("Oyun Berabere Bitti!")

        devam = input("Başka bir oyun oynamak ister misiniz? (Evet/Hayır): ").strip().lower()
        if devam != "evet":
            print("Oyun bitti. Oynadığınız için teşekkürler!")
            break
        elif random.choice([True, False]):
            print("Bilgisayar yeni bir oyuna başlamak istiyor.")
        else:
            print("Bilgisayar yeni bir oyuna başlamak istemiyor.")
            print("Oyun bitti. Oynadığınız için teşekkürler!")
            break

tas_kagit_makas_Muhammed_Zeyd_KURT()


