# Game TicTacToe

def update_papan(papan):
	print()
	print('Status Papan')
	for i in range(3):
		for j in range(3):
			print(papan[i][j], end = '')
		print()
	print()

def player_win(papan, player):
	# check rows
	for i in range(3):
		flag = True
		j = 0
		while j < 3 and flag:
			if papan[i][j] != player:
				flag = False
			j += 1
		if flag:
			return flag

	# check columns
	for i in range(3):
		flag = True
		j = 0
		while j < 3 and flag:
			if papan[j][i] != player:
				flag = False
			j += 1
		if flag:
			return flag

	# check diagonals
	# diagonal kanan
	flag = True
	i = 0
	while i < 3 and flag:
		if papan[i][i] != player:
			flag = False
		i += 1
	if flag:
		return flag

	# diagonal kiri
	flag = True
	i = 0
	while i < 3 and flag:
		if papan[i][2 - i] != player:
			flag = False
		i += 1
	if flag:
		return flag

	return False

def papan_full(papan):
	# cek apakah papan full atau tidak
	for i in range(3):
		for j in range(3):
			if papan[i][j] == '#':
				return False
	return True

def ubah_giliran(player):
	return 'X' if player == 'O' else 'O'

def validasi_papan(x, y):
	# validasi input
	if not (1 <= x <= 3) or not (1 <= y <= 3):
		return False
	return True

def papan_terisi(papan, x, y):
	# cek apakah elemen papan[x][y] sudah terisi atau belum
	if papan[x - 1][y - 1] != '#':
		return True
	return False

def start():
	# setup papan
	papan = [['#' for i in range(3)] for j in range(3)]

	print('''Legenda:
# Kosong
X Pemain 1
O Pemain 2''')

	player = 'X'
	while True:
		# cetak papan
		update_papan(papan)

		# input user
		print(f'Giliran Pemain "{player}"')
		x = int(input('baris: '))
		y = int(input('kolom: '))

		# validasi row, column papan
		while not (validasi_papan(x, y)):
			print('Kotak tidak valid.')
			print()
			print(f'Giliran Pemain "{player}"')
			x = int(input('baris: '))
			y = int(input('kolom: '))

		# check elemen papan sudah terisi atau belum
		while papan_terisi(papan, x, y):
			print('Kotak sudah terisi. Silakan pilih kotak lain.')
			print()
			print(f'Giliran Pemain "{player}"')
			x = int(input('baris: '))
			y = int(input('kolom: '))

		# fix row, column
		x -= 1
		y -= 1

		# masukan ke papan
		papan[x][y] = player

		# check menang/ tidak
		if player_win(papan, player):
			update_papan(papan)
			print(f'Pemain "{player}" menang.')
			break

		# check draw
		if papan_full(papan):
			update_papan(papan)
			print('Seri. Tidak ada yang menang.')
			break

		player = ubah_giliran(player)
