import os

for filename in os.listdir('C:\\Users\MONIKA\\Desktop\\ProgrammingInPython\\praca_z_plikami'):
	if filename.endswith(".jpg"): 
		prefix = filename.split(".jpg")[0]
		os.rename(filename, prefix+".png")
		continue
	else:
		continue


