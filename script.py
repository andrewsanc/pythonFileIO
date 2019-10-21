try:
  with open('text.txt', mode='w') as myFile:
    print(myFile.readlines())
except FileNotFoundError as err:
  print('file doesn\'t exist')
  raise err
except IOError as err:
  print('IO Error')
  raise err