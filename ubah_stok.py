import data
from utility import length
array = [[[['id', '1'], ['username', 'admin'], ['nama', 'Admin'], ['password', 'bklzo2584>'], ['role', 'admin'],
        ['saldo', '100000']], [['id', '2'], ['username', 'tara123'], ['nama', 'Tara'], ['password', 'bazbobtabokn'],
        ['role', 'user'], ['saldo', '50000']]], [[['id', 'GAME001'], ['nama', 'Python Gaming'], ['kategori', 'Adventure'],
        ['tahun_rilis', '2022'], ['harga', '150000'], ['stok', '100']], [['id', 'GAME002'], ['nama', 'PUBG'],
        ['kategori', 'WAR'], ['tahun_rilis', '2019'], ['harga', '20000'], ['stok', '23']], [['id', 'GAME003'],
        ['nama', 'apawe'], ['kategori', 'apacik'], ['tahun_rilis', '1028'], ['harga', '20000'], ['stok', '23']]],
        [[['game_id', 'GAME001'], ['nama', 'Valorant'], ['harga', '0'], ['user_id', '1'], ['tahun_beli', '2021']]],
        [[['game_id', 'GAME001'], ['user_id', '1']]]]


def ubah_stok(data):
    """Fungsi untuk mengubah stok game (F06)"""
    id = input("Masukkan ID game: ")
    idx = 0
    flag = False
    while not flag and idx < length(data[1]):
        if data[1][idx][0][1] == id:
            flag = True
        else:
            idx += 1
    if not flag:
        print("Tidak ada game dengan ID tersebut!")
    else:
        try:
            change = int(input("Masukkan jumlah: "))
            current_stock = int(data[1][idx][5][1])
            if current_stock + change >= 0:
                current_stock += change
                if change > 0:
                    print("Stok game " + data[1][idx][1][1] + " berhasil ditambahkan. Stok sekarang: " + str(current_stock))
                elif change < 0:
                    print("Stok game " + data[1][idx][1][1] + " berhasil dikurangi. Stok sekarang: " + str(current_stock))
                else:  # change == 0
                    print("Stok tidak diubah. Stok sekarang: ", current_stock)
            else:
                print("Stok game " + data[1][idx][1][1] + " gagal dikurangi. Stok sekarang: " + str(current_stock))
            data[1][idx][5][1] = str(current_stock)
        except ValueError:
            print("Stok harus berupa angka")
    return data
