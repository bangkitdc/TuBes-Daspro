# lst = []

# def register(lst):
# 	name = str(input('Masukan nama: '))
# 	username = str(input('Masukan username: '))
# 	password = str(input('Masukan password: '))
# 	if username in lst:
# 		print(f'Username {username} sudah terpakai, silakan menggunakan username lain.')
# 	else:
# 		print(f'Username {username} telah berhasil register ke dalam "Binomo".')
# 		lst += [(name, username, password)]
# 	return

# lst = [('hehe', 'hehe', 'hehe')]

# name = str(input())
# username = str(input())
# password = str(input())

# def filter_username(name, username, password, lst, target):
# 	for (x, y, z) in lst:
# 		if y == target:
# 			print('ada')
# 			return
# 	print('gaada')
# 	lst += [(name, username, password)]
# 	return lst

# filter_username(name, username, password, lst, username)
# print(lst)

# def gcd(x,y):
# 	 while y > 0:
# 	 	temp = x
# 	 	x = y
# 	 	y = temp % y

# 	 return x

def modinv(a, m):
	for i in range(1, m):
		if ((a % m) * (i % m)) % m == 1:
			return i
	return -1

# def xgcd(a, b):
#     a, b = max(a, b), min(a, b)

#     q = [-1, -1]
#     r = [a, b]
#     s = [1, 0]
#     t = [0, 1]

#     while r[-1] > 0:
#         q.append(r[-2] // r[-1])
#         r.append(r[-2] % r[-1])
#         s.append(s[-2] - q[-1] * s[-1])
#         t.append(t[-2] - q[-1] * t[-1])

#     print(q)
#     print(r)
#     print(s)
#     print(t)
#     return s[-2], t[-2]

# x, y = map(int, input().split())
# print(xgcd(x,y))

key = [3, 1]
def encrypt(text, key):
	# e(x) = (a * x + b) mod m
	hasil = ''
	for i in text:
		if 33 <= ord(i) <= 64:
			hasil += chr((key[0] * (ord(i) - 33) + key[1]) % 32 + 33)
		elif 65 <= ord(i) <= 90:
			hasil += chr((key[0] * (ord(i) - 65) + key[1]) % 26 + 65)
		elif 97 <= ord(i) <= 122:
			hasil += chr((key[0] * (ord(i) - 97) + key[1]) % 26 + 97)
		else:
			hasil += i
	return hasil

def decrypt(text, key):
	# d(x) = (a^(-1) * (x - b)) mod m
	hasil = ''
	for i in text:
		if 33 <= ord(i) <= 64:
			hasil += chr((modinv(key[0], 32) * (ord(i) - key[1] - 33)) % 32 + 33)
		elif 65 <= ord(i) <= 90:
			hasil += chr((modinv(key[0], 26) * (ord(i) - key[1] - 65)) % 26 + 65)
		elif 97 <= ord(i) <= 122:
			hasil += chr((modinv(key[0], 26) * (ord(i) - key[1] - 97)) % 26 + 97)
		else:
			hasil += i
	return hasil

# def encrypt(text, key):
# 	# e(x) = (a * x + b) mod m
# 	hasil = ''
# 	for i in text:
# 		if 32 <= ord(i) <= 127:
# 			hasil += chr((key[0] * (ord(i) - 32) + key[1]) % 96 + 32)
# 		else:
# 			hasil += i
# 	return hasil

# def decrypt(text, key):
# 	# d(x) = (a^(-1) * (x - b)) mod m
# 	hasil = ''
# 	for i in text:
# 		if 32 <= ord(i) <= 127:
# 			hasil += chr((modinv(key[0], 96) * (ord(i) - key[1] - 32)) % 96 + 32)
# 		else:
# 			hasil += i
# 	return hasil

text = input()
print(encrypt(text, key))
text1 = decrypt(encrypt(text, key), key)
print(text1)

print(text == text1)

# message = '>>> '
# inp = input(message).strip(" ")

# print(inp)