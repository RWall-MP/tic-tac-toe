player1 = input('Введите имя игрока №1 он будет играть "Крестиками": ')
player2 = input('Введите имя игрока №2 он будет играть "Ноликами": ')

field = [
    [' ', '1', '2', '3'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-'],
    ['3', '-', '-', '-']
]


def show_field():
    for row in field:
        for element in row:
            print(element, end=' ')
        print()
    print(f'Для назначения своего хода используйте координаты \n'
          f'сначала сверху (1, 2, 3), затем сбоку (1, 2, 3).')


def player_turn():
    player1_chose = input(f'Сейчас ходит {player1}: ').split()
    b1, a1 = int(player1_chose[0]), int(player1_chose[1])
    field[b1][a1] = 'x'
    show_field()
    player2_chose = input(f'Сейчас ходит {player2}: ').split()
    b2, a2 = int(player2_chose[0]), int(player2_chose[1])
    field[b2][a2] = 'o'


show_field()
player_turn()
show_field()
