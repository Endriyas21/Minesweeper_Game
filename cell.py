from tkinter import Button
import random
import settings
class Cell:
    all = []
    def __init__(self, is_mine= False):
        self.is_mine = is_mine
        self.cell_btn_object = None

        Cell.all.append(self)
    
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text = 'Text'
        )
        self.cell_btn_object = btn
    def create_btn_object(self, location):
        btn = Button(
            location,
            text="Text",
        )
        btn.bind('<Button-1', self.left_click_actions)
        btn.bind('<Button-3', self.right_click_actions)

    def left_click_actions(self, event):
        print(event)
        print('left clicked')

    def right_click_actions(self, event):
        print(event)
        print('right clicked')

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"