#Soal 1
def convert_temperature(value, unit):
    if unit == 'C':
        fahrenheit = (value * 9/5) + 32
        return fahrenheit
    elif unit =='F':
        celcius = (value - 32) * 5/9
        return celcius
    else:
        return "Pilih hanya C atau F "

temperature_value = float(input("Masukkan nilai : "))
temperature_unit = input("Masukkan nilai suhu ('C' untuk Celsius, 'F' untuk Fahrenheit): ")
converted_temperature = convert_temperature(temperature_value, temperature_unit)
print(f"{temperature_value}°{temperature_unit} setara dengan {converted_temperature}°{'C' if temperature_unit == 'F' else 'F'}")

#Soal 2
square_area = lambda side_length: side_length**2

side_length = float(input("Masukkan panjang sisi persegi : "))
area = square_area(side_length)
print(f"Luas persegi dengan panjang sisi {side_length} adalah {area} satuan")