from pyglet import shapes


class DrawManager:
    
    def __init__(self, window, cell_size):
        self.w, self.h = window.width, window.height
        self.cell_size = self.w / cell_size
        self.s = int(self.cell_size)
 
    
    
    def draw_grid(self, batch):
        w = 2
        color = (0, 230, 0)
        grid = []
        for i in range(0, self.w, self.s):
            linex = shapes.Line(i, 0, i, self.w, width=w, color=color, batch=batch)
            linex.opacity = 250
            grid.append(linex)
            liney = shapes.Line(0, i, self.h, i, width=w, color=color, batch=batch)
            liney.opacity = 250
            grid.append(liney)
        return grid
        