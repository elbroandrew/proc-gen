import numpy as np
import cv2 as cv
from coord_store import CoordinateStore
from undirected_graph import UndirectedGraph
from image import NewImage
from room_generator import RoomGenerator
from draw_manager import DrawManager


new_img = NewImage()
rows_cols=new_img._rows_cols
cell_size = new_img._cell_size


def draw_grid(img, rows, cols, color=(255,255,0), thickness=1):
    h, w, _ = img._img.shape
    dy, dx = h/rows, w/cols
    
    # draw vertical lines
    for x in np.linspace(start=dx, stop=w-dx, num=cols-1):
        x=int(round(x))
        cv.line(img._img, (x,0), (x,h), color=color, thickness=thickness)
        
    # draw horizontal lines
    for y in np.linspace(start=dy, stop=h-dy, num=rows-1):
        y = int(round(y))
        cv.line(img._img, (0, y), (w, y), color=color, thickness=thickness)
        
        
    return img._img
 

def draw_corridors(img, adj_list: dict, size, length=8):
    # the corridor connects exactly only 2 rooms
    
    thickness=3
    color = (70, 150, 150)
    s=int(size)
    
    for room1 in adj_list.keys():
        
        x = room1.x * s
        y = room1.y * s
        cx = x + s//2
        cy = y + s//2
        
        for room2 in adj_list[room1]:
            
            if room1.x == room2.x:
                # draw vertical
                if room2.y > room1.y:
                    cv.rectangle(img._img, (cx, cy+length), (cx, cy+s-length), color, thickness)  # S
                else:
                    cv.rectangle(img._img, (cx, cy-length), (cx, cy-s+length), color, thickness)  # N
            if room1.y == room2.y:
                # draw horizontal
                if room2.x > room1.x:
                    cv.rectangle(img._img, (cx+length, cy), (cx+s-length, cy), color, thickness)  # E
                else:
                    cv.rectangle(img._img, (cx-length, cy), (cx-s+length, cy), color, thickness)  # W


def main(new_img):
    
    coord_store = CoordinateStore(new_img, rows_cols)
    g = UndirectedGraph()
    generator = RoomGenerator(8, new_img, g, cell_size)
    # from room import Room
    # room = [
    #     Room(new_img, 0, 15, new_img._cell_size),
    #     Room(new_img, 15, 15, new_img._cell_size),
    #     Room(new_img, 0, 0, new_img._cell_size)
    # ]
    # for r in room:
    #     g.add_vertex(r)
        
    
    # g.add_edge(room[0], room[1])
    # g.add_edge(room[1], room[2])
    # g.add_edge(room[2], room[3])
    # g.add_edge(room[3], room[4])
    
    generator.create_first_room()
    r = generator.choose_random_room()
    
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    generator.place_next_room()
    
    
    draw_corridors(new_img, g.get_rooms, new_img._cell_size)
    rooms = list(g.get_rooms.keys())
    DrawManager(rooms)

    
    img = draw_grid(
        img=new_img,
        rows=rows_cols,
        cols=rows_cols
    )
    
    
    cv.imshow("image", new_img._img)
    
    
    # setting mouse handler for the image 
    # and calling the click_event() function
    cv.setMouseCallback('image', coord_store.click_event)
    
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main(new_img)
    
