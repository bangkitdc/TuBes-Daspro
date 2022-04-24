import utility, inputs
from time import strftime, gmtime
from utility import spaces

''' ============================ F04 - tambah_game ==========================='''

def tambah_game(data):
    """Fungsi menambah game"""
    while True:
        # Dibuat validasi per-input (khusus saat menambah game)
        nama = inputs.input_valid("Masukkan nama game: ", flagstop = '!x')
        if nama == '!x':
            return

        nama = nama.title() # Agar diawali huruf kapital
        kategori = inputs.input_valid("Masukkan kategori: ").title()
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

''' ============================ F05 - ubah_game ==========================='''

def ubah_game(data):
    """Fungsi untuk mengubah informasi game kecuali ID game dan stok"""
    id = inputs.input_valid("Masukkan ID game: ", flagstop = '!x')
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

            # Cek inputan yang empty
            if inputs.is_empty(change):
                print("Semua field kosong. Tidak ada perubahan yang dilakukan.")
            else:
                for i in range(utility.length(change)):
                    if change[i] != '':
                        data[1][idx][i+1][1] = change[i]
                print(f"Informasi {id} berhasil diubah.")
    return data

''' ============================ F06 - ubah_stok ==========================='''

def ubah_stok(data):
    """Fungsi untuk mengubah stok game (F06)"""
    id = inputs.input_valid("Masukkan ID game: ", flagstop = '!x')
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

''' ============================ F07 - list_game_toko ==========================='''

''' ============================= Procedure Pembantu ============================'''
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

''' ================================ Fungsi Utama ==============================='''
def list_game_toko(data):
    """Fungsi mencetak hasil skema pengurutan"""
    # Menyimpan data pada variabel baru agar saat di save tidak merubah urutan database utama
    dummy_data = []
    for i in data:
        dummy_data += [i]

    prompt = utility.remove_space(input("Skema sorting: "))
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

''' ============================ F08 - buy_game ==========================='''

''' ========================== Procedure Pembantu ========================='''
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

''' ================================ Fungsi Utama ==============================='''

def buy_game(userID, d) :
    user = d[0]
    game = d[1]
    riwayat = d[2]
    milik = d[3]

    gameID = inputs.input_valid('Masukkan ID Game: ', flagstop = '!x')
    if gameID == '!x':
        return

    ada_game = False
    for i in range(utility.length(game)) :  # cari gameID di game
        if gameID == game[i][0][1] :   # jika ada gameID di game
            ada_game = True

            if stock(i, d) > 0 :       # jika stok > 0
                tidak_punya_game = True
                for j in range(utility.length(milik)) :                             # cari gameID dan userID di milik
                    if gameID == milik[j][0][1] and userID == milik[j][1][1] :    # jika sudah memiliki game
                        print('Anda sudah memiliki game tersebut.')
                        tidak_punya_game = False
                        break
                
                if tidak_punya_game == True :
                    for k in range(utility.length(user)) :                          # cari userID di user jika belum memiliki game
                        if userID == user[k][0][1] :                                # jika userID ada di user
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
    if ada_game == False :  # jika tidak ada game dengan gameID yang diinput
        print('Mohon maaf, game tidak ditemukan.')
        print('Coba periksa kembali masukan Anda. Jika menurut Anda terjadi kesalahan, silakan hubungi admin.')

''' ============================ F09 - list_game ==========================='''

''' ========================== Procedure Pembantu =========================='''
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

''' ================================ Fungsi Utama ==============================='''

def list_game(userID, d) :
    # user = d[0]
    game = d[1]
    # riwayat = d[2]
    milik = d[3]
    
    tidak_punya_game = True
    list_num = 0
    for i in range(utility.length(milik)) :             # untuk setiap game milik user
        if userID == milik[i][1][1] :
            for j in range(utility.length(game)) :          # untuk setiap game
                if game_id(j, d) == milik[i][0][1] :   # jika game_id milik user sama dengan game_id yang dicari
                    print(f"{list_num + 1}. {game[j][0][1]} | {game[j][1][1]} {spaces(game, game[j][1][1], 1)}| {game[j][2][1]} {spaces(game, game[j][2][1], 2)}| {game[j][3][1]} {spaces(game, game[j][3][1], 3)}| {game[j][4][1]}")
                    list_num += 1
                    tidak_punya_game = False
    # KETERANGAN :
    # i : index dari game milik user
    # j : index dari game
    
    # jika user tidak memiliki game
    if tidak_punya_game == True :
        print("Maaf, kamu belum memiliki game.")
        
