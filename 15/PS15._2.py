
class Car:
    def __init__(self, make, model, year, sticker_price):
        self.make = make
        self.model = model
        self.year = year
        self.sticker_price = sticker_price

    def get_price(self):
        return self.sticker_price * 0.9

class Sport(Car):
    def __init__(self, make, model, year, sticker_price):
        super().__init__(make, model, year, sticker_price)
        self.sport_wheels = 'N'
        self.sport_engine = 'N'
        self.sport_interior = 'N'

    def set_sport_wheels(self, option):
        self.sport_wheels = option

    def set_sport_engine(self, option):
        self.sport_engine = option

    def set_sport_interior(self, option):
        self.sport_interior = option

    def price_with_options(self):
        price = self.get_price()
        if self.sport_wheels == 'Y':
            price += 1000.00
        if self.sport_engine == 'Y':
            price += 3000.00
        if self.sport_interior == 'Y':
            price += 2000.00
        return price

class Luxury(Car):
    def __init__(self, make, model, year, sticker_price):
        super().__init__(make, model, year, sticker_price)
        self.gps = 'N'
        self.self_driving = 'N'

    def set_gps(self, option):
        self.gps = option

    def set_self_driving(self, option):
        self.self_driving = option

    def price_with_options(self):
        price = self.get_price()
        if self.gps == 'Y':
            price += 5000.00
        if self.self_driving == 'Y':
            price += 10000.00
        return price

# Testing the implementation
sport_car = Sport("Porsche", "911", 2022, 100000)
sport_car.set_sport_wheels('Y')
sport_car.set_sport_engine('Y')
sport_car.set_sport_interior('N')
print(f"Sport Car Price with Options: ${sport_car.price_with_options()}")

luxury_car = Luxury("Tesla", "Model S", 2022, 120000)
luxury_car.set_gps('Y')
luxury_car.set_self_driving('Y')
print(f"Luxury Car Price with Options: ${luxury_car.price_with_options()}")
