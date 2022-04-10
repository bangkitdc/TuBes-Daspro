# len() = length()
def length(lst):
	count = 0
	for i in lst:
		count += 1
	return count

# .strip() = remove_space()
def remove_space(s):
	temp = ''
	string = ''
	flag = False
	for i in range(length(s) - 1, -1, -1):
		if s[i] == ' ' and not flag:
			continue
		else:
			flag = True
			temp += s[i]
	for i in range(length(temp) - 1, -1, - 1):
		string += temp[i]
	return string
