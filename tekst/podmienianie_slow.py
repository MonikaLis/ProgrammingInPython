import os

for filename in os.listdir('C:\\Users\MONIKA\\Desktop\\ProgrammingInPython\\tekst'):
	if filename.endswith('.txt'): 
		infile = filename
		prefix = filename.split(".txt")[0]
		outfile = prefix + '_swapped_words.txt'
		delete_dictionary = {'and': 'or', 'never': 'always', 'why': 'what'}
		with open(infile) as fin, open(outfile, 'w+') as fout:
			for line in fin:
				for word in delete_list:
						line = line.replace(word, '')
						continue
			
				fout.write(line)