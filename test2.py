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
  'position': [data[0]['position']],
  'score': data[0]['score'],
}
for i in data:
  first_pos = str(var['position'][0:1])
  end_pos = (var['position'][-1:])
  new_position = f'{first_pos} - {end_pos}'
  if i['score'] == var['score']:
    var['position'].append(i['position'])
    index = data.index(i)
    data[index]['position'] = new_position
  else:
    # if var['position'] != '':
    var['score'] = i['score']
    var['position'] = ''
    var['position'] = [i['position']]
    print(new_position)
    data[index]['position'] = new_position
print(data)

# print(data[1+1]['score'])

# def last_index(index):
#   print(index)
#   if data[index + 1] and data[index]['score'] == data[index+1]['score']:
#     return last_index(index+1)
#   else:
#     return index

# def placement():
#   for i in range(len(data)):
#     last = last_index(i)
#     if i != last or i <= len(data):
#       start = str(data[i]['position'])
#       end = str(data[last]['position'])
#       while i != last+1:
#         data[i]['position'] = start + '-' + end


# def new_func():
#     i+=1
#       i-=1

# placement()
# print(data)


