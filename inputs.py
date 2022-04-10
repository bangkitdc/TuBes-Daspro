import utility

# Validasi input
def input_valid(message, validation = lambda x : True, provision = '', lower = False, flagstop = ''):
	if flagstop != '':
		message += f'[{flagstop} untuk membatalkan] '

	while True:
		inp = utility.remove_space(input(message))
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

# Input yes or no
def input_yesorno(message, parse = True):
	message += '(y/ n) '
	choices = ['y', 'n']
	inp = input_valid(message, validation = lambda x : x in choices)
	return (inp == 'y' if parse else False)
