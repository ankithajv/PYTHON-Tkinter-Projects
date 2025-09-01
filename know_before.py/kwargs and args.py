class Car:

    def __init__(self,**kw):
        self.make  = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make = "Nissan", model = "GT-R")
#if skip writing anyone either make or model it will throw an ERROR
#to avoid ERROR we use .get("name_of_var")
print(my_car.make) 



