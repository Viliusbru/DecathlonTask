data = [
  { "position": 1, "name": "Edan Daniele", "score": 4200 },
<<<<<<< HEAD
  { "position": 2, "name": "Edan Daasdasdniele", "score": 4200 },
  { "position": 3, "name": "Edadsdasdan Daniele", "score": 4200 },
  { "position": 4, "name": "Edadasdasdn Daniele", "score": 4200 },
  { "position": 5, "name": "Coos Kwesi", "score": 3494 },
  { "position": 6, "name": "Coos Kasdasdwesi", "score": 3494 },
  { "position": 7, "name": "Coosasdasd Kwesi", "score": 3494 },
  { "position": 8, "name": "Lehi Poghos", "score": 3199 },
  { "position": 9, "name": "Leasdasdhi Poghos", "score": 3199 },
  { "position": 10, "name": "Lehasdasdi Poghos", "score": 3199 },
  { "position": 11, "name": "Severi Eileifr", "score": 3099 },
  { "position": 12, "name": "Seasdasdveri Eileifr", "score": 3099 },
  { "position": 13, "name": "Severi asdasdasdEileifr", "score": 3098 }
]


var = {
  'position': [],
  'score': '',
}

for i in data:
  if i['score'] == var['score']:
    var['position'].append(i['position'])
    index = data.index(i)
    data[index]['position'] = new_position
  else:
    first_pos = str(var['position'][0:1])
    end_pos = (var['position'][-1])
    # if var['position'] != '':
    new_position = f'{first_pos} - {end_pos +1}'
    print(new_position)
    var['score'] = i['score']
    var['position'] = ''
    var['position'] = [i['position']]

=======
  { "position": 2, "name": "Coos Kwesi", "score": 3494 },
  { "position": 3, "name": "Lehi Poghos", "score": 3199 },
  { "position": 4, "name": "Severi Eileifr", "score": 3099 },
  { "position": 4, "name": "Severi Eileifr2", "score": 3099 },
]

# for index, elem in enumerate(range(len(data))):
#     if (index+1 < len(data) and index - 1 >= 0):
#         prev_value = data[index-1]['score']
#         value = data[index]['score']
#         next_value = data[index+1]['score']
#         print(prev_value, value, next_value)



class Klass():
  def create_obj(self, name):
    self.name = name

obj1 = Klass.create_obj('Kevin')
print(obj1.name)
>>>>>>> testing
