class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price
    def set_model(self, new_model):
        self.model = new_model
    def set_year(self, new_year):
        self.year = new_year

    def set_price(self, new_price):
        self.price = new_price

    def discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount
    def car_age(self, current_year):
        return current_year - self.year

car = Car("Toyota Corolla", 2018, 15000)
print(car.get_model())
print(car.get_year())
print(car.get_price())

car.set_model("Honda Civic")
car.set_year(2020)
car.set_price(16000)
print(car.get_model())
print(car.get_year())
print(car.get_price())

car.discount(10)
print(car.get_price())

car_age = car.car_age(2024)
print(f"Avtomobilning yoshi: {car_age} yil.")
