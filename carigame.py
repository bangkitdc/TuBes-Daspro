from ctypes import util
import utility
# Fungsi mencari game yang dimiliki dari ID dan tahun rilis

# Kamus 

# Algoritma

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
