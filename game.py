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
        tahun_rilis = inputs.input_number("Masukkan tahun rilis: ", validation = lambda x : utility.length(x) <= 4, provision = 'Tahun rilis harus berupa angka.')
        harga = inputs.input_number("Masukkan harga: ", provision = 'Harga harus berupa angka.')
        stok = inputs.input_number("Masukkan stok awal: ", provision = 'Stok harus berupa angka.')
        add = [nama, kategori, tahun_rilis, harga, stok]
        empty = 0
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
    return data

def ubah_stok(data):
    """Fungsi untuk mengubah stok game (F06)"""
    id = inputs.input_valid("Masukkan ID game: ", validation = lambda x : filter_sep(x), flagstop = '!x')
    if id == '!x':
        return
    idx = 0
    flag = False
    while not flag and idx < utility.length(data[1]):
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
                print("Stok game " + data[1][idx][1][1] + " gagal dikurangi. Stok sekarang: " + str(current_stock) + "( < " + str(abs(change)) + ")")
            data[1][idx][5][1] = str(current_stock)
        except ValueError:
            print("Input tidak valid! Stok harus berupa angka.")
    return data

def ubah_game(data):
    """Fungsi untuk mengubah informasi game kecuali ID game dan stok"""
    id = inputs.input("Masukkan ID game: ", validation = lambda x : inputs.filter_sep(x), flagstop = '!x')
    if id == '!x':
        return
    else:
        found = False
        idx = 0
        for i in range(utility.length(data[1])):
            if id == data[1][i][0][1]:
                found = True
                idx = i
                break
        if not found:
            print("Tidak ada game dengan ID tersebut!")
        else:
            # Berdasarkan Q&A, input dibawah ini dipastikan sudah sesuai
            nama = input("Masukkan nama game: ").title()
            kategori = input("Masukkan kategori: ").title()
            tahun_rilis = input("Masukkan tahun rilis: ")
            harga = input("Masukkan harga: ")
            change = [nama, kategori, str(tahun_rilis), str(harga)]

            # Cek character terlarang ';'
            for i in change:
                if not (inputs.filter_sep(i)):
                    print('Input tidak valid, mengandung character terlarang.')
                    return

            # Cek inputan yang empty
            if inputs.is_empty(change):
                print("Semua field kosong. Tidak ada perubahan yang dilakukan.")
            else:
                for i in range(utility.length(change)):
                    if change[i] != '':
                        data[1][idx][i+1][1] = change[i]
                print(f"Informasi {id} berhasil diubah.")
    return data

def list_game_toko_descending(data, scheme):
    """Fungsi mengurutkan dari terbesar ke terkecil (menurun)"""
    for i in range(utility.length(data) - 1):
        idx_max = i
        for j in range(i, utility.length(data)):
            if scheme == 'tahun':
                if int(data[idx_max][3][1]) < int(data[j][3][1]):
                    idx_max = j
            elif scheme == 'harga':
                if int(data[idx_max][4][1]) < int(data[j][4][1]):
                    idx_max = j
        temp = data[idx_max]
        data[idx_max] = data[i]
        data[i] = temp

    # Mencetak hasil pengurutan
    for i in range(utility.length(data)):
        print(f"{i + 1}. {data[i][0][1]} | {data[i][1][1]} {spaces(data, data[i][1][1], 1)}| {data[i][4][1]} {spaces(data, data[i][4][1], 4)}| {data[i][2][1]} {spaces(data, data[i][2][1], 2)}| {data[i][3][1]} | {data[i][5][1]}")

def list_game_toko_ascending(data, scheme):
    """Fungsi mengurutkan dari terkecil ke terbesar (menaik)"""
    for i in range(utility.length(data) - 1):
        idx_min = i
        for j in range(i, utility.length(data)):
            if scheme == 'tahun':
                if int(data[idx_min][3][1]) > int(data[j][3][1]):
                    idx_min = j
            elif scheme == 'harga':
                if int(data[idx_min][4][1]) > int(data[j][4][1]):
                    idx_min = j
        temp = data[idx_min]
        data[idx_min] = data[i]
        data[i] = temp

    # Mencetak hasil pengurutan
    for i in range(utility.length(data)):
        print(f"{i + 1}. {data[i][0][1]} | {data[i][1][1]} {spaces(data, data[i][1][1], 1)}| {data[i][4][1]} {spaces(data, data[i][4][1], 4)}| {data[i][2][1]} {spaces(data, data[i][2][1], 2)}| {data[i][3][1]} | {data[i][5][1]}")

