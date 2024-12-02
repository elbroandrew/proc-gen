import pyglet
from pyglet.window import mouse
from pyglet_draw_manager import DrawManager


width = 512
height = 512
cell_size = 16
max_Y = height
   
window = pyglet.window.Window(width, height, "Title")
batch = pyglet.graphics.Batch()

def invert_y(y):
    return abs(y - max_Y)
    

draw_manager = DrawManager(window, cell_size)
grid = draw_manager.draw_grid(batch)
 
 
@window.event
def on_draw():
    window.clear()
    batch.draw()

    
@window.event
def on_mouse_press(x,y,button, modifiers):
    if button==mouse.LEFT:
        print('Left mouse button pressed!')
        print(f'Mouse clicked at {x}, {invert_y(y)}')
    elif button==mouse.RIGHT:
        print("RIGHT BUTTON CLICK")
    
 
pyglet.app.run()