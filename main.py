import numpy as np
import cv2 as cv
from math import floor
from PIL import Image
from collections import namedtuple


img_size=512
# create a black image
# img = np.zeros((img_size,img_size), np.uint8)
img1 = Image.new('RGB', (img_size, img_size), (0, 0, 0))
img = cv.cvtColor(np.array(img1), cv.COLOR_BGR2RGB)
rows=cols=16
h, w, channels = img.shape
dy, dx = h/rows, w/cols

def draw_grid(img, rows, cols, color=(255,255,0), thickness=1):
    h, w, channels = img.shape
    dy, dx = h/rows, w/cols
    
    # draw vertical lines
    for x in np.linspace(start=dx, stop=w-dx, num=cols-1):
        x=int(round(x))
        cv.line(img, (x,0), (x,h), color=color, thickness=thickness)
        
    # draw horizontal lines
    for y in np.linspace(start=dy, stop=h-dy, num=rows-1):
        y = int(round(y))
        cv.line(img, (0, y), (w, y), color=color, thickness=thickness)
        
        
    return img

class CoordinateStore:
    def __init__(self, img):
        self.points=[]
        self.img=img
            

    def click_event(self, event, x, y, flags, params):
        if event == cv.EVENT_LBUTTONDOWN:
            dx, dy = self.converted_coords(rows, cols, x, y)
            print(dx, dy)
            
    def converted_coords(self, rows, cols, xx, yy):
        h, w, channels = self.img.shape
        dy, dx = h/rows, w/cols
    
    
        return floor(xx/dx), floor(yy/dy)
  
def draw_room(img, x, y, size):
    s=int(size)
    x *= s
    y *= s
    cv.rectangle(img, (x, y), (x+s, y+s), (70, 150, 150), -1)
    

def draw_corridor(img, x, y, size, direction):
    s=int(size)
    x *= s
    y *= s
    cx = x + s//2
    cy = y + s//2
    if direction.S:
        cv.rectangle(img, (cx, cy), (cx, cy+s), (250, 250, 250), thickness=3)  # S
    elif direction.N:
        cv.rectangle(img, (cx, cy), (cx, cy-s), (250, 250, 250), thickness=3)  # N
    elif direction.E:
        cv.rectangle(img, (cx, cy), (cx+s, cy), (250, 250, 250), thickness=3)  # E
    elif direction.W:
        cv.rectangle(img, (cx, cy), (cx, cy), (250, 250, 250), thickness=3)  # W




Dir = namedtuple("Dir", ["N", "S", "W", "E"], defaults=[0,0,0,0])
    

def main(img):
    
    coord_store = CoordinateStore(img)
    
    draw_room(img, 1, 10, dx)
    draw_room(img, 1, 11, dx)
    draw_room(img, 2, 11, dx)
    draw_corridor(img, 1, 10, dx, direction=Dir(S=1))
    draw_corridor(img, 1, 11, dx, direction=Dir(E=1))
    
    img = draw_grid(
        img=img,
        rows=rows,
        cols=cols
    )
    
    cv.imshow("image", img)
    
    
    # setting mouse handler for the image 
    # and calling the click_event() function
    cv.setMouseCallback('image', coord_store.click_event)
    
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main(img)
    
    
# TODO: choose random room
# create corridor if not exists
# check if next cell has room, connect rooms. Finish.
# repeat algorithms few times
# Create GRAPH, put all rooms and edges into the graph