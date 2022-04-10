# LCG

# Xn+1 = ((a * Xn) + c) mod m
# random integers dari 0 hingga m - 1

# Xn 				-- urutan bilangan pseudo-acak
# m, m > 0			-- modulus
# a, 0 < a < m 		-- pengali
# c, 0 <= c < m 	-- increment
# X0, 0 <= Xo < m 	-- seed/ start value

# 10 kemungkinan jawaban
# 1. iyaa
# 2. ngga
# 3. bisa jadi
# 4. mungkin
# 5. tentunya
# 6. tidak mungkin
# 7. coba lagi
# 8. hmmm, gatau
# 9. hehe
# 10. sabeb deh

def panjang_string(string):
	sum = 0
	for i in string:
		sum += 1
	return sum

def kerangajaib():
	pertanyaan = str(input('Apa pertanyaanmu? '))

	kemungkinan = [(0, 'iyaa'), (1, 'ngga'), (2, 'bisa jadi'), (3, 'mungkin'),
				   (4, 'tentunya'), (5, 'tidak mungkin'), (6, 'coba lagi'),
				   (7, 'hmmm, gatau'), (8, 'hehe'), (9, 'sabeb deh')]

	import time
	import math
	seconds = math.ceil(time.time())

	x = seconds
	a = panjang_string(pertanyaan)
	c = 3
	m = 2 ** 24

	LCG = ((a * x) + c) % m
	for (p, q) in kemungkinan:
		if LCG % 10 == p:
			print(q)

kerangajaib()
