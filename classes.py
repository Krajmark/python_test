class Car:
    
    isOn = False
     
    def __init__(self, starting_fuel = 100):
        self.fuel = starting_fuel
    
    def honk(self):
        if self.isOn:
            print('honk honk...')
        else:
            print('...')
            
car_1 = Car()
car_2 =Car(200)
car_1.honk()
car_1.isOn = True
car_1.honk()
print(car_1.fuel)
print(car_2.fuel)