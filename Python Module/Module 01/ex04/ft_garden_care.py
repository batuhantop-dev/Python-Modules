class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.health: int = 100

    def water(self, amount: int) -> None:
        self.health = min(100, self.health + amount)
        print(f"{self.name} watered: health is now {self.health}")

    def inspect(self) -> None:
        status: str = "healthy" if self.health > 50 else "needs care"
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old, "
              f"health: {self.health}% ({status})")

from ft_garden_care import Plant

rose = Plant("Rose", 25.0, 30)

print("=== First Inspection ===")
rose.inspect()

print("\n=== Simulating Damage ===")
rose.health = 40
rose.inspect()

print("\n=== Watering ===")
rose.water(25)
rose.inspect()

print("\n=== Over-Watering ===")
rose.water(50)
rose.inspect()
