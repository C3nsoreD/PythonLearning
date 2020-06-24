"""
Some examples of instance, static and class methods 
"""

class CoffeeShop:
    speciality = 'espresso'

    def __init__(self, coffee_price):
        self.coffee_price = coffee_price

    # instance method 
    def make_coffee(self):
        print(f'Making {self.speciality} for ${self.coffee_price}')

    # static method 
    @staticmethod
    def check_weather():
        print('Its cloudy')
    
    # class method 
    @classmethod
    def change_speciality(cls, speciality):
        cls.speciality = speciality
        print(f'Speciality changed to {speciality}')

    
if __name__ == "__main__":
    coffee_shop = CoffeeShop('5')
    coffee_shop.make_coffee()   #=> Making espresso for $5
    coffee_shop.check_weather() 
    coffee_shop.change_speciality('drip coffee')
    coffee_shop.make_coffee()
