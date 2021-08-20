import csv

objects = []
json_file = {}
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

    def final_score(self, name, score):
        self.name = name
        self.score = score

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
        fifteenhundred_meters = data_list[i][10]                                                            # converting to seconds
        fifteenhundred_meters_split = fifteenhundred_meters.split('.')
        fifteenhundred_meters_in_seconds = (int(fifteenhundred_meters_split[0]) * 60 + int(fifteenhundred_meters_split[1]))
        fifteenhundred_meters = str(fifteenhundred_meters_in_seconds) + '.' + fifteenhundred_meters_split[2]
        fifteenhundred_meters = float(fifteenhundred_meters)
        objects.append(Athlete(name, hundred_meters, long_jump, shot_put, high_jump, fourhundred_meters, hurdles, discus_throw, pole_vault, javelin_throw, fifteenhundred_meters)) 

read_csv(filename)


# print(objects[0].get_hundred_meters())


class Score_calculate():
    def hundred_meters(score):
        A = point_dict['hundred_meters'][0]
        B = point_dict['hundred_meters'][1]
        C = point_dict['hundred_meters'][2]
        points = (A * (B - float(score)) ** C)
        return(int(points))

    def long_jump(score):
        A = point_dict['long_jump'][0]
        B = point_dict['long_jump'][1]
        C = point_dict['long_jump'][2]
        points = (A * ((float(score) * 100) - B) ** C)
        return (int(points))

    def shot_put(score):
        A = point_dict['shot_put'][0]
        B = point_dict['shot_put'][1]
        C = point_dict['shot_put'][2]
        points = (A * (float(score) - B) ** C)
        return (int(points))

    def high_jump(score):
        A = point_dict['high_jump'][0]
        B = point_dict['high_jump'][1]
        C = point_dict['high_jump'][2]
        points = (A * (float(score) * 100 - B) ** C)
        return (int(points))

    def fourhundred_meters(score):
        A = point_dict['fourhundred_meters'][0]
        B = point_dict['fourhundred_meters'][1]
        C = point_dict['fourhundred_meters'][2]
        points = (A * (B - float(score)) ** C)
        return (int(points))

    def hurdles(score):
        A = point_dict['hurdles'][0]
        B = point_dict['hurdles'][1]
        C = point_dict['hurdles'][2]
        points = (A * (B - float(score)) ** C)
        return (int(points))

    def discus_throw(score):
        A = point_dict['discus_throw'][0]
        B = point_dict['discus_throw'][1]
        C = point_dict['discus_throw'][2]
        points = (A * (float(score) - B) ** C)
        return (int(points))

    def pole_vault(score):
        A = point_dict['pole_vault'][0]
        B = point_dict['pole_vault'][1]
        C = point_dict['pole_vault'][2]
        points = (A * ((float(score) * 100) - B) ** C)
        return (int(points))

    def javelin_throw(score):
        A = point_dict['javelin_throw'][0]
        B = point_dict['javelin_throw'][1]
        C = point_dict['javelin_throw'][2]
        points = (A * (float(score) - B) ** C)
        return (int(points))

    def fifteenhundred_meters(score):
        A = point_dict['fifteenhundred_meters'][0]
        B = point_dict['fifteenhundred_meters'][1]
        C = point_dict['fifteenhundred_meters'][2]
        points = (A * (B - float(score)) ** C)
        return (int(points))
    
for i in range(len(objects)):
    # print(objects[i].name)
    hundred_meters = Score_calculate.hundred_meters(objects[i].get_hundred_meters())
    long_jump = Score_calculate.long_jump(objects[i].get_long_jump())
    shot_put = Score_calculate.shot_put(objects[i].get_shot_put())
    high_jump = Score_calculate.high_jump(objects[i].get_high_jump())
    fourhundred_meters = Score_calculate.fourhundred_meters(objects[i].get_fourhundred_meters())
    hurdles = Score_calculate.hurdles(objects[i].get_hurdles())
    discus_throw = Score_calculate.discus_throw(objects[i].get_discus_throw())
    pole_vault = Score_calculate.pole_vault(objects[i].get_pole_vault())
    javelin_throw = Score_calculate.javelin_throw(objects[i].get_javelin_throw())
    fifteenhundred_meters = Score_calculate.fifteenhundred_meters(objects[i].get_fifteenhundred_meters())
    total_score = hundred_meters + long_jump + shot_put + high_jump + fourhundred_meters + hurdles + discus_throw + pole_vault + javelin_throw + fifteenhundred_meters
    # print(f'total_score: {total_score}')
    for j in range(len(objects)):
        json_file[objects[i].name] = total_score
        sort = sorted(json_file.items(), key=lambda x: x[1])
# print(json_file)



