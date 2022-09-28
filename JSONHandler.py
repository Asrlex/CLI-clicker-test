import json

file_data = None
def loadJSON():
  f = open("tasks.json")
  data = json.load(f)
  f.close()
  global file_data
  file_data = data
  return data
  