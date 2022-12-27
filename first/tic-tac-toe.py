player1 = input('Введите имя игрока №1, будет играть "Крестиками": ')
player2 = input('Введите имя игрока №2, будет играть "Ноликами": ')

field = [
    [' ', '1', '2', '3'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-'],
    ['3', '-', '-', '-']
]


def check():
    if field[1][1] == 'x' and field[1][2] == 'x' and field[1][3] == 'x':
        print(f'{player1} побеждает!')
    elif field[2][1] == 'x' and field[2][2] == 'x' and field[2][3] == 'x':
        print(f'{player1} побеждает!')
    elif field[3][1] == 'x' and field[3][2] == 'x' and field[3][3] == 'x':
        print(f'{player1} побеждает!')

    elif field[1][1] == 'x' and field[2][1] == 'x' and field[3][1] == 'x':
        print(f'{player1} побеждает!')
    elif field[1][2] == 'x' and field[2][2] == 'x' and field[3][2] == 'x':
        print(f'{player1} побеждает!')
    elif field[1][3] == 'x' and field[2][3] == 'x' and field[3][3] == 'x':
        print(f'{player1} побеждает!')

    elif field[1][1] == 'x' and field[2][2] == 'x' and field[3][3] == 'x':
        print(f'{player1} побеждает!')


    if field[1][1] == 'o' and field[1][2] == 'o' and field[1][3] == 'o':
        print(f'{player2} побеждает!')
    elif field[2][1] == 'o' and field[2][2] == 'o' and field[2][3] == 'o':
        print(f'{player2} побеждает!')
    elif field[3][1] == 'o' and field[3][2] == 'o' and field[3][3] == 'o':
        print(f'{player2} побеждает!')

    elif field[1][1] == 'o' and field[2][1] == 'o' and field[3][1] == 'o':
        print(f'{player2} побеждает!')
    elif field[1][2] == 'o' and field[2][2] == 'o' and field[3][2] == 'o':
        print(f'{player2} побеждает!')
    elif field[1][3] == 'o' and field[2][3] == 'o' and field[3][3] == 'o':
        print(f'{player2} побеждает!')

    elif field[1][1] == 'o' and field[2][2] == 'o' and field[3][3] == 'o':
        print(f'{player2} побеждает!')


def show_field():
    for row in field:
        for element in row:
            print(element, end=' ')
        print()
    print(f'Для назначения своего хода используйте координаты \n'
          f'сначала сверху (1, 2, 3), затем сбоку (1, 2, 3).')


def players_turn():
    def player1_turn():
        player1_chose = input(f'Сейчас ходит {player1}: ').split()
        b1, a1 = int(player1_chose[0]), int(player1_chose[1])
        if field[a1][b1] == '-':
            field[a1][b1] = 'x'
        else:
            print('Эта клетка уже занята.')
            player1_turn()

    show_field()

    def player2_turn():
        player2_chose = input(f'Сейчас ходит {player2}: ').split()
        b2, a2 = int(player2_chose[0]), int(player2_chose[1])
        if field[a2][b2] == '-':
            field[a2][b2] = 'o'
        else:
            print('Эта клетка уже занята.')
            player2_turn()

    player1_turn()
    show_field()
    check()
    player2_turn()
    show_field()
    check()


players_turn()
show_field()
