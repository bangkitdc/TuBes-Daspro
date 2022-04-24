# TuBes-Daspro

1. Buka di terminal dan type `python main.py data'
2. Bisa ketik `help` buat liat command sesuai role
3. Awal mula masuk, itu sebagai role `guest`
4. Disini ada 2 akun
- username: admin, pass: admin12345 -> sebagai admin
- username: tara123, pass: arianagrande -> sebagai user
5. Udah bisa untuk parse csv filenya, nah kalau mau liat struktur datanya ketik 'debug'
6. Dari situ baru kalian bisa mainin data-datanya, bisa juga pake command find_idx_key_with_target(), nah temen2 liat dulu aja contoh penggunaannya gimana, kalau mau demo bisa didemoin di discord
7. Setelah itu untuk ngesave csvnya juga udah bisa, nah itu command-commandnya masih pake `break` semua temen-temen bikin file baru aja `.py` terus nanti gunain fitur import ke main
8. untuk length, strip, dan utility lainnya bisa dilihat di `utility.py`

## Penejelasan tiap file
1. `main.py` ini main dari app kita(parser app disini)
2. `user.py` ini yang berkaitan dengan login/ register/ dll (kemungkinan masih ada bug, belum dilanjut)
3. `inputs.py` ini untuk validasi input, kalau bisa temen-temen ngegunain fungsi input ini, tapi kalau misal dirasa susah pake input biasa juga gapapa
4. `data.py` ini parser dari load csv, read csv, write csv, sama save csv
5. `command.py` ini buat help, exit, dll
6. sisanya itu buat bonus sama aku coba coba
