field = list(range(1,10))
def game_pole(field):
    print("-" * 13)
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("-" * 13)

def Player(cell):
    valid = False
    while not valid:
        player_answer = input(f"Ход {cell}: ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(field[player_answer - 1]) not in "XO":
                field[player_answer - 1] = cell
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(filed):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if filed[each[0]] == filed[each[1]] == filed[each[2]]:
            return filed[each[0]]
    return False

def main(field):
    counter = 0
    win = False
    while not win:
        game_pole(field)
        if counter % 2 == 0:
            Player("X")
        else:
            Player("O")
        counter += 1

        tmp = check_win(field)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if counter == 9:
            print("Ничья!")
            break
    game_pole(field)
main(field)