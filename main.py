import os

#to do:
#	- inputu in fisiere:
#		- poze
#	- sa poata sa aleaga ce fel de file face(.txt etc)


def create_files():
	for i in range(nr_files):
		with open(f'{file_name}_'f'{i+1}', 'w') as fp:
			pass

def input_files(diss):

	def input_stext():
		text = input('What do you want to insert (in all the files): ')
		for i in range(nr_files):
			with open(f'{file_name}_'f'{i + 1}', 'a') as f:
				f.write(text)
				f.write(' ')

	def input_dtext():
		for i in range(nr_files):
			with open(f'{file_name}_'f'{i + 1}', 'a') as f:
				f.write(input(f"In file nr {i + 1}: "))
				f.write(' ')

	def input_cnumbers():
		nr = int(input('numarul de la care incepe: '))
		x = int(input('din cat in cat: '))
		for i in range(nr_files):
			y = nr + i * x
			with open(f'{file_name}_'f'{i + 1}', 'a') as f:
				f.write(f'{y}')
				f.write(' ')

	def input_dnumbers():
		nr = int(input('numarul de la care incepe: '))
		x = int(input('din cat in cat: '))
		for i in range(nr_files):
			y = nr - i * x
			with open(f'{file_name}_'f'{i + 1}', 'a') as f:
				f.write(f'{y}')
				f.write(' ')

	def input_fotos():
		print('work in progres')
	# work in progress ^

	def input_space():
		for i in range(nr_files):
			with open(f'{file_name}_'f'{i + 1}', 'a') as f:
				f.write(' ')

	def input_endl():
		for i in range(nr_files):
			with open(f'{file_name}_'f'{i + 1}', 'a') as f:
				f.write('\n')

	def adauga_in_bd():
		nume = input('what are you saving(the name): ')
		with open(f'{nume}', 'a') as f:
			f.write(input('the first line: '))
			opt = input('do you want to add more lines: ')
			while opt.lower() == 'yes':
				f.write('\n')
				f.write(input('the next line: '))
				opt = input('do you want to add more lines: ')
			f.write(' ')

	def input_bd():
		opt = input('what do you want to add from your saved text(the name): ')
		for line in open(opt):
			for i in range(nr_files):
				with open(f'{file_name}_'f'{i + 1}', 'a') as f:
					f.write(line)

	if diss:
		print('After any text or number insert it automaticly puts space(" ") in your files!')
		print('The space obtion for below is in case that you want an extra space(" ") caracter!')
		print("The program can't insert in one go text that spreads on 2 lines! ")
		print('\n'*2)
		print('If you want to insert insert the SAME TEXT in all your files, write "same text"! ')
		print('If you want to insert insert the DIFFERENT TEXT in your files, write "different text"! ')
		print('If you want to insert insert INCREASING NUMBERS in your files, write "increasing numbers"! ')
		print('If you want to insert insert DESCENDING NUMBERS in your files, write "descending numbers"! ')
		print('If you want to insert insert SPACE(" ") in your files, write "space"! ')
		print('If you want to start a NEW LINE, write "new line" ')
		print('If you want to insert insert something SAVED in your files, write "saved" ')
		print('If you want to ADD something to your saved files, write "add" ')
		print("If you don't remember the options, write 'help' ")
		print('Inserting photos coming soon! ')
		diss = 0

	opt = input('I want to insert: ')
	if opt.lower() == 'help':
		print('After any text or number insert it automaticly puts space(" ") in your files!')
		print('The space obtion for below is in case that you want an extra space(" ") caracter!')
		print("The program can't insert in one go text that spreads on 2 lines! ")
		print('\n' * 2)
		print('If you want to insert insert the SAME TEXT in all your files, write "same text"! ')
		print('If you want to insert insert the DIFFERENT TEXT in your files, write "different text"! ')
		print('If you want to insert insert INCREASING NUMBERS in your files, write "increasing numbers"! ')
		print('If you want to insert insert DESCENDING NUMBERS in your files, write "descending numbers"! ')
		print('If you want to insert insert SPACE(" ") in your files, write "space"! ')
		print('If you want to start a NEW LINE, write "new line" ')
		print('If you want to insert insert something SAVED in your files, write "saved" ')
		print('If you want to ADD something to your saved files, write "add" ')
		print("If you don't remember the options, write 'help' ")
		print('Inserting photos coming soon! ')
	elif opt.lower() in ['same text', 's text']:
		input_stext()
	elif opt.lower() in ['different text','d text']:
		input_dtext()
	elif opt.lower() in ['increasing numbers','nr c']:
		input_cnumbers()
	elif opt.lower() in ['descending numbers','nr d']:
		input_dnumbers()
	elif opt.lower() == 'fotos':
		input_fotos()
	elif opt.lower()  in ['space',' ']:
		input_space()
	elif opt.lower() in ['newline','new line','line']:
		input_endl()
	elif opt.lower() in ['save','add']:
		adauga_in_bd()
	elif opt.lower() in ['saved','data base','database','db']:
		input_bd()
	else:
		print('comanda introdusa gresit! ')
		input_files(diss)
	print('\n'*2)

	opt = input("Do you want to insert anything else(yes or no): ")
	if opt.lower() in ['da', 'yes']:
		input_files(diss)

def move_files():
	path = input('What is the location you want the file/fiels in: ')
	path = "C:/Users/vladv/OneDrive/Desktop/test"
	for i in range(nr_files):
		x = f'{pathp}\{file_name}_{i+1}'
		y = f'{path}/'f'{file_name}_'f'{i+1}'
		os.rename(f'{x}',f'{y}')

def find_path():
	x = os.path.abspath('P acte py')
	l = len('\P acte py')
	y = len(x) - l
	return x[:y]

pathp = find_path()
file_name = input("The name of the files/file u want 2 create: ")
nr_files = int(input('How many files u want 2 create: '))
create_files()
print('\n'*2)

input_files(1)
move_files()

#                         CODE MADE BY SERPE VLAD
#	This code creates files, let's you input in them, and then moves them in a locsation of your choice!
#	You may use it if you need it but please don't delete the credits!