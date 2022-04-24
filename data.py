import os, time
import inputs, utility

file_ext = '.csv'
filenames = ['user', 'game', 'riwayat', 'kepemilikan']
headers = []

''' ============================ F15 - load ==========================='''

def read_csv(file, fileidx, sep = ';'):
	global headers
	'''
		Membaca CSV dari file -> list

		Arguments:
			file(IO)			: file yang akan diread
			sep(str, optional)	: separator pada CSV file

		Returns:
			list: data parsed dari CSV file
	'''

	data = []
	text = ''
	line = ''

	# Read header
	line = file.readline()
	header_arr = []
	for i in line:
		if i == sep or i == '\n':
			header_arr += [text]
			text = ''
		else:
			text += i
	headers += [header_arr]

	# Read tiap row dalam file
	while True:
		line = file.readline()
		if utility.length(line) == 0: # file kosong
			break
		if line == '\n': # ignore newline
			continue

		idx = 0
		rowData = [0 for i in range(utility.length(header_arr))]
		for i in line:
			if i == sep or i == '\n':
				rowData[idx] = [header_arr[idx], text]
				text = ''
				idx += 1
			else:
				text += i
		if idx != utility.length(header_arr):
			print(f"Error saat parsing CSV: Panjang row & column tidak sinkron saat membaca '{file.name}'")
			exit()
		data += [rowData]
	return data

def load_data(folder_name):
	global filenames, file_ext
	'''
		Load data pada folder

		Arguments:
			folder_name(str)	: folder database

		Returns:
			list: data keseluruhan dari semu CSV files yang ada di folder_name
	'''

	data = []
	if not os.path.exists(folder_name):
		print('Folder tidak ada. Periksa nama folder kembali.')
		exit()

	for i in range(utility.length(filenames)):
		path = os.path.join(folder_name, filenames[i]+file_ext)
		if not os.path.exists(path):
			print(f'File {filenames[i]+file_ext} tidak ada!')
			exit()
		with open(path, 'r') as f:
			data += [read_csv(f, i)]
	return data

''' ============================ F16 - save ==========================='''

def to_csv(data, fileidx, sep = ';'):
	global headers
	'''
		Mengubah data(list) -> CSV file

		Arguments:
			data(list)			: data yang akan diubah ke CSV file
			sep(str, optional)	: separator pada CSV file

		Returns:
			str 	: CSV strings representasi dari data
	'''
	output = ''
	# masukkan header
	output = utility.join_(sep, headers[fileidx]) + '\n'
	# masukkan tiap baris setelahnya
	for i in data:
		temp = ''
		for j in range(utility.length(i)):
			temp += i[j][1]
			if j != utility.length(i) - 1:
				temp += sep
		output += temp + '\n' # diakhiri dengan newline
	return output

def save_data(data):
	'''
		Save semua data yang ada ke folder database

		Arguments:
			data(list)	: data yang akan disave ke folder (dalam bentuk CSV files)
	'''
	global filenames, file_ext

	folder_name = inputs.input_valid('Masukkan nama folder penyimpanan: ', validation = lambda x : inputs.filter_folder(x), flagstop = '!x')
	if folder_name == '!x':
		return
	if not os.path.exists(folder_name):
		os.mkdir(folder_name)
	else:
		if not inputs.input_yesorno('Folder sudah ada. Apakah kamu yakin ingin replace folder (mungkin data hilang)? '):
			print('Failed to save data!')
			return
	print('Saving...')
	for i in ('...'):
		print(i)
		time.sleep(1)
	for i in range(utility.length(filenames)):
		path = os.path.join(folder_name, filenames[i]+file_ext)
		try:
			with open(path, 'w') as f:
				f.write(to_csv(data[i], i))
		except OSError as error: # error
			print(error)
			print('Data unsaved!')
			return None
	print('Data saved succesfully!')
	return
