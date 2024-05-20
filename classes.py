class Veichle:
    def __init__(self, tire_count, initial_fuel):
        self.tire_count = tire_count
        self.fuel = initial_fuel
        
class Car(Veichle):
    
    is_on = False
     
    def __init__(self, starting_fuel = 100):
        super().__init__(4, starting_fuel)
    
    def honk(self):
        if self.is_on:
            print('honk honk...')
        else:
            print('...')
            
    def __repr__(self):
        temp = 'on' if self.is_on else 'off'
        return f"This car is {'on' if self.is_on else 'off'} and has {self.fuel} units of fuel left."
        # why this breaks if putn in directly -> no using '' or "" whitin themseves
car_1 = Car()
car_2 =Car(200)
car_1.honk()
car_1.is_on = True
car_1.honk()
print(car_1.fuel)
print(car_2.fuel)
print(car_1.tire_count)
print(car_1)