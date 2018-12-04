class Car(object):
    """Car class"""
    def __init__(self,manufacture,model,year):
        self.manufacture = manufacture
        self.model = model
        self.year = year
        self.odometer = 0
    def get_descriptive_name(self):
        """return description"""
        long_name = str(self.year) + ' ' + self.manufacture + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print ("The meters are:" + str(self.odometer) + "KM!")
    def update_mile(self,mile):
        if mile >= self.odometer:
            self.odometer = mile
        else:
            print("It's unreasonable")
    def increment_mile(self,mile):
        self.odometer += mile
        return self.odometer
class BMW(Car):
    """ sub class BMW"""
    def __init__(self,manufacture,model,year):
        super().__init__(manufacture,model,year)
        print (super().get_descriptive_name())
        self.battery_size = "6H3.0T"
        self.Motor = Motor()
        #print (self.Motor)
    def motor(self):
        """ output parameter"""
        print (self.battery_size)
class Motor(BMW):
    """class Motor"""
    def __init__(self,Motor_size=60):
        self.Motor_size = Motor_size
    def describe_motor(self):
        print ("motor size:" + str(self.Motor_size))

my_car = Car("Benz", "EL200", 2018)
print (my_car.get_descriptive_name())
my_car.odometer = 12
my_car.update_mile(15)
my_car.increment_mile(2000)
my_car.read_odometer()
my_newcar = BMW("BMW", "Series 5", 2011)
my_newcar.Motor.describe_motor()
