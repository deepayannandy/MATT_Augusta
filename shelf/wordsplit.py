text = input('Enter a string')
first, *middle, last = text.split()
print(first, last)