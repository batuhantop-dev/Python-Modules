class Plant:
    name: str
    height: float
    age: int
    growth_rate: float

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age_one_day(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")



# from ft_plant_growth import Plant

# # 1. Bitkiyi oluştur ve başlangıç değerlerini ver
# rose = Plant()
# rose.name = "Rose"
# rose.height = 25.0
# rose.age = 30
# rose.growth_rate = 0.8

# # İlk boyu hafızaya al (haftalık toplam büyümeyi hesaplamak için)
# initial_height: float = rose.height

# print("=== Garden Plant Growth ===")
# rose.show()

# # 2. 7 günlük büyüme döngüsü
# for day in range(1, 8):
#     print(f"=== Day {day} ===")
#     rose.grow()          # Boyunu artır
#     rose.age_one_day()   # Yaşını 1 gün artır
#     rose.show()          # Yeni durumunu yazdır

# # 3. Haftalık toplam büyümeyi yazdır
# total_growth: float = round(rose.height - initial_height, 1)
# print(f"Growth this week: {total_growth:.1f}cm")
