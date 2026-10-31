
# clas bir sınıf eğer klasın içinde def varsa 
# bu fonksiyon değil bir metot dur sınıfın bir özelliği bir yeteneğidir
#


class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

# çalışturma olarak 

# from ft_garden_data import Plant
# rose= Plant()
# rose.name = "Rose"
# rose.height = 12
# rose.age = 3
# rose.show()

# >>> from ft_garden_data import Plant   # Yazdığın dosyadan sınıfı çağırıyorsun
# >>> rose = Plant()                     # Nesneyi oluşturuyorsun
# >>> rose.name = "Rose"                 # Adını veriyorsun
# >>> rose.height = 25                   # Boyunu veriyorsun
# >>> rose.age = 30                      # Yaşını veriyorsun
# >>> rose.show()                        # Metodu çalıştırıyorsun
