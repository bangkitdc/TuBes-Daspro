import inputs, sys, data

F02 = 'register' #admin
F03 = 'login' #user and admin
F04 = 'tambah_game' #admin
F05 = 'ubah_game' #admin
F06 = 'ubah_stok' #admin
F07 = 'list_game_toko' #user and admin
F08 = 'buy_game' #user
F09 = 'list_game' #user
F10 = 'search_my_game' #user
F11 = 'search_game_at_store' #user and admin
F12 = 'topup' #admin
F13 = 'riwayat' #user
F14 = 'help' #user and admin
F16 = 'save' #user and admin
F17 = 'exit' #user and admin

def help(role):
	print(F03, F14, F17, sep = '\n')
	if role != '':
		print(F07, F11, F16, sep = '\n')
		if role == 'admin':
			print(F02, F04, F05, F06, F12, sep = '\n')
		elif role == 'user':
			print(F08, F09, F10, F13, sep = '\n')

def exit(d):
	if inputs.input_yesorno('Apakah kamu ingin menyimpan data sebelum keluar? '):
		data.save_data(d)
	print('Terima kasih! Jangan lupa mampir lagi xixixi ＼ʕ •ᴥ•ʔ／')
	sys.exit()
