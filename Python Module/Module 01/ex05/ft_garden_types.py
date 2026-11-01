class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True
        print(f"{self.name} has bloomed into a {self.color} flower!")


# from ft_garden_types import Plant, Flower

# # 1. Normal bir bitki oluşturuyoruz
# generic_plant = Plant("Grass", 5.0, 10)
# generic_plant.show()

# print("---")

# # 2. Kalıtımla türetilmiş Çiçek oluşturuyoruz
# rose = Flower("Rose", 25.0, 30, "Red")
# # Flower sınıfında show() yazmadığımız halde miras aldığı için çalışır:
# rose.show()

# # Çiçeğe özel metodu çalıştırıyoruz:
# rose.bloom()
