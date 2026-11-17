# Kendi hata türümüz. Exception'dan türediği için raise edilebilir ve
# except ile yakalanabilir (kalıtım / inheritance).
class GardenError(Exception):
    # __init__: nesne oluşturulurken Python'un otomatik çalıştırdığı
    # kurulum fonksiyonu. self = oluşturulan hata nesnesinin kendisi.
    # message = varsayılan değerli parametre. Mesaj verilmezse
    # "Unknown garden error" kullanılır.
    def __init__(self, message: str = "Unknown garden error") -> None:
        # super() = üst sınıf (Exception). Kendi __init__'imizi yazınca
        # üst sınıfınki otomatik çalışmaz, o yüzden mesajı elle iletiriz.
        # Yazmasaydık print(error) boş çıkardı.
        super().__init__(message)


# PlantError, GardenError'dan türer: her PlantError aynı zamanda
# bir GardenError'dır. Bu yüzden except GardenError bunu da yakalar.
class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        # Mesaj GardenError'a, o da Exception'a iletilir.
        super().__init__(message)


# WaterError de GardenError'dan türer, PlantError ile kardeş sınıftır.
class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


# Bu fonksiyon sadece hata fırlatır (raise), yakalamaz.
# Yakalama işini test_custom_errors yapar.
def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        raise_plant_error()
    # Sadece PlantError yakalanır. WaterError çıksaydı yakalanmazdı.
    except PlantError as error:
        # error bizim seçtiğimiz isim. Hata nesnesinin mesajını tutar.
        print(f"Caught PlantError: {error}")
    print()
    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print()
    print("Testing catching all garden errors...")
    # Fonksiyonlar Python'da değer gibi taşınabilir. İki fonksiyonu
    # demete koyup sırayla çağırıyoruz, aynı try/except'i iki kez
    # yazmamak için.
    for function in (raise_plant_error, raise_water_error):
        try:
            function()
        # Tek except GardenError iki hatayı da yakalar, çünkü
        # PlantError ve WaterError, GardenError'ın alt sınıflarıdır.
        # Not: hem alt hem üst sınıf yazılacaksa alt sınıf ÖNCE yazılır,
        # yoksa üst sınıf her şeyi yakalar.
        except GardenError as error:
            print(f"Caught GardenError: {error}")
    print()
    print("All custom error types work correctly!")


# Dosya doğrudan çalıştırılırsa testi başlatır, import edilirse
# başlatmaz.
if __name__ == "__main__":
    test_custom_errors()