class Plant:
    name: str
    height: int
    age_days: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.age_days = 30

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 80
    sunflower.age_days = 45

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.age_days = 120

    for plant in [rose, sunflower, cactus]:
        plant.show()