from translate import Translator
translator = Translator(to_lang='ja')

try:
  with open('translation.txt', mode='r') as myFile:
    text = myFile.read()
    translation = translator.translate(text)
    with open('translatedToJapanese.txt', mode='w') as myFile2:
      myFile2.write(translation)
except FileNotFoundError as err:
  print('File not found')
  raise err