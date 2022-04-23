''' ============================ B01 - hash(cipher) ==========================='''

# Implementasi affine cipher
# Menggunakan Euclid's Algorithm dan Extended Euclid's Algorithm

def encrypt(text, key = [3, 1]):
	# e(x) = (a * x + b) mod m
	hasil = ''
	for i in text:
		if i == '4':
			hasil += i # pengecualian karena '4' menghasilkan ';'

		# alphabet, simbol, dan angka
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
		if i == '4': # pengecualian karena '4' menghasilkan ';'
			hasil += i

		# alphabet, simbol, dan angka
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
	# Euclid's Algorithm (FPB)
	# gcd(x, y) = gcd(x, y - x) = gcd(x, y % x)
	 while y > 0:
	 	temp = x
	 	x = y
	 	y = temp % y

	 # return saat salah satu angka 0
	 return x

def modinv(a, b):
	# Extended Euclid's Algorithm (ax + by = gcd(a, b))
	g = gcd(a, b)

	if g != 1: # modular inverse ada, jika dan hanya jika gcd(a, b) = 1
		return None

	# a > b
	if b > a:
		temp = a
		a = b
		b = temp

	# table
	q = [-1, -1]
	r = [a, b]
	s = [1, 0]
	t = [0, 1]

	# selama remainder > 0
	while r[-1] > 0:
		q += [r[-2] // r[-1]] # quotient = (remainder[-2]) // (remainder[-1])
		r += [r[-2] % r[-1]] # remainder = hasil bagi (remainder[-2] dan remainder[-1])

		# s * a + t * b = remainder
		s += [s[-2] - q[-1] * s[-1]] # koefisien dari a
		t += [t[-2] - q[-1] * t[-1]] # koefisien dari b

	# return koefisien b saat remainder = 0
	# ini yang menyebabkan modulo inverse dari a, ax = 1 (mod b)
	return t[-2]
