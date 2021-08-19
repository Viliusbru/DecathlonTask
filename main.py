import csv

objects = []
data_list = []
filename = 'data.csv'

point_dict = {
    'hundred_meters':           [25.4347, 18, 1.81],
    'long_jump':                [0.14354, 220, 1.4],
    'shot_put':                 [51.39, 1.5, 1.05],
    'high_jump':                [0.8465, 75, 1.42],
    'fourhundred_meters':       [1.53775, 82, 1.81],
    'hurdles':                  [5.74352, 28.5, 1.92],
    'discus_throw':             [12.91, 4, 1.1],
    'pole_vault':               [0.2797, 100, 1.35],
    'javelin_throw':            [10.14, 7, 1.08],
    'fifteenhundred_meters':    [0.03768, 480, 1.85],
}

class Athlete:
    def __init__(self, name, hundred_meters, long_jump, shot_put, high_jump, fourhundred_meters, hurdles, discus_throw, pole_vault, javelin_throw, fifteenhundred_meters):
        self.name = name
        self.hundred_meters = hundred_meters
        self.long_jump = long_jump
        self.shot_put = shot_put
        self.high_jump = high_jump
        self.fourhundred_meters = fourhundred_meters
        self.hurdles = hurdles
        self.discus_throw = discus_throw
        self.pole_vault = pole_vault
        self.javelin_throw = javelin_throw
        self.fifteenhundred_meters = fifteenhundred_meters

    def get_name(self):
        return self.name

    def get_hundred_meters(self):
        return self.hundred_meters

    def get_long_jump(self):
        return self.long_jump
        
    def get_shot_put(self):
        return self.shot_put

    def get_high_jump(self):
        return self.high_jump

    def get_fourhundred_meters(self):
        return self.fourhundred_meters

    def get_hurdles(self):
        return self.hurdles

    def get_discus_throw(self):
        return self.discus_throw

    def get_pole_vault(self):
        return self.pole_vault

    def get_javelin_throw(self):
        return self.javelin_throw

    def get_fifteenhundred_meters(self):
        return self.fifteenhundred_meters

    def get_all(self):
        return self.name, self.hundred_meters, self.long_jump, self.shot_put, self.high_jump, self.fourhundred_meters, self.hurdles, self.discus_throw, self.pole_vault, self.javelin_throw, self.fifteenhundred_meters
        

def read_csv(filename):
    with open(filename, 'r',) as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            data_list.append(row)

    for i in range(len(data_list)):
        name = data_list[i][0]
        hundred_meters = data_list[i][1]
        long_jump = data_list[i][2]
        shot_put = data_list[i][3]
        high_jump = data_list[i][4]
        fourhundred_meters = data_list[i][5]
        hurdles = data_list[i][6]
        discus_throw = data_list[i][7]
        pole_vault = data_list[i][8]
        javelin_throw = data_list[i][9]
        fifteenhundred_meters = data_list[i][10]
        objects.append(Athlete(name, hundred_meters, long_jump, shot_put, high_jump, fourhundred_meters, hurdles, discus_throw, pole_vault, javelin_throw, fifteenhundred_meters)) 

read_csv(filename)


print(objects[0].get_hundred_meters())


class Score_calculate():
    def hundred_meters(score):
        for k, v in point_dict.items():
            if k == 'hundred_meters':
                points = (v[0] * (v[1] - float(score)) ** v[2])
                print(int(points))

    def long_jump(score):
        for k, v in point_dict.items():
            if k == 'long_jump':
                points = (v[0] * ((float(score) * 100) - v[1]) ** v[2])
                print(int(points))



    def shot_put(score):
        for k, v in point_dict.items():
            if k == 'shot_put':
                points = (v[0] * (float(score) - v[1]) ** v[2])
                print(round(points))



    def high_jump(score):
        for k, v in point_dict.items():
            if k == 'high_jump':
                points = (v[0] * ((float(score) * 100) - v[1]) ** v[2])
                print(int(points))



    def fourhundred_meters(score):
        for k, v in point_dict.items():
            if k == 'fourhundred_meters':
                points = (v[0] * (v[1] - float(score)) ** v[2])
                print(int(points))

    def hurdles(score):
        for k, v in point_dict.items():
            if k == 'hurdles':
                points = (v[0] * (v[1] - float(score)) ** v[2])
                print(int(points))

    def discus_throw(score):
        for k, v in point_dict.items():
            if k == 'discus_throw':
                points = (v[0] * (float(score) - v[1]) ** v[2])
                print(int(points))

    def pole_vault(score):
        for k, v in point_dict.items():
            if k == 'pole_vault':
                points = (v[0] * ((float(score) * 100) - v[1]) ** v[2])
                print(int(points))

    def javelin_throw(score):
        for k, v in point_dict.items():
            if k == 'javelin_throw':
                points = (v[0] * (float(score) - v[1]) ** v[2])
                print(int(points))

    def fifteenhundred_meters(score):
        for k, v in point_dict.items():
            if k == 'fifteenhundred_meters':
                points = (v[0] * (v[1] - float(score)) ** v[2])
                print(int(points))

Score_calculate.hundred_meters(objects[0].get_hundred_meters())

print(objects[0].get_long_jump())
Score_calculate.long_jump(objects[0].get_long_jump())

print(objects[0].get_shot_put())
Score_calculate.shot_put(objects[0].get_shot_put())

print(objects[0].get_high_jump())
Score_calculate.high_jump(objects[0].get_high_jump())

print(objects[0].get_fourhundred_meters())
Score_calculate.fourhundred_meters(objects[0].get_fourhundred_meters())

print(objects[0].get_hurdles())
Score_calculate.hurdles(objects[0].get_hurdles())

print(objects[0].get_discus_throw())
Score_calculate.discus_throw(objects[0].get_discus_throw())

print(objects[0].get_pole_vault())
Score_calculate.pole_vault(objects[0].get_pole_vault())

print(objects[0].get_javelin_throw())
Score_calculate.javelin_throw(objects[0].get_javelin_throw())

print(objects[0].get_fifteenhundred_meters())
Score_calculate.fifteenhundred_meters(objects[0].get_fifteenhundred_meters())



