class GardenError(Exception): # burda klası exception (hata sınıfı) tanımlıyosun bu sayede hata sınıfının tüm özelliklerini alabiliyorsun
    def __init__(self, message: str = "Unknown garden error") -> None: #Bu sayede raise GardenError(...) yazabilir ve except GardenError ile yakalayabilirsin. Exception’dan türemeseydi Python bunu hata olarak tanımazdı.
        super().__init__(message) #super bir üst sınıfım demektir üst sınıfı çağırmak için kullanılır


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


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
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print()
    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print()
    print("Testing catching all garden errors...")
    for function in (raise_plant_error, raise_water_error):
        try:
            function()
        except GardenError as error:
            print(f"Caught GardenError: {error}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()

# self 
# self Python’un özel bir anahtar kelimesi değil, bir isim geleneği. Metodun (sınıf içindeki fonksiyonun) ilk parametresi olarak Python, nesnenin kendisini otomatik verir. Bu parametreye self demek gelenektir ama istersen başka isim verebilirsin: