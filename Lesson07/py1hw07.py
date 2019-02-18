"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
Если цифра есть на карточке - она зачеркивается и игра продолжается.
Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
Если цифра есть на карточке - игрок проигрывает и игра завершается.
Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random


class Card:
    _pool = [i for i in range(1, 91)]  # пул - набор всех значений откуда берутся номера для карточки. Создал до инита,
    # чтоб он сохранялся для класса и каждая следующая карта брала значения у четом предыдущих карт, чтоб не было
    # повторов номеров между картами

    def __init__(self, name):
        self.name = name
        self._width = 9
        self._height = 3
        self._only_numbers_card = []
        _pool = self.__class__._pool
        #  генерируем пустую карту, точней карту только из пробелов
        self._card = [['  ' for _ in range(1, self._width + 1)] for _ in range(1, self._height + 1)]

        for line_index, line in enumerate(self._card):  # добавил нумерацию чтоб потом выйти на элемент карточки для
            # присвоения значения
            while line.count('  ') > 4:  # по сути - пока в строке меньше 5 заполненых клеток
                for cell_index, number in enumerate(line):
                    if number == '  ' and line.count('  ') > 4 and random.choice([True, False]):
                        options = [pool_elem for pool_elem in _pool
                                   if cell_index * 10 < pool_elem <= (cell_index + 1) * 10]  # делаем выборку из
                        # значений пула которые в 10 раз больше номера клетки для расположения значений по
                        # столбцам: 1-10 первый, 11-20 и так далее. По честному распределение немного другое и
                        # неравномерное, но еще усложнять логику не хотелось. Так же как и правило что в одном
                        # столбце не должно быть больше 2 клеток с числами
                        pick = random.choice(options)
                        self._card[line_index][cell_index] = pick
                        self._only_numbers_card.append(pick)
                        # изымаем значение из пула чтоб не было повторов в следующих картах
                        _pool.pop(_pool.index(pick))

    def show_card(self):
        numbers = ''
        for line in self._card:
            num_line = ' '
            for num in line:
                num_line += str(num).ljust(3)
            numbers += num_line + '\n'
        card_view = '\n' + f'{self.name}'.center(self._width * 3, '-') + '\n' + numbers
        print(card_view)


class Game:
    _bag = [i for i in range(1, 91)]  # мешок с номерами до инита чтоб он не создавался заново со всеми 90 вариантами,
    # мешок не перемешиваю с помощью random.shuffle, так как потом вытягиваю наугад с помощью random.choice

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start_game(self):
        for _ in range(1, 91):
            self.player1.show_card()
            self.player2.show_card()
            if self.card_is_closed():
                print(self.card_is_closed())
                break
            draw = self.draw()
            if not self.player_choice(draw):
                print(f'Игра окончена! {self.player1.name} проиграл!')
                break

    def player_choice(self, draw):
        _card1 = self.player1._card
        _card2 = self.player2._card

        user_input = input('Зачеркнуть? (Y/N) ').upper()

        for line_index, line in enumerate(_card2):  # ход компьютера
            for num_index, number in enumerate(line):
                if number == draw:
                    _card2[line_index][num_index] = '-- '
                    self.player2._only_numbers_card.pop(self.player2._only_numbers_card.index(draw))

        if self._number_in_card(draw):  # ход игрока
            if user_input == 'Y':
                for line_index, line in enumerate(_card1):
                    for num_index, number in enumerate(line):
                        if number == draw:
                            _card1[line_index][num_index] = '-- '
                            self.player1._only_numbers_card.pop(self.player1._only_numbers_card.index(draw))
                            return True
            else:
                return False
        else:
            if user_input == 'Y':
                return False
            else:
                return True

    def _number_in_card(self, draw):
        for line in self.player1._card:
            if draw in line:
                return True
        return False

    def draw(self):
        draw = random.choice(self.__class__._bag)  # тянем бочонок наугад из классового (не создающегося заново) мешка
        print(f'Выпал бочонок с числом {draw}, осталось еще {len(self.__class__._bag) - 1} бочонков')
        self.remove_draw(draw)
        return draw

    def remove_draw(self, draw):
        self.__class__._bag.pop(self.__class__._bag.index(draw))  # наверняка есть более адекватный способ
        # удаления конкретного значения их списка

    def card_is_closed(self):
        if len(self.player1._only_numbers_card) == 0 and len(self.player2._only_numbers_card) == 0:
            return f'Уоооу! Ничья! Не часто такое увидишь!'
        elif len(self.player1._only_numbers_card) == 0:
            return f'Поздравляем! {self.player1.name} Выиграл!'
        elif len(self.player2._only_numbers_card) == 0:
            return f'Поздравляем! {self.player2.name} Выиграл!'
        else:
            return False


player = Card('Игрок')
ai_player = Card('Компьютер')

game = Game(player, ai_player)
game.start_game()
