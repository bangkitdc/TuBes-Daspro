def encrypt(text, key = [3, 1]):
	# e(x) = (a * x + b) mod m
	hasil = ''
	for i in text:
		if i == '4':
			hasil += i
		elif (33 <= ord(i) <= 64):
			hasil += chr((key[0] * (ord(i) - 33) + key[1]) % 32 + 33)
		elif 65 <= ord(i) <= 90:
			hasil += chr((key[0] * (ord(i) - 65) + key[1]) % 26 + 65)
		elif 97 <= ord(i) <= 122:
			hasil += chr((key[0] * (ord(i) - 97) + key[1]) % 26 + 97)
		else:
			hasil += i
	return hasil

def decrypt(text, key = [3, 1]):
	# d(x) = (a^(-1) * (x - b)) mod m
	hasil = ''
	for i in text:
		if i == '4':
			hasil += i
		elif 33 <= ord(i) <= 64:
			hasil += chr((modinv(key[0], 32) * (ord(i) - key[1] - 33)) % 32 + 33)
		elif 65 <= ord(i) <= 90:
			hasil += chr((modinv(key[0], 26) * (ord(i) - key[1] - 65)) % 26 + 65)
		elif 97 <= ord(i) <= 122:
			hasil += chr((modinv(key[0], 26) * (ord(i) - key[1] - 97)) % 26 + 97)
		else:
			hasil += i
	return hasil

def gcd(x,y):
	# euclid algorithm
	# gcd(x, y) = gcd(x, y - x) = gcd(x, y % x)
	 while y > 0:
	 	# x, y = y, x % y
	 	temp = x
	 	x = y
	 	y = temp % y

	 return x

def modinv(a, m):
	for i in range(1, m):
		if ((a % m) * (i % m)) % m == 1:
			return i
	return -1

