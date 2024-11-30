import cv2 as cv
from coord_store import CoordinateStore
from undirected_graph import UndirectedGraph
from image import NewImage
from room_generator import RoomGenerator
from draw_manager import DrawManager

        

def main():
    new_img = NewImage()
    rows_cols=new_img._rows_cols    
    cell_size = new_img._cell_size
    rooms_number = 10
    
    coord_store = CoordinateStore(new_img, rows_cols)
    g = UndirectedGraph()
    generator = RoomGenerator(rooms_number, new_img, g, cell_size)
    
    generator.create_first_room()
    generator.create_rooms()

        
    rooms = list(g.get_rooms.keys())
    draw_manager = DrawManager()
    draw_manager.draw_corridors(new_img, g.get_rooms, new_img._cell_size)
    draw_manager.draw_rooms(rooms)
    draw_manager.draw_grid(new_img, rows_cols, rows_cols)
    
    
    cv.imshow("image", new_img._img)
    
    
    # setting mouse handler for the image 
    # and calling the click_event() function
    cv.setMouseCallback('image', coord_store.click_event)
    
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
    