''' ============================ F10 - search_my_game ==========================='''

# Fungsi mencari game yang dimiliki dari ID dan tahun rilis
def search_my_game(iduser, DataGame, DataKepemilikan):
    # parameter tidak wajib diisi (tidak validasi)
    id = input("Masukkan ID Game: [!x untuk membatalkan] ")
    if id == '!x':
        return

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
                gameowned = utility.removebaris(gameowned, i)

    if thn:
        for i in range(utility.length(gameowned) - 1, -1, -1):
            if gameowned[i][3][1] != thn:
                gameowned = utility.removebaris(gameowned, i)


    print("\nDaftar game pada inventory yang memenuhi kriteria: ")
    if gameowned:
        for i in range(utility.length(gameowned)):
            print(f"{i + 1}. {gameowned[i][0][1]} | {gameowned[i][1][1]} {spaces(gameowned, gameowned[i][1][1], 1)}| {gameowned[i][2][1]} {spaces(gameowned, gameowned[i][2][1], 2)}| {gameowned[i][3][1]} {spaces(gameowned, gameowned[i][3][1], 3)}| {gameowned[i][4][1]}")
    else:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

''' ============================ F11 - search_game_at_store ==========================='''

#Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis
def search_game_at_store(DataGame):
    # parameter tidak wajib diisi (tidak validasi)
    id = input("Masukkan ID Game: [!x untuk membatalkan] ")
    if id == '!x':
        return
    nama = input("Masukkan Nama Game: ").title()
    harga = input("Masukkan Harga: ")
    kategori = input("Masukkan Kategori: ").title()
    thn = input("Masukkan tahun rilis: ")

    if id:
        for i in range(utility.length(DataGame) - 1, -1, -1):
            if DataGame[i][0][1] != id:
                DataGame = utility.removebaris(DataGame, i)

    if nama:
        for i in range(utility.length(DataGame) - 1, -1, -1):
            if DataGame[i][1][1] != nama:
                DataGame = utility.removebaris(DataGame, i)

    if harga:
        for i in range(utility.length(DataGame) - 1, -1, -1):
            if DataGame[i][4][1] != harga:
                DataGame = utility.removebaris(DataGame, i)

    if kategori:
        for i in range(utility.length(DataGame) - 1, -1, -1):
            if DataGame[i][2][1] != kategori:
                DataGame = utility.removebaris(DataGame, i)

    if thn:
        for i in range(utility.length(DataGame) - 1, -1, -1):
            if DataGame[i][3][1] != thn:
                DataGame = utility.removebaris(DataGame, i)

    if DataGame:
        print("\nDaftar game pada toko yang memenuhi kriteria: ")
        for i in range(utility.length(DataGame)):
            print(f"{i + 1}. {DataGame[i][0][1]} | {DataGame[i][1][1]} {spaces(DataGame, DataGame[i][1][1], 1)}| {DataGame[i][4][1]} {spaces(DataGame, DataGame[i][4][1], 4)}| {DataGame[i][2][1]} {spaces(DataGame, DataGame[i][2][1], 2)}| {DataGame[i][3][1]} | {DataGame[i][5][1]}")
    else:
        print("Tidak ada game pada toko yang memenuhi kriteria")   

''' ============================ F12 - topup ==========================='''

# Top Up Saldo 
def topup(DataUser):
    username = inputs.input_valid("Masukkan username: ", flagstop = '!x')
    if username == '!x':
        return
    saldo = inputs.input_number("Masukkan harga: ", provision = 'Saldo harus berupa angka.')
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
    else:
        print(f'Username "{username}" tidak ditemukan.')
    return DataUser

''' ============================ F13 - riwayat ==========================='''

# Melihat Riwayat Pembelian
def riwayat(iduser, DataRiwayat):
    datariwayatuser = []
    for i in range(utility.length(DataRiwayat)):
        if DataRiwayat[i][3][1] == iduser:
            datariwayatuser += [utility.removebaris(DataRiwayat[i], 3)]
    # output

    if datariwayatuser == []:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah `buy_game` untuk membeli.')
    else:
        print('Daftar game:')
        for i in range(utility.length(datariwayatuser)):
            print(f"{i + 1}. {datariwayatuser[i][0][1]} | {datariwayatuser[i][1][1]} {spaces(datariwayatuser, datariwayatuser[i][1][1], 1)}| {datariwayatuser[i][2][1]} {spaces(datariwayatuser, datariwayatuser[i][2][1], 2)}| {datariwayatuser[i][3][1]} {spaces(datariwayatuser, datariwayatuser[i][3][1], 3)}")
