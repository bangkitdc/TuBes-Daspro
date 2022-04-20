# Implementasi fungsi pembantu sendiri

# len() = length()
def length(lst):
	count = 0
	for i in lst:
		count += 1
	return count

# .strip() = remove_space()
def remove_space(s, params = 'depan'):
	temp = ''
	string = ''
	flag = False
	# Menghilangkan spaces di belakang string
	for i in range(length(s) - 1, -1, -1):
		if s[i] == ' ' and not flag:
			continue
		else:
			flag = True
			temp += s[i]

	# Menghilangkan spaces di awal string (reversed string, jadi sama saja seperti algoritma sebelumnya)
	flag = False
	for i in range(length(temp) - 1, -1, -1):
		if temp[i] == ' ' and not flag:
			continue
		else:
			flag = True
			string += temp[i]
	return string

# string.join(iterable) = join_(string, iterable)

def join_(e, l):
	temp = ''
	for i in range(length(l)):
		temp += l[i]
		if i != (length(l) - 1):
			temp += e
	return temp

# utility F11 & F13
def removebaris(matriks, baris):
    arraybaru = []
    for i in range(baris):
        arraybaru += [matriks[i]]
    for i in range(baris+1, length(matriks)):
        arraybaru += [matriks[i]]
    return arraybaru

# utility spaces untuk format
# params1 | params2 | params3 | ...
def spaces(data, current_data, key):
    max1 = 0 # max spaces
    for i in range(length(data)):
        if length(data[i][key][1]) > max1:
            max1 = length(data[i][key][1])
    return (' ' * (max1 - length(current_data)))