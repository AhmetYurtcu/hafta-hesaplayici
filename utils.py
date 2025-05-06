from datetime import datetime, timedelta

def tarih_to_hafta_bilgisi(dt: datetime):
    hafta_no = dt.isocalendar().week
    yil = dt.isocalendar().year

    # Haftanın pazartesi günü
    gun = dt.weekday()
    baslangic = dt - timedelta(days=gun)
    bitis = baslangic + timedelta(days=6)

    return {
        "hafta_numarasi": hafta_no,
        "yil": yil,
        "hafta_baslangic": baslangic.strftime("%Y-%m-%d"),
        "hafta_bitis": bitis.strftime("%Y-%m-%d"),
        "girdigin_tarih": dt.strftime("%Y-%m-%d")
    }
