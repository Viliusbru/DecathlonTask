import csv, json
from operator import itemgetter

res = []
objects = []
json_file = {}
data_list = []
sorted_json_file = []
POINT_DICT = {
    "hundred_meters": [25.4347, 18, 1.81],
    "long_jump": [0.14354, 220, 1.4],
    "shot_put": [51.39, 1.5, 1.05],
    "high_jump": [0.8465, 75, 1.42],
    "fourhundred_meters": [1.53775, 82, 1.81],
    "hurdles": [5.74352, 28.5, 1.92],
    "discus_throw": [12.91, 4, 1.1],
    "pole_vault": [0.2797, 100, 1.35],
    "javelin_throw": [10.14, 7, 1.08],
    "fifteenhundred_meters": [0.03768, 480, 1.85],
}


class Athlete:
    def __init__(
        self,
        name,
        hundred_meters,
        long_jump,
        shot_put,
        high_jump,
        fourhundred_meters,
        hurdles,
        discus_throw,
        pole_vault,
        javelin_throw,
        fifteenhundred_meters,
    ):
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
        return (
            self.name,
            self.hundred_meters,
            self.long_jump,
            self.shot_put,
            self.high_jump,
            self.fourhundred_meters,
            self.hurdles,
            self.discus_throw,
            self.pole_vault,
            self.javelin_throw,
            self.fifteenhundred_meters,
        )


def read_csv(filename):
    with open(
        filename,
        "r",
    ) as f:
        reader = csv.reader(f, delimiter=";")
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
        fifteenhundred_meters = data_list[i][10]  # converting to seconds
        fifteenhundred_meters_split = fifteenhundred_meters.split(".")
        fifteenhundred_meters_in_seconds = int(
            fifteenhundred_meters_split[0]
        ) * 60 + int(fifteenhundred_meters_split[1])
        fifteenhundred_meters = (
            str(fifteenhundred_meters_in_seconds) + "." + fifteenhundred_meters_split[2]
        )
        fifteenhundred_meters = float(fifteenhundred_meters)
        objects.append(
            Athlete(
                name,
                hundred_meters,
                long_jump,
                shot_put,
                high_jump,
                fourhundred_meters,
                hurdles,
                discus_throw,
                pole_vault,
                javelin_throw,
                fifteenhundred_meters,
            )
        )


class FinalClass:
    def __init__(self, position, name, score):
        self.position = position
        self.name = name
        self.score = score


class Score_calculate:
    def hundred_meters(score):
        A = POINT_DICT["hundred_meters"][0]
        B = POINT_DICT["hundred_meters"][1]
        C = POINT_DICT["hundred_meters"][2]
        points = A * (B - float(score)) ** C
        return int(points)

    def long_jump(score):
        A = POINT_DICT["long_jump"][0]
        B = POINT_DICT["long_jump"][1]
        C = POINT_DICT["long_jump"][2]
        points = A * ((float(score) * 100) - B) ** C
        return int(points)

    def shot_put(score):
        A = POINT_DICT["shot_put"][0]
        B = POINT_DICT["shot_put"][1]
        C = POINT_DICT["shot_put"][2]
        points = A * (float(score) - B) ** C
        return int(points)

    def high_jump(score):
        A = POINT_DICT["high_jump"][0]
        B = POINT_DICT["high_jump"][1]
        C = POINT_DICT["high_jump"][2]
        points = A * (float(score) * 100 - B) ** C
        return int(points)

    def fourhundred_meters(score):
        A = POINT_DICT["fourhundred_meters"][0]
        B = POINT_DICT["fourhundred_meters"][1]
        C = POINT_DICT["fourhundred_meters"][2]
        points = A * (B - float(score)) ** C
        return int(points)

    def hurdles(score):
        A = POINT_DICT["hurdles"][0]
        B = POINT_DICT["hurdles"][1]
        C = POINT_DICT["hurdles"][2]
        points = A * (B - float(score)) ** C
        return int(points)

    def discus_throw(score):
        A = POINT_DICT["discus_throw"][0]
        B = POINT_DICT["discus_throw"][1]
        C = POINT_DICT["discus_throw"][2]
        points = A * (float(score) - B) ** C
        return int(points)

    def pole_vault(score):
        A = POINT_DICT["pole_vault"][0]
        B = POINT_DICT["pole_vault"][1]
        C = POINT_DICT["pole_vault"][2]
        points = A * ((float(score) * 100) - B) ** C
        return int(points)

    def javelin_throw(score):
        A = POINT_DICT["javelin_throw"][0]
        B = POINT_DICT["javelin_throw"][1]
        C = POINT_DICT["javelin_throw"][2]
        points = A * (float(score) - B) ** C
        return int(points)

    def fifteenhundred_meters(score):
        A = POINT_DICT["fifteenhundred_meters"][0]
        B = POINT_DICT["fifteenhundred_meters"][1]
        C = POINT_DICT["fifteenhundred_meters"][2]
        points = A * (B - float(score)) ** C
        return int(points)


def sort():
    for i in range(len(objects)):
        hundred_meters = Score_calculate.hundred_meters(objects[i].get_hundred_meters())
        long_jump = Score_calculate.long_jump(objects[i].get_long_jump())
        shot_put = Score_calculate.shot_put(objects[i].get_shot_put())
        high_jump = Score_calculate.high_jump(objects[i].get_high_jump())
        fourhundred_meters = Score_calculate.fourhundred_meters(
            objects[i].get_fourhundred_meters()
        )
        hurdles = Score_calculate.hurdles(objects[i].get_hurdles())
        discus_throw = Score_calculate.discus_throw(objects[i].get_discus_throw())
        pole_vault = Score_calculate.pole_vault(objects[i].get_pole_vault())
        javelin_throw = Score_calculate.javelin_throw(objects[i].get_javelin_throw())
        fifteenhundred_meters = Score_calculate.fifteenhundred_meters(
            objects[i].get_fifteenhundred_meters()
        )
        total_score = (
            hundred_meters
            + long_jump
            + shot_put
            + high_jump
            + fourhundred_meters
            + hurdles
            + discus_throw
            + pole_vault
            + javelin_throw
            + fifteenhundred_meters
        )
        json_file[objects[i].name] = total_score
    sorted_json_file = sorted(json_file.items(), key=itemgetter(1), reverse=True)
    # print(sorted_json_file)

    position_counter = 1
    for i in sorted_json_file:
        # print(i)
        res.append(FinalClass(position_counter, i[0], i[1]))
        position_counter += 1

    # FIXING THE POSITIONS
def else_func(placeholder):
            for j in range(placeholder['start'], placeholder['end'] + 1):
                if placeholder['start'] == placeholder['end']:
                    placeholder['start'] += 1
                    res[j].position = str(placeholder['start'])
                else:
                    new_position = f"{placeholder['start'] + 1}-{placeholder['end'] + 1}"
                    res[j].position = new_position
            placeholder['end'] += 1
            placeholder['start'] = placeholder['end']

def fix_positions():
    placeholder = {
        'start':    0,
        'end':      -1,
        "score":    res[0].score,
    }
    for i in res:
        if i.score == placeholder['score']:
            placeholder['end'] += 1
        else:
            placeholder['score'] = i.score
            else_func(placeholder)
    placeholder['score'] = i.score
    else_func(placeholder)
        



def create_download_file():
    with open("output.json", "w", encoding="utf-8") as f:
        json_string = json.dumps([ob.__dict__ for ob in res])
        f.write(json_string)
        res.clear()