def game_idx(id):
    # format = GAMEXXX
    temp = ''
    for i in range(7):
        if i >= 4:
            temp += id[i]
    return int(temp)

def list_game_toko_base(data, output = False):
    """Fungsi mengurutkan dari ID terkecil ke terbesar"""
    for i in range(utility.length(data) - 1):
        idx_min = i
        for j in range(i, utility.length(data)):
            temp = data[idx_min][0][1] # GAMEID -> GAMEXXX
            temp1 = data[j][0][1] # GAMEID setelahnya (dibandingkan)
            if game_idx(temp) > game_idx(temp1):
                idx_min = j
        temp_data = data[idx_min]
        data[idx_min] = data[i]
        data[i] = temp_data

    # Mencetak hasil pengurutan
    if output:
        for i in range(utility.length(data)):
            print(f"{i + 1}. {data[i][0][1]} | {data[i][1][1]} {spaces(data, data[i][1][1], 1)}| {data[i][4][1]} {spaces(data, data[i][4][1], 4)}| {data[i][2][1]} {spaces(data, data[i][2][1], 2)}| {data[i][3][1]} | {data[i][5][1]}")

def spaces(data, current_data, key):
    max1 = 0 # max spaces
    for i in range(utility.length(data)):
        if utility.length(data[i][key][1]) > max1:
            max1 = utility.length(data[i][key][1])
    return (' ' * (max1 - utility.length(current_data)))

def list_game_toko(data):
    """Fungsi mencetak hasil skema pengurutan"""
    # Menyimpan data pada variabel baru agar saat di save tidak merubah urutan database utama
    dummy_data = []
    for i in data:
        dummy_data += [i]

    prompt = input("Skema sorting: ")
    if prompt == 'tahun+':
        list_game_toko_ascending(dummy_data[1], 'tahun')
    elif prompt == 'tahun-':
        list_game_toko_descending(dummy_data[1], 'tahun')
    elif prompt == 'harga+':
        list_game_toko_ascending(dummy_data[1], 'harga')
    elif prompt == 'harga-':
        list_game_toko_descending(dummy_data[1], 'harga')
    elif prompt == '':
        list_game_toko_base(dummy_data[1], output = True)
    else:
        print("Skema sorting tidak valid!")
    # ubah ke posisi awal
    list_game_toko_base(dummy_data[1])

# buy game

def stock(a, data) :
    stock = data[1][a][5][1]   # dari data game
    return int(stock)

def price(a, data) :
    price = data[1][a][4][1]   # dari data game
    return int(price)

def saldo(a, data) :
    saldo = data[0][a][5][1]   # dari data user
    return int(saldo)

def nama_game(a, data) :
    nama_game = data[1][a][1][1]     # dari data game
    return nama_game

def buy_game(userID, d) :
    user = d[0]
    game = d[1]
    riwayat = d[2]
    milik = d[3]

    gameID = inputs.input_valid('Masukkan ID Game: ', validation = lambda x : inputs.filter_sep(x), flagstop = '!x')
    if gameID == '!x':
        return

    for i in range(length(game)) :  # cari gameID di game
        if gameID in game[i][0] :   # jika ada gameID di game
            if stock(i, d) > 0 :       # jika stok > 0
                tidak_punya_game = True
                for j in range(length(milik)) :                             # cari gameID dan userID di milik
                    if gameID in milik[j][0] and userID in milik[j][1] :    # jika sudah memiliki game
                        print('Anda sudah memiliki game tersebut.')
                        tidak_punya_game = False
                        break
                
                if tidak_punya_game == True :
                    for k in range(length(user)) :                          # cari userID di user jika belum memiliki game
                        if userID in user[k][0] :                       
                            if int(saldo(k, d)) >= int(price(i, d)) :                                                   # jika saldo cukup
                                print('Anda berhasil membeli Game "%s". Terima kasih.\n' % game[i][1][1])               # berhasil membeli
                                print('Saldo Anda sekarang adalah Rp' + str(int(saldo(k, d)) - int(price(i, d))) + '.') # saldo baru
                                
                                user[k][5][1] = str(int(saldo(k, d)) - int(price(i, d)))                        # update saldo
                                game[i][5][1] = str(int(stock(i, d)) - 1)                                       # update stok
                                milik += [[['game_id', gameID], ['user_id', userID]]]                            # update kepemilikan
                                riwayat += [[['game_id', gameID], ['nama', str(nama_game(i, d))], ['harga', str(price(i, d))], ['user_id', userID], ['tahun_beli', strftime("%Y", gmtime())]]] # update riwayat
                                break
                            else :
                                print('Saldo Anda tidak cukup.')            # saldo tidak cukup
                                break
        # KETERANGAN :
        # i : index game
        # j : index milik / kepemilikan
        # k : index user

            else :  # jika stok = 0
                print('Mohon maaf, stok Game "%s" sedang habis.' % game[i][1][1])               
            break
        else :  # jika tidak ada game dengan gameID yang diinput
            print('Mohon maaf, game tidak ditemukan.')
            print('Coba periksa kembali masukan Anda. Jika menurut Anda terjadi kesalahan, silakan hubungi admin.')

