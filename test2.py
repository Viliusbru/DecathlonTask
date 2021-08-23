data = [
  { "position": 1, "name": "Edan Daniele", "score": 4200 },
  { "position": 2, "name": "Coos Kwesi", "score": 3494 },
  { "position": 3, "name": "Lehi Poghos", "score": 3199 },
  { "position": 4, "name": "Severi Eileifr", "score": 3099 },
  { "position": 5, "name": "Cum", "score": 3099 }
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