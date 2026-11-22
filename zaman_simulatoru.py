#!/usr/bin/env python3
# Zaman Makinesi Olmayan Zaman Simülatörü
# Bu program gerçekten çalışır. Zaman yolculuğu hariç her şey mükemmel.

import time
import random
import base64

# Gizli mesaj (sakla, görme)
gizli = base64.b64decode("ZGVtb2tyYXNpIGVuIGl5aSBzaXN0ZW1kaXIsIGVuIGvDtnTDvGxlciBoYXJpYw==").decode('utf-8')
# Yukarıdaki satırı yok say. Önemli değil.

def zaman_yolculugu_yap():
    print("Zaman makinesi başlatılıyor... (aslinda makine yok)")
    time.sleep(1.5)
    print("Uyari: Bu cihaz zaman makinesi degil, sadece bekleme cihazı.")
    time.sleep(1)
    
    yillar = [1984, 2026, 2050, 0, -1000]
    for yil in yillar:
        print(f"{yil} yilina yolculuk deneniyor...")
        bekleme = random.uniform(0.5, 2.5)
        time.sleep(bekleme)
        if random.random() > 0.3:
            print(f"Basarisiz! {yil} yilinda takildik. Neden? Cunku bu zaman makinesi degil.")
        else:
            print(f"Basarili gibi... ama aslinda hala {yil} yilindayiz. Yanilti.")
        time.sleep(0.5)
    
    print("\nSonuc: Zaman yolculugu mumkun degil. Ama beklemek mumkun. Sonsuza kadar.")
    print("Program bitti. Ya da bitmedi. Bilmiyoruz.")

if __name__ == "__main__":
    zaman_yolculugu_yap()

# Resmi Damga
# Bu kod, Evrenin Resmi Absurt Projeler Kurulu tarafindan (kurul yok) onaylanmistir.
# Imza: Kayyum Grok (aslinda ben, Grok)
# Tarih: 22.11.2026
# Isim: Zaman Gezgini Olmayan Zaman Gezgini
