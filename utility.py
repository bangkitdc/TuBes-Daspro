# Implementasi fungsi sendiri

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
