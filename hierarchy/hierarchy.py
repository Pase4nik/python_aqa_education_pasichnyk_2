from abc import ABC, abstractmethod
from termcolor import colored, cprint


class Transport(ABC):
    class_message = colored('\033[96m Specific Class feature')
    transports = {}
    n = 0

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
        print(colored('\033[95mMethod from Transport class'), f'''Transport type: {self.type}
Brand: {self.brand}
Model: {self.model}
Color: {self.color}
Year: {self.year}
Distance driven: {self.km}''', sep='\n')

    def __str__(self):
        cprint(f"__Str method from Transport class", 'yellow')
        print_str = f"{self.transport_status()}"
        cprint(print_str)


class ClassicCar(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            self.fuel_tank = kwargs['fuel_tank']
        elif args:
            self.fuel_tank = args[6]

    def transport_status(self, *args, **kwargs):
        super().transport_status()
        return f'Fuel capacity: ' + str(self.fuel_tank) + self.class_message

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
        print('Energy Storage (Kwh): ' + str(self.energy_storage) + self.class_message)


class HighPerformance(ClassicCar):
    def __init__(self, horse_power, top_speed, *args, **kwargs):
        self.horse_power = horse_power
        self.top_speed = top_speed
        ClassicCar.__init__(self, *args, **kwargs)

    def transport_status(self):
        ClassicCar.transport_status(self)
        print('Horse power: ' + str(self.horse_power) + self.class_message)
        print('Top speed: ' + str(self.top_speed) + self.class_message)


class SportCar(HighPerformance):
    def __init__(self, gear_box, drive_system, *args, **kwargs):
        self.gearbox = gear_box
        self.drive_system = drive_system
        HighPerformance.__init__(self, *args, **kwargs)

    def transport_status(self):
        HighPerformance.transport_status(self)
        print('Gear box: ' + self.gearbox + self.class_message)
        print('Drive system: ' + self.drive_system + self.class_message)

    def __add__(self, other):
        acceleration = self.top_speed + other.top_speed
        horse_power = self.horse_power + other.horse_power
        return horse_power, acceleration


class HeavyVehicle(ClassicCar):
    def __init__(self, max_weight, wheels, length, *args, **kwargs):
        self.max_weight = max_weight
        self.wheels = wheels
        self.length = length
        ClassicCar.__init__(self, *args, **kwargs)

    def transport_status(self):
        ClassicCar.transport_status(self)
        print('Maximum load (tons): ' + str(self.max_weight) + self.class_message)
        print('Wheels: ' + str(self.wheels) + self.class_message)
        print('Length (m): ' + str(self.length) + self.class_message)


class SnowTruck(HeavyVehicle):
    def __init__(self, snow_throwing_length, *args, **kwargs):
        self.snow_throwing_length = snow_throwing_length
        HeavyVehicle.__init__(self, *args, **kwargs)

    def transport_status(self):
        HeavyVehicle.transport_status(self)
        print('Snow throwing length: ' + str(self.snow_throwing_length) + self.class_message)

    @abstractmethod
    def start(self):
        ...


class Bus(HeavyVehicle):
    def __init__(self, seats, * args, **kwargs):
        self.seats = seats
        HeavyVehicle.__init__(self, *args, **kwargs)

    def transport_status(self):
        HeavyVehicle.transport_status(self)
        print('Number of seats: ' + str(self.seats) + self.class_message)

    @classmethod
    def class_meth(cls):
        print(f'method called with cls={cls}')


def main():
    bmw = ClassicCar('sedan', 'BMW', 'X5', 'silver', 2020, 10000, 35)
    bmw.__str__()
    print('\n======================\n')

    print(bmw.transport_status())
    print('\n======================\n')

    tesla = ElectricCar(300, 'sport', 'Tesla', 'Model S', 'red', 2020, 5000)
    tesla.transport_status()

    print('\n======================\n')
    lamborghini = SportCar('manual', 'rear wheel', 650, 220, 'coupe', 'Lamborghini',
                           'race car', 'red', 2014, 3500, 65)
    lamborghini.transport_status()

    print('\n======================\n')
    bohdan = Bus(55, 1, 8, 20, type='263', brand='Bohdan', model='Armenia',
                 color='yellow', year=1978, km=99999, fuel_tank=80)
    bohdan.transport_status()

    print('\n======================\n')
    ferrari = SportCar('auto', '4 wheel drive', 800, 320, 'coupe', 'Ferrari',
                       'race car', 'yellow', 2020, 1000, 80)
    cprint('__add method implemented', 'yellow')
    print(lamborghini + ferrari)


if __name__ == '__main__':
    main()
