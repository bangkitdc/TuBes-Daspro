import os
import inputs, utility

file_ext = '.csv'
filenames = ['user', 'game', 'riwayat', 'kepemilikan']
headers = []

def read_csv(file, fileidx, sep = ';'):
	global headers

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
		if utility.length(line) == 0:
			break
		if line == '\n':
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
			print(f"Error memparsing CSV: Panjang row & column tidak sinkron saat membaca '{file.name}'")
			exit()
		data += [rowData]
	return data

def load_data(folder_name):
	global filenames, file_ext

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

def to_csv(data, fileidx, sep = ';'):
	global headers

	output = ''
	# print Header
	output = sep.join(headers[fileidx]) + '\n'
	# print tiap baris
	for i in data:
		temp = ''
		for j in range(utility.length(i)):
			temp += i[j][1]
			if j != len(i) - 1:
				temp += sep
		output += temp + '\n'
	return output

def save_data(data):
	global filenames, file_ext

	folder_name = inputs.input_valid('Masukkan nama folder penyimpanan: ', validation = lambda x : filter_folder(x), flagstop = '!x')
	if folder_name == '!x':
		return
	if not os.path.exists(folder_name):
		os.mkdir(folder_name)
	else:
		if not inputs.input_yesorno('Folder sudah ada. Apakah kamu yakin ingin replace folder (mungkin data hilang)? '):
			print('Failed to save data!')
			return
	print('Saving...')
	for i in range(utility.length(filenames)):
		path = os.path.join(folder_name, filenames[i]+file_ext)
		with open(path, 'w') as f:
			f.write(to_csv(data[i], i))
		# kalo error permission denied (tambahan aja)
	print('Data saved succesfully!')

def filter_folder(x):
	exception = '\\/:*?"<>|'
	for i in x:
		if i in exception:
			return False
	return True