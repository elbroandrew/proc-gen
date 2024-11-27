import numpy as np
import cv2 as cv
from math import floor
from PIL import Image
from undirected_graph import UndirectedGraph


img_size=512
img1 = Image.new('RGB', (img_size, img_size), (0, 0, 0))
img = cv.cvtColor(np.array(img1), cv.COLOR_BGR2RGB)
rows=cols=16
h, w, channels = img.shape
dy, dx = h/rows, w/cols

def draw_grid(img, rows, cols, color=(255,255,0), thickness=1):
    h, w, _ = img.shape
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
        h, w, _ = self.img.shape
        dy, dx = h/rows, w/cols
    
    
        return floor(xx/dx), floor(yy/dy)

class Room:
    def __init__(self, img, x, y, size, offset=6, id=0):
        self.id = id
        self.x = x
        self.y = y
        s=int(size)
        self.xx = x * s
        self.yy = y * s
        cv.rectangle(img, 
                     (self.xx+offset, self.yy+offset), 
                     (self.xx+s-offset, self.yy+s-offset), 
                     (70, 150, 150), -1)
        
        # draw ID
        cv.putText(img, 
                   str(self.id), 
                   (self.xx+12, self.yy+20), 
                   cv.FONT_HERSHEY_PLAIN, 
                   0.8, 
                   (255, 255, 255), 
                   1, 
                   cv.LINE_AA)
        
    

def draw_corridors(img, adj_list: dict, size, length=8):
    # the corridor connects exactly only 2 rooms
    # adj_list is 'room0.id:[room1.id, room2.id, ..]' adjacency list
    thickness=8

    s=int(size)
    
    for room1 in adj_list.keys():
        
        x = room1.x * s
        y = room1.y * s
        cx = x + s//2
        cy = y + s//2
        
        for room2 in adj_list[room1]:
            # print("room1:", room1.id, "room2: ", room2.id)
            
            
            
            if room1.x == room2.x:
                # draw vertical
                if room2.y > room1.y:
                    cv.rectangle(img, (cx, cy+length), (cx, cy+s-length), (250, 250, 250), thickness)  # S
                else:
                    cv.rectangle(img, (cx, cy-length), (cx, cy-s+length), (250, 250, 250), thickness)  # N
            if room1.y == room2.y:
                # draw horizontal
                if room2.x > room1.x:
                    cv.rectangle(img, (cx+length, cy), (cx+s-length, cy), (250, 250, 250), thickness)  # E
                else:
                    cv.rectangle(img, (cx, cy), (cx, cy), (250, 250, 250), thickness)  # W


def main(img):
    
    coord_store = CoordinateStore(img)
    g = UndirectedGraph()
    
    room = [
        Room(img, 1, 10, dx, id=0),
        Room(img, 1, 11, dx, id=1),
        Room(img, 2, 11, dx, id=2),
        Room(img, 2, 10, dx, id=3),
        Room(img, 2, 9, dx, id=4)
    ]
    
    for r in room:
        g.add_vertex(r)
    
    
    g.add_edge(room[0], room[1])
    g.add_edge(room[1], room[2])
    g.add_edge(room[2], room[3])
    g.add_edge(room[3], room[4])
    
    
    draw_corridors(img, g.get_rooms, dx)

    
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
# create corridor if not exists or if no boundaries.
# check if next cell has room, connect rooms. Finish.
# repeat algorithm few times
