import utility

# Validasi input
def input_valid(message, validation = lambda x : True, provision = '', lower = False, flagstop = '', type = ''):
	if flagstop != '':
		message += f'[{flagstop} untuk membatalkan] '

	while True:
		if not (type == 'pass'):
			inp = utility.remove_space(input(message))
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
	for i in data:
		if i[key][1] == target:
			return i[0][1]
	return -1

# input yes or no
def input_yesorno(message, parse = True):
	message += '(y/ n) '
	choices = ['y', 'n']
	inp = input_valid(message, validation = lambda x : x in choices)
	return (inp == 'y' if parse else False)

# filter name
def filter_name(name):
	for i in name:
		if not ((ord('A') <= ord(i) <= ord('Z')) or (ord('a') <= ord(i) <= ord('z')) or (ord(i)) == 32):
			return False
	return True

# filter username
def filter_username(username):
	for i in username:
		if not ((ord('A') <= ord(i) <= ord('Z')) or (ord('a') <= ord(i) <= ord('z')) or (i == '_') or (i == '-') or (ord('0') <= ord(i) <= ord('9'))):
			return False
	return True

# id generator
def id_generator(num):
    if 1 <= num <= 9:
        return '00' + str(num)
    elif 10 <= num <= 99:
        return '0' + str(num)
    else:
        return str(num)

# filter input without seperation
def filter_sep(x):
	for i in x:
		if i == ';':
			return False
	return True

# Input numbers
def input_number(message, validation = lambda x : True, provision = '', parse = True, flagstop = ''):
	inp = input_valid(message, validation = lambda x : is_number(x), provision = provision, flagstop = flagstop)
	return inp

def is_number(x):
	for i in x:
		if not (ord('0') <= ord(i) <= ord('9')):
			return False
	return True

def is_empty(x):
	"""Return True jika array kosong"""
	count = True
	for i in x:
		if i != '':
			count = False
	return count
