with open('test.txt', mode='a') as myFile: # Standard way of opening a file. automatically closes file.
  text = myFile.write('hey it\'s me!')
  print(text)

with open('sad.txt', mode='w') as myFile: # Creates a new file called sad.txt and writes a :(
  sad = myFile.write(':(')
  print(text)