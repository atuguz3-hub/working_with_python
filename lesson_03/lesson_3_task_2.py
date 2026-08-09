from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79991111111"),
    Smartphone("Samsung", "Galaxy S24", "+79992222222"),
    Smartphone("Xiaomi", "13T", "+79993333333"),
    Smartphone("Honor", "Magic6", "+79994444444"),
    Smartphone("Google", "Pixel 9", "+79995555555")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")