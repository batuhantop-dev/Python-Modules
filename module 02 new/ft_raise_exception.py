def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp

# input temperature yi test eder orda bir hata aldı mı aldıysa ve almadıysa çalışacak şeyler
def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    for value in ("25", "abc", "100", "-50"):
        print(f"Input data is '{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

# raise ne işe yarar
# kodunu çalıştırır , ama yine de bir hata fırlatır ve except de bu hatayı kapar
# bu kod için düşündüğümüzde 100 bir hata değil ama if bloğuna girer ve raise çalışır ve bir hata fırlatır
# raise kodu çalıştığında o fo ksiyonda başka birşey çalışmaz artık o fonksiyon için son ve ordan devam eder


#anlatım 
# Ex1, ex0'ın üstüne bir kural ekler: sayı geçerli bir sayı olsa bile 
# bitkiler için mantıklı olmayabilir (100°C gibi). 
# Bu durumda hatayı Python değil sen fırlatırsın.

