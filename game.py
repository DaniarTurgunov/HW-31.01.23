max_total = {}
total = []
new_game = {}

def set_max_total(value: int, mes_id: str):
    global max_total
    max_total[mes_id] = value
    print(max_total)

def set_game(mes_id:str, game_st: str):
    global new_game
    new_game[mes_id] = game_st
    print(new_game)