# list game

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

def panjang_nama(data) :
    longest_name = 0
    for i in range(utility.length(data[1])) :  # dari data game
        if utility.length(nama_game(i, data)) >= longest_name :
            longest_name = utility.length(nama_game(i, data))
    return longest_name         # return length nama game terpanjang

def panjang_kategori(data) :
    longest_category = 0
    for i in range(utility.length(data[1])) :  # dari data game
        if utility.length(kategori(i, data)) >= longest_category :
            longest_category = utility.length(kategori(i, data))
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
    for i in range(utility.length(milik)) :             # untuk setiap game milik user
        if userID == milik[i][1][1] :
            for j in range(utility.length(game)) :          # untuk setiap game
                if game_id(j, d) == milik[i][0][1] :   # jika game_id milik user sama dengan game_id yang dicari
                    list_num += 1
                    print(list_num, end = '. ')     # print nomor urut list game yang dimiliki user
                    
                    print(game_id(i, d), '|', nama_game(i, d), ' ' * (longest_name - utility.length(nama_game(i, d))), '|', kategori(i, d), ' ' * (longest_category - utility.length(kategori(i, d))), '|', tahun_rilis(i, d), '|', price(i, d))
                    tidak_punya_game = False
    # KETERANGAN :
    # i : index dari game milik user
    # j : index dari game
    
    # jika user tidak memiliki game
    if tidak_punya_game == True :
        print("Maaf, kamu belum memiliki game.")
        

# Fungsi mencari game yang dimiliki dari ID dan tahun rilis
def search_my_game(iduser, DataGame, DataKepemilikan):
    id = input("Masukkan ID Game: ")
    thn = input("Masukkan tahun rilis: ")
    
    gameowned = []

    for i in range(utility.length(DataKepemilikan)):
        if DataKepemilikan[i][1][1] == iduser:
            idgame = DataKepemilikan[i][0][1]
            for j in range(utility.length(DataGame)):
                if idgame == DataGame[j][0][1]:
                    gameowned += [DataGame[j]]

    if id:
        for i in range(utility.length(gameowned) - 1, -1, -1):
            if gameowned[i][0][1] != id:
                gameowned = utility.remove_space(gameowned, i)

    if thn:
        for i in range(utility.length(gameowned) - 1, -1, -1):
            if gameowned[i][3][1] != thn:
                gameowned = utility.remove_space(gameowned, i)


    print("\nDaftar game pada inventory yang memenuhi kriteria: ")
    if gameowned:
        print(gameowned)
    else:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
        
# Top Up Saldo 
def topup(DataUser):
    username = input("Masukkan username: ")
    saldo = inputs.input_number("Masukkan harga: ", provision = 'Harga harus berupa angka.')
    found = False
    baris = 0
    for i in range(utility.length(DataUser)):
        if DataUser[i][1][1] == username:
            found = True
            baris = i
            break

    if found:
        saldosaatini = int(DataUser[baris][5][1])
        if saldosaatini + int(saldo) < 0:
            print("Masukan tidak valid.")
        else:
            saldoakhir = saldosaatini + int(saldo)
            DataUser[baris][5][1] = str(saldoakhir)
            nama = DataUser[baris][2][1]
            print(f"Top up berhasil. Saldo {nama} bertambah menjadi {saldoakhir}")
            print(DataUser)
    else:
        print(f'Username "{username}" tidak ditemukan.')
    return DataUser
