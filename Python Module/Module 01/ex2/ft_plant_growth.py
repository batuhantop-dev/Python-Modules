class Plant:
    name: str
    height: float
    age_days: int
    growth_rate: float

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age_days = 30
    rose.growth_rate = 0.8

    start_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()
    growth = round(rose.height - start_height, 1)
    print(f"Growth this week: {growth}cm")