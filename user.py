import data
import inputs, utility
import hash

def register(data):
	flag = True
	while flag:
		reg_name = inputs.input_valid('Masukan nama: ', validation = lambda x : inputs.filter_name(x), provision = 'Nama hanya terdiri dari alphabet.', flagstop = '!x')
		if reg_name == '!x':
			return

		reg_name = reg_name.title() # Agar diawali dengan huruf kapital
		reg_username = inputs.input_valid('Masukan username: ', validation = lambda x : inputs.filter_username(x), provision = 'Username hanya terdiri dari A-Z, a-z, `_`, `-`, dan 0-9.')
		reg_password = inputs.input_valid('Masukan password (min. 10 karakter): ', validation = lambda x : utility.length(x) >= 10, provision = 'Password minimal 10 karakter.', type = 'pass')

		inp = inputs.input_yesorno('Apakah kamu yakin dengan data kamu? ')
		if not inp:
			print('Gagal mendaftarkan user.')
		else:
			flag = False

	if inputs.find_idx_key_with_target(data[0], 1, reg_username) == -1: # User tidak ditemukan
		data[0] += [
			['id', str(utility.length(data[0]) + 1)], 
			['username', reg_username], 
			['nama', reg_name], 
			['password', hash.encrypt(reg_password)],
			['role', 'user'],
			['saldo', '0']
		]
		print(f'Username {reg_username} telah berhasil register ke dalam "Binomo".')
	else:
		print(f'Username {reg_username} sudah terpakai, silakan menggunakan username lain.')

def login(data):
	while True:
		username = inputs.input_valid('Masukan username: ', flagstop = '!x')
		if username == '!x':
			return None
		password = inputs.input_valid('Masukan password: ')
		data_user = data[0] # user.csv
		user_id = inputs.find_idx_key_with_target(data_user, 1, username)
		if user_id != -1 and hash.encrypt(password) == data_user[int(user_id) - 1][3][1]: # password
			print(f'Halo {data_user[int(user_id) - 1][2][1]}! Selamat datang di "Binomo".')
			return data_user[int(user_id) - 1] # id
		else:
			print('Password atau username salah atau tidak ditemukan.')
