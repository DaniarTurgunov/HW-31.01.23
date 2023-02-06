import game
from loader import dp
from aiogram.types import Message

@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
        await message.answer(f'Привет, {message.from_user.full_name}'
                             f'Мы будем играть в конфеты.')
        await message.reply(f'Введи команду "/set_total и число" чтобы установить их общее кол-во')
        mess_id = str(message.from_user.id)
        off = 'off'
        game.set_game(mess_id, off)

@dp.message_handler(commands=['set_total'])
async def max_t(message: Message):
        v = game.new_game
        mes_id = str(message.from_user.id)
        for keys, values in v.items():
            if keys == mes_id:
                if values == 'online':
                    await message.answer('Идет игра, очнись')
                else:
                    while True:
                        max_tot = message.text.split()
                        mes_id = str(message.from_user.id)
                        if max_tot[1].isdigit() and len(max_tot[1]) > 1:
                            game.set_max_total(int(max_tot[1]), mes_id)
                            await message.reply(f'Максимальное кол-во конфет измененно на {max_tot[1]}\n Для продолжения введите команду /continue')
                            print(game.max_total)
                            return False
                        else:
                            await message.reply(f'Нет такого числа, попробуй ещё')
                            return True    

@dp.message_handler(commands=['continue'])
async def mes_start_c(message: Message):
    await message.answer(f'Бери от 1 до 28...')
    v = game.max_total.keys()
    mess_id = str(message.from_user.id)
    for key in v:
        if mess_id == key:
            c = game.max_total.get(key,0)
            print(c)
    my_game = [message.from_user.id, message.from_user.first_name,c]
    on = 'online'
    game.set_game(mess_id, on)
    print(my_game)
    print(game.max_total)
    game.total.append(my_game)
        