from smartphone import Smartphone

catalog = [
    Smartphone("Apple iPhone", "14", "+7(495) 123-45-67"),
    Smartphone("Samsung Galaxy", "S23", "+7(495) 234-56-78"),
    Smartphone("Google Pixel", "7", "+7(495) 345-67-89"),
    Smartphone("OnePlus", "11", "+7(495) 456-78-90"),
    Smartphone("Xiaomi", "13", "+7(495) 567-89-01")
]


for smartphone in catalog:
    print(f"{smartphone.brand}-{smartphone.model}. {smartphone.phone_number}")
