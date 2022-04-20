''' ============================ B02 - kerangajaib ==========================='''

# Implementasi LCG (Linear Congruential Generator)

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
# 5. sok asik
# 6. kepo
# 7. coba lagi
# 8. hmmm, gatau
# 9. hehe
# 10. sabeb deh

import time, math, utility

def start():
	print()
	print('kerangajaib : apa?')
	pertanyaan = str(input('kamu        : '))

	kemungkinan = [(0, 'iyaa'), (1, 'ngga'), (2, 'bisa jadi'), (3, 'mungkin'),
				   (4, 'sok asik'), (5, 'kepo'), (6, 'coba lagi'),
				   (7, 'hmmm, gatau'), (8, 'hehe'), (9, 'sabeb deh')]

	# mengambil seconds dari waktu eksekusi
	seconds = math.ceil(time.time())

	# menggunakan variasi seconds dan panjang string dari pertanyaan
	x = seconds
	a = utility.length(pertanyaan)
	c = 3
	m = 2 ** 24

	LCG = ((a * x) + c) % m
	for (p, q) in kemungkinan:
		if LCG % 10 == p:
			print(f'kerangajaib : {q}')
