data = [
  { "position": 1, "name": "Edan Daasdasdniele", "score": 4200 },
  { "position": 2, "name": "Edadsdasdan Daniele", "score": 4200 },
  { "position": 3, "name": "Edadasdasdn Daniele", "score": 4200 },
  { "position": 4, "name": "Coos Kwesi", "score": 3494 },
  { "position": 5, "name": "Coos Kasdasdwesi", "score": 3494 },
  { "position": 6, "name": "Coosasdasd Kwesi", "score": 3494 },
  { "position": 7, "name": "Lehi Poghos", "score": 3199 },
  { "position": 8, "name": "Leasdasdhi Poghos", "score": 3199 },
  { "position": 9, "name": "Lehasdasdi Poghos", "score": 3199 },
  { "position": 10, "name": "Severi Eileifr", "score": 3099 },
  { "position": 11, "name": "Seasdasdveri Eileifr", "score": 3099 },
  { "position": 12, "name": "Severi asdasdasdEileifr", "score": 3098 }
]

var = {
  'position': [],
  'score': '',
}

for i in data:
  if i['score'] == var['score']:
    var['position'].append(i['position'])
  else:
    new_position = str(var["position"][0:1]) + ' - ' + str(var["position"][-1:])
    print(new_position)
    var['score'] = i['score']
    var['position'].clear()
    var['position'] = [i['position']]

# print(data)