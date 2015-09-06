my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

#NOTE!!! There is a bug in this. You need to go to the actual text file and make changes then delete changes else will not work. Error on Codecademy side