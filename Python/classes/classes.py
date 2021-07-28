class Vehicle:
    def __init__(self,ma,mo,ye,we,neMa = False,tsm = 0):
        self.Make = ma
        self.Model = mo
        self.Year = ye
        self.Weight = we
        self.NeedsMaintenance = neMa
        self.TripsSinceMaintenance = tsm

    def Make(self, ma):
        self.Make = ma
        return self.Make

    def Model(self, mo):
        self.Model = mo
        return self.Model

    def Year(self, ye):
        self.Year = ye
        return self.Year

    def Weight(self, we):
        self.Weight = we
        return self.Weight

    def NeedsMaintenance(self, neMa):
        self.NeedsMaintenance = neMa
        return self.NeedsMaintenance

    def TripsSinceMaintenance(self, tsm):
        self.TripsSinceMaintenance = tsm
        return self.TripsSinceMaintenance

    def printVehicle(self):
        print(self.Make, self.Model, self.Year, self.Weight, self.NeedsMaintenance, self.TripsSinceMaintenance)


class Cars(Vehicle):
    def __init__(self,ma,mo,ye,we,neMa=False,tsm=0,isD = False):
        Vehicle.__init__(self,ma,mo,ye,we,neMa = False,tsm = 0)
        self.isDriving = isD
        if self.TripsSinceMaintenance >= 3:
            self.NeedsMaintenance = True

    
    def Drive(self):
        if self.isDriving == False:
            self.isDriving = True

    def Stop(self):
        if self.isDriving == True:
            self.TripsSinceMaintenance += 1
            self.isDriving = False

    def Maintenance(self):
        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True
            return self.NeedsMaintenance
        else:
            self.NeedsMaintenance = False
            return self.NeedsMaintenance
    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False


    def printCar(self):
        print(self.Make,self.Model,self.Year,self.Weight,self.Maintenance(),self.TripsSinceMaintenance,self.isDriving)

carOne = Cars('Nissan', 'Sentra', 2020, '1.359kg')
carTwo = Cars('Volkswagen', 'Jetta', 2020, '1.355kg')
carThree = Cars('Mazda', '3', 2020, '1.320kg')

#Trips loop

#carOne 80 trips
for i in range(80):
    carOne.Drive()
    carOne.Stop()


#carTwo 120 trips
for i in range(120):
    carTwo.Drive()
    carTwo.Stop()

#carThree 100 trips
for i in range(100):
    carThree.Drive()
    carThree.Stop()

#Print Cars
carOne.printCar()
carTwo.printCar()
carThree.printCar()