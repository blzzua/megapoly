class Bank:
    balance = 100_000

class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 15_000
        self.owned_companies = []
        self.skip_turns = 0

class Cell:
    def __init__(self, name, type_, **kwargs):
        self.name = name
        self.type = type_  # TODO set on enum of cell type
        self.prev = None
        self.next = None

class Board:
    def __init__(self):
        self.cells = []
        self.cells.append(Cell(name='Start', type_='Start'))
        self.cells.append(Cell(name='SomeCompany', type_='company', color='green', price=650, rent1=150, rent2=300, rent3=600, prev=self.cells[0]))
        self.cells.append(Cell(name='AnotherCompany', type_='company', color='red', price=700, rent1=150, rent2=300, rent3=600,  prev=self.cells[-1]))

class Game:
    def __init__(self, players_count=2):
        _colors = ['red', 'green']
        self.players = [Player(name=color) for color, player in zip(_colors, range(players_count))]


if __name__ == '__main__':
    g = Game()
    board = Board()
    print(Board)
