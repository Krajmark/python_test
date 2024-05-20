class Car():
    fuel = 100
    isOn = False
    
    def honk(self):
        if self.isOn:
            print('honk honk...')
        else:
            print('...')
            
car_1 = Car()
car_1.honk()
car_1.isOn = True
car_1.honk()