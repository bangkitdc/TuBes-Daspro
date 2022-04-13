# import utility as ul

# Contoh data
# d = [[[['id', '1'], ['username', 'admin'], ['nama', 'Admin'], ['password', 'bklzo2584>'], ['role', 'user'], ['saldo', '100000']], [['id', '2'], ['username', 'tara123'], ['nama', 'Tara'], ['password', 'bazbobtabokn'], ['role', 'user'], ['saldo', '50000']]], [[['id', 'GAME001'], ['nama', 'Python Gaming'], ['kategori', 'Adventure'], ['tahun_rilis', '2022'], ['harga', '150000'], ['stok', '100']]], [[['game_id', 'GAME001'], ['nama', 'Valorant'], ['harga', '0'], ['user_id', '1'], ['tahun_beli', '2021']]], [[['game_id', 'GAME001'], ['user_id', '1']]]]


def length(arr) :
    length = 0
    for i in arr :
        length += 1
    return length

def stock(a, data) :
    stock = data[1][a][5][1]   # dari data game
    return int(stock)

def price(a, data) :
    price = data[1][a][4][1]   # dari data game
    return int(price)

def saldo(a, data) :
    saldo = data[0][a][5][1]   # dari data user
    return int(saldo)

def buy_game(userID, d) :
    user = d[0]
    game = d[1]
    # riwayat = d[2]
    milik = d[3]

    gameID = str(input('Masukkan ID Game: '))

    for i in range(length(game)) :  # cari gameID di game
        if gameID in game[i][0] :   
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
                                game[i][5][1] = str(int(stock(i, d)) - 1)                                    # update stok
                                milik + [[['game_id', gameID], ['user_id', userID]]]                      # update kepemilikan
                                break
                            else :
                                print('Saldo Anda tidak cukup.')                                            # saldo tidak cukup
                                break
    # KETERANGAN :
    # i : index game
    # j : index milik / kepemilikan
    # k : index user

            else :  # jika stok = 0
                print('Mohon maaf, stok Game "%s" sedang habis.' % game[i][1][1])               
            break


# -- TEST --

# userID = '2'    # userID Tara

# buy_game(userID, d)

# -- END TEST --