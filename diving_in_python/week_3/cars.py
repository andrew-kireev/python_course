import os 
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
    
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_width = 0.0
        self.body_height = 0.0
        self.body_length = 0.0
        self.car_type = "truck"
        try:
            w, h, l = body_whl.split('x')
            self.body_length = float(w)
            self.body_width = float(h)
            self.body_height = float(l)
        except ValueError:
            self.body_length = float(0.0)
            self.body_width = float(0.0)
            self.body_height = float(0.0)
    
    def get_body_volume(self):
        V = self.body_length * self.body_width * self.body_height
        return V



class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra
    


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        try:
            reader = csv.reader(csv_fd, delimiter=';')
            print(reader)
            next(reader)
            for row in reader:
                if len(row) < 7:
                    continue
                if row[0] == 'car':
                    if row[1] == '' or row[2] == '' or row[3] == '' or row[5] == '':
                        pass
                    try:
                        car = Car(row[1], row[3], row[5], row[2])
                    except:
                        pass
                    car_list.append(car)
                elif row[0] == 'truck':
                    if row[1] == '' or row[4] == '' or row[3] == '' or row[5] == '':
                        pass
                    try:
                        truck = Truck(row[1], row[3], row[5], row[4])
                    except:
                        pass
                    car_list.append(truck)
                elif row[0] == 'spec_machine':
                    if row[1] == '' or row[6] == '' or row[3] == '' or row[5] == '':
                        pass
                    try:
                        speck = SpecMachine(row[1], row[3], row[5], row[6])
                    except:
                        pass
                    car_list.append(speck)
                else:
                    raise ValueError
        except:
                pass
        
    return car_list


# l = get_car_list('/Users/andrewkireev/Documents/python_course/new_test')
# for i in l:
#     print(i.car_type)
