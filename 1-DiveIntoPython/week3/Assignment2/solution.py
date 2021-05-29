#car_type;brand;passenger_seats_count;photo_file_name;body_whl;carrying;extra

import os
import csv
photo_ext = []
class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__('car', brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

    @classmethod
    def to_car(cls, row):
        try:
            float(row[5])
            int(row[2])
            return Car(row[1], row[3], float(row[5]), row[2])
        except Exception:
            return None

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__('truck', brand, photo_file_name, carrying)
        whl = body_whl.split('x')
        self.body_length, self.body_width , self.body_height = self._valid_whl(body_whl)
    
    @staticmethod
    def _valid_whl(whl):
        whl = whl.split('x')
        try:
            if len(whl) != 3:
                raise TypeError

            l = float(whl[0])
            w = float(whl[1])
            h = float(whl[2])
            return [l, w, h]
        except:
            return [0.0, 0.0, 0.0]

    @classmethod
    def to_truck(cls, row):
        try:
            float(row[5])
            return Truck(row[1], row[3], row[5],row[4])
        except Exception:
            return None

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width
            
class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__('spec_machine', brand , photo_file_name, carrying)
        self.extra = extra

    @classmethod
    def to_speec_machine(cls, row):
        try:
            float(row[5])
            if not row[6]:
                raise ValueError
            return SpecMachine(row[1], row[3],row[5], row[6])
        except Exception:
            return None
    

def valid_row(row):
    if len(row) < 7:
        return False
    if os.path.splitext(row[3])[1] not in [".jpg", ".jpeg", ".png", ".gif"]:
        return False
    if not row[1] or not row[3] or not row[5]:
        return False
    return True
    

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if not valid_row(row):
                continue
            if row[0] == 'car':
                car = Car.to_car(row)
                if  car:
                    car_list.append(car) 
            
            elif row[0] == 'truck':
                truck = Truck.to_truck(row)
                if truck:
                    car_list.append(truck)

            elif row[0] == 'spec_machine':
                spec_machine = SpecMachine.to_speec_machine(row)
                if spec_machine:
                    car_list.append(spec_machine)
            else:
                continue
    return car_list