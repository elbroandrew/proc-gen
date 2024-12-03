import cv2 as cv
import numpy as np


class DrawManager:
    
    def __init__(self, img, cell_size):
        self.img = img
        self.s=int(cell_size)
        # self.gen = self.write_image_generator()
     
    def draw_rooms(self, rooms):
        
        for room in rooms:
            room.draw()
            # next(self.gen)
        
        
    def draw_corridors(self, adj_list: dict, length=10):
    # the corridor connects exactly only 2 rooms
    
        thickness=3
        color = (70, 150, 150)
        
        
        for room1 in adj_list.keys():
            
            x = room1.x * self.s
            y = room1.y * self.s
            cx = x + self.s//2
            cy = y + self.s//2
            
            for room2 in adj_list[room1]:
                
                if room1.x == room2.x:
                    # draw vertical
                    if room2.y > room1.y:
                        cv.rectangle(self.img._img, (cx, cy+length), (cx, cy+self.s-length), color, thickness)  # S
                        # next(self.gen)
                    else:
                        cv.rectangle(self.img._img, (cx, cy-length), (cx, cy-self.s+length), color, thickness)  # N
                        # next(self.gen)
                if room1.y == room2.y:
                    # draw horizontal
                    if room2.x > room1.x:
                        cv.rectangle(self.img._img, (cx+length, cy), (cx+self.s-length, cy), color, thickness)  # E
                        # next(self.gen)
                    else:
                        cv.rectangle(self.img._img, (cx-length, cy), (cx-self.s+length, cy), color, thickness)  # W
                        # next(self.gen)
    
    
    def draw_grid(self, rows, cols, color=(255,255,0), thickness=1):
        h, w, _ = self.img._img.shape
        dy, dx = h/rows, w/cols
        
        # draw vertical lines
        for x in np.linspace(start=dx, stop=w-dx, num=cols-1):
            x=int(round(x))
            cv.line(self.img._img, (x,0), (x,h), color=color, thickness=thickness)
        # next(self.gen)
            
        # draw horizontal lines
        for y in np.linspace(start=dy, stop=h-dy, num=rows-1):
            y = int(round(y))
            cv.line(self.img._img, (0, y), (w, y), color=color, thickness=thickness)
        # next(self.gen)
            
    def draw_path(self, path):
        if path is None:
            return
        color = (10, 20, 200)
        thickness = 2
        i = 0
        while i < len(path) - 1:
            x = path[i].x * self.s
            y = path[i].y * self.s
            cx = x + self.s//2
            cy = y + self.s//2
            if path[i].x == path[i+1].x:
                # draw vertical
                if path[i+1].y > path[i].y:
                    cv.rectangle(self.img._img, (cx, cy), (cx, cy+self.s), color, thickness)  # S
                    # next(self.gen)
                else:
                    cv.rectangle(self.img._img, (cx, cy), (cx, cy-self.s), color, thickness)  # N
                    # next(self.gen)
            if path[i].y == path[i+1].y:
                # draw horizontal
                if path[i+1].x > path[i].x:
                    cv.rectangle(self.img._img, (cx, cy), (cx+self.s, cy), color, thickness)  # E
                    # next(self.gen)
                else:
                    cv.rectangle(self.img._img, (cx, cy), (cx-self.s, cy), color, thickness)  # W
                    # next(self.gen)
            i += 1

    
    def write_image_generator(self):
        n = 0
        while True:
            cv.imwrite(f"output/{n}.png", self.img._img)
            n += 1
            yield
            
    def dark_regions_create(self, adj_list):
        rooms = list(adj_list.keys())
        for room in rooms:
            if room.hidden is True:
                self.create_region(room.x, room.y)
            
    def create_region(self, x, y):
        xx = x * self.s
        yy = y * self.s
        black = (0,0,0)
        filled = -1
        cv.rectangle(self.img._img, (xx+2, yy+2), (xx+self.s-2, yy+self.s-2), black, filled)
        
    def draw_player(self, player):
        xx = player.x * self.s + self.s//2
        yy = player.y * self.s + self.s//2
        
        filled = 2
        radius = 8
        cv.circle(self.img._img, (xx, yy), radius, (250, 0, 0), filled)
        