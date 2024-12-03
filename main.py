import cv2 as cv
from undirected_graph import UndirectedGraph
from image import NewImage
from room_generator import RoomGenerator
from draw_manager import DrawManager
from find_path_manager import PathManager

        

def main():
    new_img = NewImage()
    rows_cols=new_img._rows_cols    
    cell_size = new_img._cell_size
    rooms_number = 20
    draw_manager = DrawManager(new_img, new_img._cell_size)
    path_manager = PathManager(new_img, rows_cols, draw_manager)
    g = UndirectedGraph()
    generator = RoomGenerator(rooms_number, new_img, g, cell_size)
    
    generator.create_first_room()
    generator.create_rooms()

        
    rooms = list(g.get_rooms.keys())
    draw_manager.draw_grid(rows_cols, rows_cols)
    draw_manager.draw_rooms(rooms)
    draw_manager.draw_corridors(g.get_rooms)
    
    param = {
        "graph": g,
        "current_room": g.root,
    }
    print("current_room: ",param["current_room"].id)
        
    
    cv.imshow("image", new_img._img)
    
    
    # setting mouse handler for the image 
    # and calling the click_event() function
    cv.setMouseCallback('image', path_manager.find_path, param=param)
    
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
    
