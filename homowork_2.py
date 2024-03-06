class Vehicle:
    
    vehicle_count = int()

    def __init__(self,make,model) -> None:
        self.make = make
        self.model = model
        Vehicle.increment_vehicle_count()

    def increment_vehicle_count():
        Vehicle.vehicle_count += 1

    def get_vehicle_count():
        return Vehicle.vehicle_count
    

    def start_engine(self):
        print("Engine started")

        


class Car(Vehicle):
    
    def __init__(self, make, model,number_if_wheels=4) -> None:
        super().__init__(make, model)
        
        self.number_if_wheels = number_if_wheels
        

    def __repr__(self) -> str:
        return f"-->Car object--\nmodel: {self.model}\nmake: {self.make}\n<--Car object--"
    
    def start_engine(self):
        
        print("Car engine started")
        super().start_engine()
        
        
        


class ElectricVehicle:

    def __init__(self,battery_capacity) -> None:
        self.battery_capacity = battery_capacity



class ElectricCar(Car,ElectricVehicle):
        
        def __init__(self, make, model,battery_capacity,number_if_wheels=4) -> None:
           super().__init__(make, model,number_if_wheels)
           super(ElectricVehicle).__init__(battery_capacity)

        
        def __repr__(self) -> str:
            return f"--ElectricCar object--\nmodel: {self.model}\nmake: {self.make}\n--ElectricCar object"




car = Car(make="Zaz",model="Tavria")
print(car)
# print(Vehicle.get_vehicle_count())
# print(Car.get_vehicle_count())
# print(Car.mro())
# Vehicle.start_engine()
Car.start_engine(car)
electric_car = ElectricCar(make="Tesla",model="N4",battery_capacity=100,number_if_wheels=8)
# print(electric_car)
print(ElectricCar.mro())

