def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    for value in ("25", "abc"):
        print(f"Input data is '{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp}°C")
        except ValueError as error: # value error çıkarsa yakala onu error adıyla bana ver
            print(f"Caught input_temperature error: {error}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__": # dosya doğrudan çalıştırıldıysa çalıştır import edildiyse çalıştırma 
    test_temperature()

#if name açıklaması 
# python dosyayı çalıştırırken her dosyaya __name__ adında bir değişken verir 
# bu değişkende çalıştırma şekline göre isimlendirilir 
# eğer terminalde python3 dosyaadı şeklinde çalıştırıcaksanız __main__ adına gelir
# veya import ederek çalıştırıcaksanız o zamanda dosyanın adı olur 
# burda bunu yazmamızın nedeni 
# birden fazla fonksiyon olduğu zaman birini import ettiğimizde sadece fonksiyonu alabilir tüm kodu çalıştırmaz 


# Hata türleri 
# valueerror = değer çakışması değer uygun değil int("abc") gibi 
# zero division error sıfıra bölünmez hatası 
# typeerror uyumsuz türler "abc" + 5 
# filenotfounderror olmayan dosyayı açma

# Döngü bitince son mesaj yazdırılır.
# Bu mesaj, program hata yaşamasına rağmen çökmeden sonuna kadar geldiğinin kanıtıdır.
