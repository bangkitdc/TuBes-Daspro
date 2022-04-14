from utility import length

# Contoh data
# d = [[[['id', '1'], ['username', 'admin'], ['nama', 'Admin'], ['password', 'bklzo2584>'], ['role', 'user'], ['saldo', '100000']], [['id', '2'], ['username', 'tara123'], ['nama', 'Tara'], ['password', 'bazbobtabokn'], ['role', 'user'], ['saldo', '50000']]], [[['id', 'GAME001'], ['nama', 'Python Gaming'], ['kategori', 'Adventure'], ['tahun_rilis', '2022'], ['harga', '150000'], ['stok', '100']], [['id', 'GAME069'], ['nama', 'Haskell Gaming'], ['kategori', 'Programming'], ['tahun_rilis', '2015'], ['harga', '230000'], ['stok', '25']]], [[['game_id', 'GAME001'], ['nama', 'Valorant'], ['harga', '0'], ['user_id', '1'], ['tahun_beli', '2021']]], [[['game_id', 'GAME001'], ['user_id', '2']], [['game_id', 'GAME069'], ['user_id', '2']]]]


def game_id(a, data) :
    game_id = data[1][a][0][1]       # dari data game
    return game_id

def nama_game(a, data) :
    nama_game = data[1][a][1][1]     # dari data game
    return nama_game

def kategori(a, data) :
    kategori = data[1][a][2][1]      # dari data game
    return kategori

def tahun_rilis(a, data) :
    tahun_rilis = data[1][a][3][1]   # dari data game
    return tahun_rilis

def price(a, data) :
    price = data[1][a][4][1]         # dari data game
    return int(price)

def panjang_nama(data) :
    longest_name = 0
    for i in range(length(data[1])) :  # dari data game
        if length(nama_game(i, data)) >= longest_name :
            longest_name = length(nama_game(i, data))
    return longest_name         # return length nama game terpanjang

def panjang_kategori(data) :
    longest_category = 0
    for i in range(length(data[1])) :  # dari data game
        if length(kategori(i, data)) >= longest_category :
            longest_category = length(kategori(i, data))
    return longest_category     # return length kategori game terpanjang

def list_game(userID, d) :
    # user = d[0]
    game = d[1]
    # riwayat = d[2]
    milik = d[3]
    
    longest_name = panjang_nama(d)           # length nama game terpanjang
    longest_category = panjang_kategori(d)   # length kategori game terpanjang

    tidak_punya_game = True
    list_num = 0
    for i in range(length(milik)) :             # untuk setiap game milik user
        if userID == milik[i][1][1] :
            for j in range(length(game)) :          # untuk setiap game
                if game_id(j, d) == milik[i][0][1] :   # jika game_id milik user sama dengan game_id yang dicari
                    list_num += 1
                    print(list_num, end = '. ')     # print nomor urut list game yang dimiliki user
                    
                    print(game_id(i, d), '|', nama_game(i, d), ' ' * (longest_name - length(nama_game(i, d))), '|', kategori(i, d), ' ' * (longest_category - length(kategori(i, d))), '|', tahun_rilis(i, d), '|', price(i, d))
                    tidak_punya_game = False
    # KETERANGAN :
    # i : index dari game milik user
    # j : index dari game
    
    # jika user tidak memiliki game
    if tidak_punya_game == True :
        print("Maaf, kamu belum memiliki game.")


# -- TEST --

# userID = '2'    # userID Tara

# list_game(userID, d)

# -- END TEST --