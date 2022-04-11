import utility


def tambah_game(data):
    """Fungsi menambah game"""
    flag = False
    while not flag:
        # id = input("Masukkan id game: ")
        nama = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok = input("Masukkan stok awal: ")
        add = [nama, kategori, tahun_rilis, harga, stok]
        empty = 0
        for i in add:
            if i == '':
                empty += 1
        if empty == 0:
            data[1] += [[
                ['id', 'GAME' + id_generator(utility.length(data[1]) + 1)],
                ['nama', add[0]],
                ['kategori', add[1]],
                ['tahun_rilis', add[2]],
                ['harga', add[3]],
                ['stok', add[4]]
            ]]
            print("Selamat! Berhasil menambahkan game", add[1])
            break
        else:
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
    return data


def id_generator(num):
    if 1 <= num <= 9:
        return '00' + str(num)
    elif 10 <= num <= 99:
        return '0' + str(num)
    else:
        return str(num)
"""
cek = tambah_game()
print(cek)
"""