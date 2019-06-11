from tkinter import *

anaform = Tk()

anaform.title("katalog")


def verial():
    veri = giris.get()
    veritabani = open("list.txt", "a+")
    if veri=="1":
        etiket2.config(text="Kitaplarımız şunlardır:", font=("Flux", 24, "bold"), fg="red")
        araetiket.config(text="_________________________", font=("Flux", 24, "bold"), fg="red")
        veritabani.seek(0)
        etiket3.config(text=veritabani.read(), font=("Corbal", 12))
    elif veri=="2":
        ekle()
    elif veri=="3":
        bul1()
    elif veri=="4":
        bul2()
    elif veri=="5":
        bul3()
def bul1():
    kişi_defteri = {"yaşar kemal": "kuşlar da gitti ve yılanı öldürseler",
                    "samed behrengi": "küçük kara balık",
                    "aziz nesin": "ah biz eşşekler ve şiirler",
                    "servin sarıyer": "masallar"}

    kişi = input("Yazar adı girin: ")

    if kişi in kişi_defteri:
        cevap = "{} 'in kitabı: {}"
        print(cevap.format(kişi, kişi_defteri[kişi]))
    else:
        print("Aradığınız kişi katalogda yok..")
def bul2():
    kitap_defteri = {"kuşlar da gitti": "yaşar kemal",
                     "küçük kara balık": "samed behrengi",
                     "ah biz eşşekler": "aziz nesin",
                     "masallar": "servin sarıyer",
                     "yılanı öldürseler": "yaşar kemal",
                     "şiirler": "aziz nesin"}

    kitap = input("Kitap adı girin: ")

    if kitap in kitap_defteri:
        cevap = "{} yazarı: {}"
        print(cevap.format(kitap, kitap_defteri[kitap]))
    else:
        print("Aradığınız kitap katalogda yok..")
def bul3():
    yıl_defteri = {"2018": "küçük kara balık-samed behrengi",
                   "1965": "yılanı öldürseler-yaşar kemal",
                   "1960": "ah biz eşşekler-aziz nesin",
                   "2019": "masallar-servin sarıyer",
                   "1969": "yılanı öldürseler-yaşar kemal",
                   "2004": "şiirler-aziz nesin"}
    yıl = input("Yıl girin: ")

    if yıl in yıl_defteri:
        cevap = "{} yılı: {}"
        print(cevap.format(yıl, yıl_defteri[yıl]))
    else:
        print("Aradığınız yıl katalogda yok..")

def ekle():
    list = open("list.txt")
    print(list.read())
    with open("list.txt", "a") as f:
        f.write("\nAziz Nesin: Şiirler :2004")


girisekrani = Label(text="""-katolog icin 1'i 
-kitap eklemek için 2'yi 
 -kişiye göre arama için 3'ü tuşlayınız
 -kitaba göre 4
 -yıla göre 5:) 
""", font=(24))
girisekrani.pack()

etiket = Label(text="Seçimizi yapınız: ", font=(24))
etiket.pack()

giris = Entry()
giris.pack()

giris2 = Entry()

buton2 = Button(text="Ekle!", command=ekle, font=(24))

buton = Button(text="Gir!", command=verial, font=(24))
buton.pack(expand="yes", anchor="center")

etiket2 = Label(text="")
etiket2.pack()

araetiket = Label(text="")
araetiket.pack()

etiket3 = Label()
etiket3.pack()

mainloop()

pencere.mainloop()