class Car:
    def __init__(self,Name,Model,Year):
        self.Name = Name
        self.Model = Model
        self.Year = Year
    
    def info(self):
        print(f"Name : {self.Name} ")
        print(f"Model: {self.Model}")
        print(f"Year : {self.Year}")

c=Car("Ford","Mustang",1970)
c2=Car("VW","Virtus",2023)

c.info()
c2.info()