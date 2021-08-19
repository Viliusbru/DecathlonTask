import csv

objects = []
data_list = []

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

with open('data.csv', 'r',) as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        data_list.append(row)
    #     split_lines = data_list.split(",")
    # print(split_lines[0])

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


for object in objects:
    print(object.name)

