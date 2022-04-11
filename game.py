import utility, inputs

def tambah_game(data):
    """Fungsi menambah game"""
    while True:
        # id = input("Masukkan id game: ")
        nama = inputs.input_valid("Masukkan nama game: ", validation = lambda x : inputs.filter_sep(x), flagstop = '!x')
        if nama == '!x':
            return

        nama = nama.title() # Agar diawali huruf kapital
        kategori = inputs.input_valid("Masukkan kategori: ", validation = lambda x : inputs.filter_sep(x)).title()
        tahun_rilis = inputs.input_number("Masukkan tahun rilis: ", validation = lambda x : utility.length(x) <= 4, provision = 'Harus integer.')
        harga = inputs.input_number("Masukkan harga: ", provision = 'Harus integer.')
        stok = inputs.input_number("Masukkan stok awal: ", provision = 'Harus integer.')
        add = [nama, kategori, tahun_rilis, harga, stok]
        empty = 0
        for i in add:
            if i == '':
                empty += 1
        if empty == 0:
            data[1] += [[
                ['id', 'GAME' + inputs.id_generator(utility.length(data[1]) + 1)],
                ['nama', add[0]],
                ['kategori', add[1]],
                ['tahun_rilis', add[2]],
                ['harga', add[3]],
                ['stok', add[4]]
            ]]
            print("Selamat! Berhasil menambahkan game", add[0])
            break
        else:
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
    return data
