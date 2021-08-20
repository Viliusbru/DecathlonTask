import json
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
A = point_dict['hundred_meters'][1]
print(A)

test = '5.25.72'

minutes = test.split('.')
counted = (int(minutes[0]) * 60 + int(minutes[1]))
print(counted)
final = str(counted) + '.' + minutes[2]
print(float(final))

def fifteenhundred_meters(score):
    A = point_dict['fifteenhundred_meters'][0]
    B = point_dict['fifteenhundred_meters'][1]
    C = point_dict['fifteenhundred_meters'][2]
    points = (A * (B - float(score)) ** C)
    print(int(points))

fifteenhundred_meters(float(final))

# JSON

athletes = {
    'name1': 'score1',
    'name2': 'score2',
    'name3': 'score3',
}
with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(athletes, f)