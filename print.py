x = 'spam'
y = 99
z = ['eggs']

print(x,y,z, sep=',',end='\n\t')

sourceFile = open('python.txt', 'w')
print('Круто же, правда?', file = sourceFile)
sourceFile.close()