import settings

def height_prct(percentage):
    return (settings.HEIGHT/100)* percentage

def width_prct(percentage):
    return (settings.WIDTH /100) * percentage

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