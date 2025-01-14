### Код игры "Битва героев"

#```python
import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} на {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра начата!")
        # Случайный выбор, кто начинает
        #turn = random.choice(['player', 'computer'])
        #print(f"{turn.capitalize()} начинает первым!")

        while self.player.is_alive() and self.computer.is_alive():
            # Случайный выбор, кто атакует
            turn = random.choice(['player', 'computer'])
            print(f"{turn.capitalize()} атакует!")
            if turn == 'player':
                self.player_turn()
                turn = 'computer'  # Меняем ход на компьютер
            else:
                self.computer_turn()
                turn = 'player'  # Меняем ход на игрока

        self.declare_winner()

    def player_turn(self):
        self.player.attack(self.computer)
        print(f"{self.computer.name} осталось здоровья: {self.computer.health}")

    def computer_turn(self):
        self.computer.attack(self.player)
        print(f"{self.player.name} осталось здоровья: {self.player.health}")

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()

### Kanban Доска

# | Этап             | Задача                                         | Статус       |
# |------------------|-----------------------------------------------|--------------|
# | Идея игры        | Определить правила игры                       | Выполнено    |
# | Проектирование   | Создать классы Hero и Game                    | Выполнено    |
# | Игровой процесс  | Реализовать атаку и проверку жизней героев    | Выполнено    |
# | Тестирование     | Проверить разные сценарии                     | В процессе   |
# | Доработка        | Добавить уникальные характеристики героев     | Запланировано|
# | Документация     | Добавить комментарии и написать руководство   | Запланировано|
