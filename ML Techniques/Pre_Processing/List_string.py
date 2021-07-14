'''
		Program to write customized index values for the dataframe in training set in ML related problems.

'''


i = 0

Index = list()

for i in range (10):
  index = str('Row') + str(i)
  print(index)
  Index.append(index)
print(type(Index))