class TicTacToe:

    data = [[0] * 3 for _ in range(3)]

    @classmethod
    def show_field(cls):
        print('\ta\tb\tc', end='\n1\t')
        print(*cls.data[0], sep='\t', end='\n2\t')
        print(*cls.data[1], sep='\t', end='\n3\t')
        print(*cls.data[2], sep='\t', end='\n')

    @classmethod
    def win(cls, sel):
        data_win = [cls.data[0], cls.data[1], cls.data[2],
                    [cls.data[i][0] for i in range(3)],
                    [cls.data[i][1] for i in range(3)],
                    [cls.data[i][2] for i in range(3)],
                    [cls.data[i][i] for i in range(3)],
                    [cls.data[i][2 - i] for i in range(3)]]
        for dw in data_win:
            if dw.count(sel) == 3:
                return True
        return False
    print('Игра рассчитана на двух игроков.\nИгрок 1 ставит "+", '
          'игрок 2 ставит "-".\n'
          'Желаю хорошо провести время. Удачи!\n')

    @classmethod
    def play(cls):
        sel_data = {'1 a': (0, 0), '1 b': (0, 1), '1 c': (0, 2),
                    '2 a': (1, 0), '2 b': (1, 1), '2 c': (1, 2),
                    '3 a': (2, 0), '3 b': (2, 1), '3 c': (2, 2)}

        flag = False

        cls.show_field()
        while not flag:

            player = input('Введите +/- ')
            select = input('Выберите клетку, например "1 a": ')

            if player in ('-', '+') and select in sel_data:
                i, j = sel_data[select]
                if not cls.data[i][j]:
                    cls.data[i][j] = player
                else:
                    print('Это клетка занята')

                flag = cls.win(player)

                cls.show_field()


ttt = TicTacToe()
ttt.play()
# print(ttt.data)
