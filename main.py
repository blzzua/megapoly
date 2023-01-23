class Bank:
    balance = 100_000

class Player:
    def __init__(self, name, current_cell):
        self.name = name
        self.balance = 15_000
        self.owned_companies = []
        self.skip_turns = 0
        self.current_cell = current_cell

class Cell:
    def __init__(self, name, type_, **kwargs):
        self.name = name
        self.type = type_  # TODO set on enum of cell type
        self.prev = None
        self.next = None
    
    def __str__(self):
        return f'Cell({self.name})'

class Board:
    def __init__(self):
        self.cells = []
        start = Cell(name='Start', type_='Start')
        start.prev = start
        start.next = start
        self.cells.append(start)

        comp = Cell(name='SomeCompany1', type_='company', color='green', price=650, rent1=150, rent2=300, rent3=600, prev=self.cells[-1])
        self.append_cell(comp, start)
        self.append_cell(Cell(name='SomeCompany2', type_='company', color='red', price=700, rent1=150, rent2=300,
                              rent3=600, prev=self.cells[-1]), self.cells[-1])
        self.append_cell(Cell(name='SomeCompany3', type_='company', color='green', price=650, rent1=150, rent2=300,
                              rent3=600, prev=self.cells[-1]), self.cells[-1])
        self.append_cell(Cell(name='SomeCompany4', type_='company', color='red', price=700, rent1=150, rent2=300,
                              rent3=600, prev=self.cells[-1]), self.cells[-1])
        self.append_cell(Cell(name='SomeCompany5', type_='company', color='green', price=650, rent1=150, rent2=300,
                              rent3=600, prev=self.cells[-1]), self.cells[-1])
        self.append_cell(Cell(name='SomeCompany6', type_='company', color='red', price=700, rent1=150, rent2=300,
                              rent3=600, prev=self.cells[-1]), self.cells[-1])

    def append_cell(self, add, after):
        add.next = after.next
        after.next = add
        add.prev = after
        self.cells.append(add)


    def __str__(self):
        return f'Boardgame'

class Game:
    def __init__(self, players_count=2):
        self._init_board()
        _colors = ['red', 'green']
        self.players = [Player(name=color, current_cell=self.board.cells[0]) for color, player in zip(_colors, range(players_count))]
        self.current_player = self.players[0]

    def _init_board(self):
        self.board = Board()

    def make_turn(self):
        points = self.roll_dice()
        while points > 0:
            points = points - 1
            prev_cell = self.current_player.current_cell
            self.current_player.current_cell = self.current_player.current_cell.next
            print(f'Player go from {prev_cell} to {self.current_player.current_cell}')
        
    def roll_dice(self):
        return 4 #  chosen by fail dice roll. guaranteed to be random


if __name__ == '__main__':
    g = Game()
    g.make_turn()
    #print(Board)
