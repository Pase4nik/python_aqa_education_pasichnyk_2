class Transport:
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.type = kwargs['type']
            self.brand = kwargs['brand']
            self.model = kwargs['model']
            self.color = kwargs['color']
            self.year = kwargs['year']
            self.km = kwargs['km']
        elif args:
            self.type = args[0]
            self.brand = args[1]
            self.model = args[2]
            self.color = args[3]
            self.year = args[4]
            self.km = args[5]

    def transport_status(self):
        print(f'''Transport type: {self.type}
Brand: {self.brand}
Model: {self.model}
Color: {self.color}
Year: {self.year}
Distance driven: {self.km}''')


class ClassicCar(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            self.fuel_tank = kwargs['fuel_tank']
        elif args:
            self.fuel_tank = args[6]

    def transport_status(self, *args, **kwargs):
        super().transport_status()
        return f'Fuel capacity: ' + str(self.fuel_tank)

    @staticmethod
    def vroom():
        print('Vroom-vroom static')

    def vroom_vroom(self):
        return f'''{self.brand} says vroom-vroom!'''


class ElectricCar(Transport):
    def __init__(self, energy_storage, *args, **kwargs):
        self.energy_storage = energy_storage
        Transport.__init__(self, *args, **kwargs)

    def transport_status(self):
        Transport.transport_status(self)
        print('Energy Storage (Kwh): ' + str(self.energy_storage))


class HighPerformance(ClassicCar):
    def __init__(self, horse_power, top_speed, *args, **kwargs):
        self.horse_power = horse_power
        self.top_speed = top_speed
        ClassicCar.__init__(self, *args, **kwargs)

    def transport_status(self):
        ClassicCar.transport_status(self)
        print('Horse power: ' + str(self.horse_power))
        print('Top speed: ' + str(self.top_speed))


class SportCar(HighPerformance):
    def __init__(self, gear_box, drive_system, *args, **kwargs):
        self.gearbox = gear_box
        self.drive_system = drive_system
        HighPerformance.__init__(self, *args, **kwargs)

    def transport_status(self):
        HighPerformance.transport_status(self)
        print('Gear box: ' + self.gearbox)
        print('Drive system: ' + self.drive_system)


class HeavyVehicle(ClassicCar):
    def __init__(self, max_weight, wheels, length, *args, **kwargs):
        self.max_weight = max_weight
        self.wheels = wheels
        self.length = length
        ClassicCar.__init__(self, *args, **kwargs)

    def transport_status(self):
        ClassicCar.transport_status(self)
        print('Maximum load (tons): ' + str(self.max_weight))
        print('Wheels: ' + str(self.wheels))
        print('Length (m): ' + str(self.length))


class SnowTruck(HeavyVehicle):
    def __init__(self, snow_throwing_length, *args, **kwargs):
        self.snow_throwing_length = snow_throwing_length
        HeavyVehicle.__init__(self, *args, **kwargs)

    def transport_status(self):
        HeavyVehicle.transport_status(self)
        print('Snow throwing length: ' + str(self.snow_throwing_length))


class Bus(HeavyVehicle):
    def __init__(self, seats, * args, **kwargs):
        self.seats = seats
        HeavyVehicle.__init__(self, *args, **kwargs)

    def transport_status(self):
        HeavyVehicle.transport_status(self)
        print('Number of seats: ' + str(self.seats))

    @classmethod
    def class_meth(cls):
        print(f'method called with cls={cls}')


def main():
    bmw = ClassicCar('sedan', 'BMW', 'X5', 'silver', 2020, 10000, 35)
    print(bmw.transport_status())
    print('\n======================\n')
    tesla = ElectricCar(300, 'sport', 'Tesla', 'Model S', 'red', 2020, 5000)
    tesla.transport_status()
    print('\n======================\n')
    lamborghini = SportCar('manual', 'rear wheel', 650, 220, 'coupe', 'Lamborghini',
                           'race car', 'dark silver', 2014, 3500, 65)
    lamborghini.transport_status()
    print('\n======================\n')
    bohdan = Bus(55, 1, 8, 20, type='263', brand='Bohdan', model='Armenia',
                 color='yellow', year=1978, km=99999, fuel_tank=80)
    bohdan.transport_status()


if __name__ == '__main__':
    main()
