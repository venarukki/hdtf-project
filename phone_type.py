import random
import sys
import time


def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # сразу вывод - без буфера
        time.sleep(delay)
    print()


class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def __str__(self):
        return f'Это {self.line_type} телефон. Набор - {self.dial_type}.'

    def ring(self):
        slow_print('"Дзыыыыыыыынь!"')

    def call(self, phone_number):
        slow_print(f'Звоню по номеру {phone_number}! Связь: {self.line_type}.')

    def missed_calls(self, missed_calls_number):
        slow_print('Запрос количества пропущенных вызовов у оператора...')
        time.sleep(1.5)
        slow_print(f'Кол-во пропущенных вызовов: {missed_calls_number}.')


class MobilePhone(Phone):

    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        super().__init__(dial_type_value)
        self.network_type = network_type

    def ring(self):
        slow_print('Пам-пам-пам...ПАМ')

    def start_game(self):
        slow_print('Игра запущена!')


rotary = Phone(dial_type_value='дисковый')
keypad = MobilePhone(dial_type_value='кнопочный', network_type='4G')

slow_print('Запрос информации о первом телефоне...')
time.sleep(1.5)
slow_print(f'{rotary}')
slow_print('И он звонит с таким звуком:')
rotary.ring()
rotary.call('8-800-555-35-35')
rotary.missed_calls(random.randint(1, 10))
slow_print('Запрос информации о втором телефоне...')
time.sleep(1.5)
slow_print(f'{keypad}')
slow_print('А он уже звонит с таким звуком:')
keypad.ring()
keypad.call('8-800-555-35-35')
keypad.missed_calls(random.randint(1, 10))
