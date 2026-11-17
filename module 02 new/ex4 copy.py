# Ex3'teki sınıflar. Her egzersiz kendi dosyasında olmak zorunda olduğu
# için import edemedik, buraya kopyaladık.
class GardenError(Exception):
    # __init__: nesne oluşturulurken otomatik çalışan kurulum fonksiyonu.
    # message varsayılan değerli parametre, verilmezse bu mesaj kullanılır.
    def __init__(self, message: str = "Unknown garden error") -> None:
        # Kendi __init__'imizi yazınca üst sınıfınki otomatik çalışmaz.
        # Mesajı elle Exception'a iletiriz, yoksa print(error) boş çıkar.
        super().__init__(message)


# PlantError, GardenError'dan türer (kalıtım).
class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    # capitalize(): ilk harfi büyütür, geri kalanı küçültür.
    # İsim kendi capitalize halinden farklıysa kurala uymuyordur:
    # "lettuce" -> "Lettuce" (farklı, hata), "Tomato" -> "Tomato" (aynı)
    # "TOMATO" -> "Tomato" (farklı, hata)
    # not plant_name: boş yazıyı yakalar. Boş yazı capitalize sonrası da
    # boş kalır ve "aynı" çıkardı, yani hatalı isim geçerli sayılırdı.
    if not plant_name or plant_name != plant_name.capitalize():
        # raise çalışırsa fonksiyon burada biter, alttaki print'e
        # gelinmez. Hatayı yakalama işi çağıran tarafa kalır.
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    # Her eleman (etiket, bitki listesi) çiftidir. Aynı kodu iki kez
    # yazmak yerine iki senaryoyu döngüyle çalıştırıyoruz.
    scenarios = [
        ("valid", ["Tomato", "Lettuce", "Carrots"]),
        ("invalid", ["Tomato", "lettuce", "Carrots"]),
    ]
    # Her turda çift ikiye ayrılır (tuple unpacking):
    # 1. tur label = "valid", 2. tur label = "invalid"
    for label, plants in scenarios:
        print()
        print(f"Testing {label} plants...")
        print("Opening watering system")
        try:
            for plant in plants:
                water_plant(plant)
        # Hata çıkarsa try'ın kalanı atlanır (sonraki bitkiler denenmez)
        # ve akış buraya gelir.
        except PlantError as error:
            print(f"Caught PlantError: {error}")
            print(".. ending tests and returning to main")
            # return fonksiyondan çıkmak ister, ama Python çıkmadan
            # önce finally bloğunu çalıştırır.
            return
        # finally: hata olsa da olmasa da, return olsa bile HER ZAMAN
        # çalışır. Kaynakları (burada sulama sistemini) kapatmak için
        # kullanılır, çünkü except sadece hata çıkarsa çalışır.
        finally:
            print("Closing watering system")


# Dosya doğrudan çalıştırılırsa testi başlatır, import edilirse
# başlatmaz.
if __name__ == "__main__":
    test_watering_system()
    # return ile main'e dönüldüğünü bu satır gösterir.
    print()
    print("Cleanup always happens, even with errors!")