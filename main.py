import argparse, time
import bmo
import inputs, user, data, game, command, utility, tictactoe, kerangajaib

ERROR_MESSAGE = 'Perintah tidak valid, periksa kembali perintah atau izin role kamu (atau ketik `help` untuk melihat daftar perintah ʕ ᵔᴥᵔ ʔ)'

def main():
	# Setup parser
	parser = argparse.ArgumentParser(description = 'BNMO Robot Pereda Stres')
	parser.add_argument('nama_folder', metavar = 'nama_folder', type = str, help = 'Nama folder berisi data eksternal.')
	args = parser.parse_args()
	# Interface
	print('Loading...')
	for i in ('...'):
		print(i)
		time.sleep(1)
	bmo.interface()
	# Load data dalam folder 'nama_folder'
	d = data.load_data(args.nama_folder)
	dUser = [['id', '-1'], ['username', ''], ['nama', ''], ['password', ''], ['role', ''], ['saldo', '']]
	print('Selamat datang di "BNMO"!!!')
	print('Ketik perintah kamu atau ketik `help` untuk melihat list perintah ʕ •ᴥ•ʔ')

	# Program berjalan
	while True:
		print()
		header = '>>> '
		if dUser[4][1] == 'admin':
			header = f'Admin ({dUser[1][1]}) {header}'
		elif dUser[4][1] == 'user':
			header = f'User ({dUser[1][1]}) {header}'
		else:
			header = f'Guest {header}'

		inp = inputs.input_valid(header, lower = True)
		
		# Cek input
		if inp == 'debug':
			print(d)
		elif inp == 'login':
			u = user.login(d)
			if u != None:
				dUser = u
		elif inp == 'help':
			command.help(dUser[4][1])
		elif inp == 'exit':
			command.exit(d)
		elif dUser[4][1] != '':
			if inp == 'save':
				data.save_data(d)
			elif inp == 'list_game_toko':
				break
			elif inp == 'search_game_at_store':
				break
			elif dUser[4][1] == 'admin':
				if inp == 'register':
					user.register(d)
				elif inp == 'tambah_game':
					game.tambah_game(d)
				elif inp == 'ubah_game':
					game.ubah_game(d)
				elif inp == 'ubah_stok':
					game.ubah_stok(d)
				elif inp == 'topup':
					game.topup(d[0])
				else:
					print(ERROR_MESSAGE)
			elif dUser[4][1] == 'user':
				if inp == 'buy_game':
					game.buy_game(dUser[0][1], d)
				elif inp == 'list_game':
					game.list_game(dUser[0][1], d)
				elif inp == 'search_my_game':
					break
				elif inp == 'riwayat':
					break
				else:
					print(ERROR_MESSAGE)
		elif inp == 'tictactoe':
			tictactoe.start()
		elif inp == 'kerangajaib':
			kerangajaib.start()
		else:
			print(ERROR_MESSAGE)

if __name__ == '__main__':
	main()
