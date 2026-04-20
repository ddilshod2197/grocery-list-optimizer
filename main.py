class Xona:
    def __init__(self, raqam, tur, narx):
        self.raqam = raqam
        self.tur = tur
        self.narx = narx
        self.bron = False

class Hotel:
    def __init__(self):
        self.xonalar = []

    def qo'sh_xona(self, xona):
        self.xonalar.append(xona)

    def sana_bo'yicha_bandlik(self, sana):
        band_xonalar = [xona for xona in self.xonalar if xona.bron and xona.bron_sana == sana]
        return band_xonalar

    def bron_xona(self, sana, raqam):
        band_xonalar = self.sana_bo'yicha_bandlik(sana)
        for xona in self.xonalar:
            if xona.raqam == raqam and not xona.bron:
                xona.bron = True
                xona.bron_sana = sana
                return f"Xona {raqam} {sana} sana uchun bron qilindi."
        if band_xonalar:
            return f"Xona {band_xonalar[0].raqam} {sana} sana uchun band."
        return f"Xona {raqam} {sana} sana uchun topilmadi."

    def ozgacha_xona(self, sana):
        ozgacha_xonalar = [xona for xona in self.xonalar if not xona.bron]
        return ozgacha_xonalar

hotel = Hotel()
hotel.qo'sh_xona(Xona(1, "standart", 100))
hotel.qo'sh_xona(Xona(2, "standart", 100))
hotel.qo'sh_xona(Xona(3, "standart", 100))

print(hotel.bron_xona("2024-04-20", 1))
print(hotel.bron_xona("2024-04-20", 2))
print(hotel.bron_xona("2024-04-20", 3))
print(hotel.bron_xona("2024-04-20", 1))
print(hotel.bron_xona("2024-04-20", 2))
print(hotel.bron_xona("2024-04-20", 3))
print(hotel.bron_xona("2024-04-21", 1))
print(hotel.bron_xona("2024-04-21", 2))
print(hotel.bron_xona("2024-04-21", 3))
```

Kodda quyidagilar mavjud:

- `Xona` classi xonalar haqida ma'lumot saqlaydi: raqam, tur, narx va bron qilinganligi haqida ma'lumot.
- `Hotel` classi hotel haqida ma'lumot saqlaydi: xonalar ro'yxati.
- `qo'sh_xona` metodi hotelga xona qo'shadi.
- `sana_bo'yicha_bandlik` metodi sana bo'yicha band xonalar ro'yxatini qaytaradi.
- `bron_xona` metodi sana va raqam bo'yicha xona bron qiladi yoki band xona topilganligini ko'rsatadi.
- `ozgacha_xona` metodi sana bo'yicha ozgacha xonalar ro'yxatini qaytaradi.
