from PyDictionary import PyDictionary

dictionary=PyDictionary()


text = input('how can i help you? \n')
first, *middle, last = text.split()

a=dictionary.synonym(str(last))
print (str(a))