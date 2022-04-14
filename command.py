import inputs, sys, data
from utility import length

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
	print('1  || ' + F03 + ' ' * (20 - length(F03)) + ' || Untuk melakukan login ke dalam sistem', 
    '2  || ' + F14 + ' ' * (20 - length(F14)) + ' || Untuk melihat panduan penggunaan sistem', 
    '3  || ' + F17 + ' ' * (20 - length(F17)) + ' || Untuk keluar dari aplikasi', sep = '\n')
	if role != '':
		print('4  || ' + F07 + ' ' * (20 - length(F07)) + ' || Untuk melihat daftar game yang tersedia di toko', 
        '5  || ' + F11 + ' ' * (20 - length(F11)) + ' || Untuk mencari game berdasarkan paramter tertentu', 
        '6  || ' + F16 + ' ' * (20 - length(F16)) + ' || Untuk menyimban data setelah dilakukan perubahan', sep = '\n')
		if role == 'admin':
			print('7  || ' + F02 + ' ' * (20 - length(F02)) + ' || Untuk melakukan registraasi user baru', 
            '8  || ' + F04 + ' ' * (20 - length(F04)) + ' || Untuk menambah game ke dalam toko',
            '9  || ' + F05 + ' ' * (20 - length(F05)) + ' || Untuk mengubah data game yang ada di toko',
            '10 || ' + F06 + ' ' * (20 - length(F06)) + ' || Untuk mengubah stok game yang ada di toko',
            '11 || ' + F12 + ' ' * (20 - length(F12)) + ' || Untuk menambahkan saldo kepada user', sep = '\n')
		elif role == 'user':
			print('7  || ' + F08 + ' ' * (20 - length(F08)) + ' || Untuk membeli game', 
            '8  || ' + F09 + ' ' * (20 - length(F09)) + ' || Untuk melihat daftar game yang telah dibeli',
            '9  || ' + F10 + ' ' * (20 - length(F10)) + ' || Untuk mencari game yang telah dibeli',
            '10 || ' + F13 + ' ' * (20 - length(F13)) + ' || Untuk melihat riwayat pembelian game', sep = '\n')

def exit(d):
	if inputs.input_yesorno('Apakah kamu ingin menyimpan data sebelum keluar? '):
		data.save_data(d)
	print('Terima kasih! Jangan lupa mampir lagi xixixi ＼ʕ •ᴥ•ʔ／')
	sys.exit()
