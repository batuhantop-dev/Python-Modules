class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def count_grow(self) -> None:
            self._grow_calls += 1

        def count_age(self) -> None:
            self._age_calls += 1

        def count_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._stats = Plant._Stats()
        if height < 0:
            print(f"{name}: Error, height can't be negative")
        else:
            self._height = height
        if age < 0:
            print(f"{name}: Error, age can't be negative")
        else:
            self._age = age

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height:g}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> "Plant._Stats":
        return self._stats

    def show(self) -> None:
        self._stats.count_show()
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self, amount: float = 1.0) -> None:
        self._stats.count_grow()
        self._height = round(self._height + amount, 1)

    def age(self, days: int = 1) -> None:
        self._stats.count_age()
        self._age += days


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def count_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._tree_stats = Tree._TreeStats()
        self._stats = self._tree_stats

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._tree_stats.count_shade()
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, amount: float = 1.0) -> None:
        super().grow(amount)
        self._nutritional_value += 1

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    for days in (30, 400):
        print(f"Is {days} days more than a year? -> "
              f"{Plant.is_older_than_year(days)}")

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_stats(rose)

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    print()
    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_stats(unknown)