class Vehicle:
    def __init___(self,ma,mo,ye,we,neMa = False,tsm = 0):
        self.make = ma
        self.model = mo
        self.year = ye
        self.weight = we
        self.needs_maintenance = neMa
        self.trips_since_maintenance = tsm

    #Getters
    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_weight(self):
        return self.weight
    def get_needs_maintenance(self):
        return self.needs_maintenance
    def get_trips_since_maintenance(self):
        return self.trips_since_maintenance

    #Setters
    def set_make(self,ma):
        self.make = ma
    def set_model(self,mo):
        self.model = mo
    def set_year(self,ye):
        self.year = ye
    def set_weight(self,we):
        self.weight = we
    def set_needs_maintenance(self,neMa):
        self.needs_maintenance = neMa
    def set_trips_since_maintenance(self,tsm):
        self.trips_since_maintenance = tsm

class Car(Vehicle):
    def __init__(self,idr):
        self.is_driving = idr

    def Drive(self,dr)_


