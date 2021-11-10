
class Musteri:

    def __init__(self, ad, merkez, bakiye, tel):
        self.ad = ad
        self.merkez = merkez
        self.tel = tel
        self.bakiye = bakiye

    def musteri_adini_yazdir(self):
        return self.ad

    def musteri_bankasi(self):
        return self.merkez

    def musteri_tel(self):
        return self.tel

    def musteri_bakiye(self):
        return self.bakiye

    def para_yatir(self, eklenecek_para_miktari):
        self.bakiye += eklenecek_para_miktari

    def para_cek(self, cikarilacak_para_miktari):
        self.bakiye -= cikarilacak_para_miktari
