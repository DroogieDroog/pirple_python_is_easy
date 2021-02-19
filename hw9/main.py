"""
pirple/python/hw9/main.py
Homework Assignment #9

Create a Vehicle class, with Cars and Planes
 as inheritance classes
"""

class Vehicle:

    def __init__(self, make, mod, yr, wt, maint=False, trips=0):
        self.Make = make
        self.Model = mod
        self.Year = yr
        self.Weight = wt
        self.NeedsMaintenance = maint
        self.TripsSinceMaintenance = trips

    def __str__(self):
        ret = 'Make: {}'.format(self.Make) + '\n' + 'Model: {}'.format(self.Model) + '\n' +\
              'Year: {}'.format(self.Year) + '\n' + 'Weight: {}'.format(self.Weight) + '\n' +\
              'Needs maintenance: {}'.format(self.NeedsMaintenance) + '\n' +\
              'Trips since last maintenance: {}'.format(self.TripsSinceMaintenance)
        return ret


class Cars(Vehicle):

    def __init__(self, make, mod, yr, wt, maint=False, trips=0, tot=0, reps=0, isDrv=False):
        Vehicle.__init__(self, make, mod, yr, wt, maint, trips)
        self.TotalTrips = tot
        self.TotalRepairs = reps
        self.IsDriving = isDrv

    def __str__(self):
        ret = Vehicle.__str__(self) + '\n' + 'Total trips taken: {}'.format(self.TotalTrips) + '\n' +\
              'Total number of repairs: {}'.format(self.TotalRepairs) + '\n' + 'Driving now: {}'.format(self.IsDriving)
        return ret

    def Drive(self):
        self.IsDriving = True

    def Stop(self):
        if self.IsDriving:
            self.TripsSinceMaintenance += 1
            self.TotalTrips += 1
            if self.TripsSinceMaintenance >= 100:
                self.NeedsMaintenance = True
        self.IsDriving = False

    def Repair(self):
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0
        self.TotalRepairs += 1


class Planes(Vehicle):

    def __init__(self, make, mod, yr, wt, maint=False, trips=0, tot=0, reps=0, isFly=False):
        Vehicle.__init__(self, make, mod, yr, wt, maint, trips)
        self.TotalTrips = tot
        self.TotalRepairs = reps
        self.IsFlying = isFly

    def __str__(self):
        ret = Vehicle.__str__(self) + '\n' + 'Total trips taken: {}'.format(self.TotalTrips) + '\n' +\
              'Total number of repairs: {}'.format(self.TotalRepairs) + '\n' + 'Flying now: {}'.format(self.IsFlying)
        return ret

    def TakeOff(self):
        if self.NeedsMaintenance:
            print('ERROR!: This plane cannot fly until it undergoes repairs.')
            self.IsFlying = False
        else:
            self.IsFlying = True

    def Land(self):
        if self.IsFlying:
            self.TripsSinceMaintenance += 1
            self.TotalTrips += 1
            if self.TripsSinceMaintenance >= 100:
                self.NeedsMaintenance = True
        self.IsFlying = False

    def Repair(self):
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0
        self.TotalRepairs += 1


def drive_car(car, trips):
    for trip in range(trips):
        car.Drive()
        car.Stop()
    return car


def fly_plane(plane, trips):
    for trip in range(trips):
        plane.TakeOff()

        if plane.IsFlying:
            plane.Land()
        else:
            print('Plane is going in for repairs')
            plane.Repair()
    return plane


def main():
    cars = [Cars('Subaru', 'Impreza', 2015, 2225),
            Cars('Lincoln', 'Cadillac', 2020, 3150),
            Cars('Jeep', 'Wrangler', 2004, 3675)
            ]

    car_trips = [52, 101, 236]

    for i in range(len(cars)):
        print('~~~~~~~~~~~~~~~~~~')
        print('INITIAL STATUS CAR #{}'.format(i + 1))
        print('~~~~~~~~~~~~~~~~~~')
        print(cars[i])
        print('~~~~~~~~~~~~~~~~~~')

        cars[i] = drive_car(cars[i], car_trips[i])
        print('STATUS CAR #{} AFTER {} TRIPS AND {} REPAIRS'.format(i + 1, cars[i].TotalTrips, cars[i].TotalRepairs))
        print('~~~~~~~~~~~~~~~~~~')
        print(cars[i])

        if i == 2:
            cars[i].Repair()
            cars[i] = drive_car(cars[i], 25)
            print('~~~~~~~~~~~~~~~~~~')
            print('STATUS CAR #{} AFTER {} TRIPS AND {} REPAIRS'.format(i + 1, cars[i].TotalTrips, cars[i].TotalRepairs))
            print('~~~~~~~~~~~~~~~~~~')
            print(cars[i])

        print()

    planes = [Planes('Boeing', '737', 2011, 125500),
              Planes('Lockheed Martin', 'F-16', 2019, 35750)
              ]

    plane_trips = [86, 223]

    for i in range(len(planes)):
        print('~~~~~~~~~~~~~~~~~~')
        print('INITIAL STATUS PLANE #{}'.format(i + 1))
        print('~~~~~~~~~~~~~~~~~~')
        print(planes[i])
        print('~~~~~~~~~~~~~~~~~~')

        planes[i] = fly_plane(planes[i], plane_trips[i])
        print('STATUS PLANE #{} AFTER {} TRIPS AND {} REPAIRS'.format(i + 1, planes[i].TotalTrips, planes[i].TotalRepairs))
        print('~~~~~~~~~~~~~~~~~~')
        print(planes[i])
        print()

main()