class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def grow(self) -> None:
        self.height = round(self.height + 1.0, 1)

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    # Üst sınıftaki grow() metodunu eziyoruz (Overriding):
    def grow(self) -> None:
        self.height = round(self.height + 2.0, 1)

    def show(self) -> None:
        print(f"{self.name} ({self.color}): {self.height:.1f}cm, "
              f"{self.age} days old (blooming)")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    # Ağaç için grow() metodunu farklı eziyoruz:
    def grow(self) -> None:
        self.height = round(self.height + 0.5, 1)
        self.trunk_diameter = round(self.trunk_diameter + 0.2, 1)

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old, "
              f"trunk: {self.trunk_diameter:.1f}cm")

from ft_garden_diversity import Plant, Flower, Tree

garden = [
    Plant("Grass", 5.0, 10),
    Flower("Rose", 20.0, 15, "Red"),
    Tree("Oak", 200.0, 365, 15.0)
]

print("=== Before Growth ===")
for plant in garden:
    plant.show()

# Tek bir döngüyle her birinin kendi özel grow() metodunu çalıştırıyoruz:
print("\n=== Growing All Plants ===")
for plant in garden:
    plant.grow()
    plant.show()
