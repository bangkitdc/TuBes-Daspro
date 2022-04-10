import os

f = open('data/user.csv', 'r')

data = []
text = ''
line = ''

headers = {}

# Read header
line = f.readline()
header_arr = []

for i in line:
	if i == ';' or i == '\n':
		header_arr += [text]
		text = ''
	else:
		text += i

headers['user'] = header_arr

# Read tiap line setelahnya
while True:
	line = f.readline()
	if len(line) == 0:
		break

	idx = 0
	rowData = [0 for i in range(len(header_arr))]
	for i in line:
		if i == ';' or i == '\n':
			# rowData[header_arr[idx]] = text
			rowData[idx] = [header_arr[idx], text]
			text = ''
			idx += 1
		else:
			text += i
	
	if idx != len(header_arr):
		print(f"Error parsing CSV(row != column)'{f.name}'")
		exit()
	data += [rowData]

filenames = ['user', 'hello']
file_ext = '.csv'
for i in filenames:
	path = os.path.join('data', i+file_ext)
	if not os.path.exists(path):
		print(f'File tidak ada!')

print(data)
# key = 1
# value = 'tara123'

# for i in data:
# 	if i[key][1] == value:
# 		i[key][1] = 'tara456'

# print(i)

f.close()


# d = [user[[]], list_game[[]], list_toko]

# temp = d[0]

# for i in temp:



# d[0][0][0][1]