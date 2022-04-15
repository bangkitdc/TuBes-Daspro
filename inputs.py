import utility

# Validasi input
def input_valid(message, validation = lambda x : True, provision = '', lower = False, flagstop = '', type = ''):
	'''
		Mendapatkan validated input (jika tidak valid, loop pertanyaan hingga valid)
	
		Arguments:
			message(str)					: input message dari user
			validation(lambda, optional)	: lambda function untuk validasi input
			lower(bool, optional)			: boolean untuk lowercase input, default = False
			provision(str, optional)		: message yang ditampilkan (hint user untuk inputan valid)
			type(str, optional)				: membedakan inputan untuk password dan bukan

		Returns:
			str 	: return input yang sudah tervalidasi, stop saat input = flagstop

	'''
	if flagstop != '':
		message += f'[{flagstop} untuk membatalkan] '

	while True:
		if not (type == 'pass'):
			inp = utility.remove_space(input(message)) # strip.()
		else:
			inp = input(message)
		if lower:
			inp = inp.lower()
		if flagstop != '' and inp == flagstop:
			print('Aksi dibatalkan!')
			return flagstop
		elif inp == '':
			print('Input kosong!')
		elif validation(inp):
			return inp
		else:
			print(f'Input tidak valid. {provision}')

# Find idx key with target
def find_idx_key_with_target(data, key, target):
	'''
		Mencari index id dari target yang dicari

		Arguments:
			data(list)	: data yang diolah
			key(str)	: key yang dicari (list ke berapa)
			target(str)	: target yang dicari (dibandingkan)

		Returns:
			int 	: index id yang didapat
	'''
	for i in data:
		if i[key][1] == target:
			return i[0][1]
	return -1

# input yes or no
def input_yesorno(message, parse = True):
	'''
		Mendapat input dari yes or no question

		Arguments:
			message(str)	: pertanyaan yang akan ditampilkan

		Returns:
			str 	: 'y' if yes else {'n'} if no
	'''
	message += '(y/ n) '
	choices = ['y', 'n']
	inp = input_valid(message, validation = lambda x : x in choices)
	return (inp == 'y' if parse else False)

# filter name
def filter_name(name):
	'''
		Filter nama sesuai spesifikasi (terdiri dari alphabet saja)

		Arguments:
			name(str)	: nama yang akan diolah (elemen per elemen) 
	
		Returns:
			bool 	: jika elemen yang dicek pada string sesuai spesifikasi return True else False
	'''
	for i in name:
		if not ((ord('A') <= ord(i) <= ord('Z')) or (ord('a') <= ord(i) <= ord('z')) or (ord(i)) == 32):
			return False
	return True

# filter username
def filter_username(username):
	'''
		Filter usernama sesuai spesifikasi

		Arguments:
			username(str)	: usernama yang akan diolah (elemen per elemen) 
	
		Returns:
			bool 	: jika elemen yang dicek pada string sesuai spesifikasi return True else False
	'''
	for i in username:
		if not ((ord('A') <= ord(i) <= ord('Z')) or (ord('a') <= ord(i) <= ord('z')) or (i == '_') or (i == '-') or (ord('0') <= ord(i) <= ord('9'))):
			return False
	return True

# id generator
def id_generator(num):
	'''
		Generate format id sesuai spesifikasi

		Arguments:
			num(int)	: number yang akan digenerate to id
	
		Returns:
			str 	: hasil generated id menggunakan format
	'''
	if 1 <= num <= 9:
		return '00' + str(num)
	elif 10 <= num <= 99:
		return '0' + str(num)
	else:
		return str(num)

# filter input without seperation
def filter_sep(x):
	'''
		Filter input agar tidak mengandung ';' -> yang akan bermasalah bagi csv

		Arguments:
			x(str)	: string yang akan diolah (elemen per elemen)
	
		Returns:
			bool 	: jika elemen yang dicek pada string sesuai spesifikasi return True else False
	'''
	for i in x:
		if i == ';':
			return False
	return True

# Input numbers
def input_number(message, validation = lambda x : True, provision = '', parse = True, flagstop = ''):
	'''
		Mendapat inputan numbers

		Arguments:
			message(str)					: pertanyaan yang akan ditampilkan
			validation(lambda, optional)	: lambda function untuk validasi input
			provision(str, optional)		: message yang ditampilkan (hint user untuk inputan valid)

		Returns:
			str 	: return input yang sudah tervalidasi, stop saat input = flagstop
	'''
	inp = input_valid(message, validation = lambda x : is_number(x), provision = provision, flagstop = flagstop)
	return inp

def is_number(x):
	'''
		Filter input agar berupa numbers

		Arguments:
			x(str)	: string yang akan diolah (elemen per elemen)
	
		Returns:
			bool 	: jika elemen yang dicek pada string sesuai spesifikasi return True else False
	'''
	for i in x:
		if not (ord('0') <= ord(i) <= ord('9')):
			return False
	return True

def is_empty(x):
	'''
		Mengecek apakah string kosong atau tidak

		Arguments:
			x(str)	: string yang akan diolah (elemen per elemen)
	
		Returns:
			bool 	: jika elemen yang dicek pada string sesuai spesifikasi return True else False
	'''
	count = True
	for i in x:
		if i != '':
			count = False
	return count
