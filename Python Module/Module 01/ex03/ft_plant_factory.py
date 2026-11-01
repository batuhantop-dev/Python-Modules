class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

from ft_plant_factory import Plant

# Nesne doğduğu an ismi, boyu ve yaşı bellidir:
rose = Plant("Rose", 25.0, 30)
cactus = Plant("Cactus", 15.0, 120)

print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")
