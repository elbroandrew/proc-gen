import cv2 as cv
from coord_store import CoordinateStore


class PathManager:
    
    def __init__(self, img, rowscols, dm):
        self.coord_store = CoordinateStore(img, rowscols)
        self.img = img
        self.g = None
        self.draw_manager = dm
    
    def find_path(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.coord_store.click_event(x, y)
            # find path with BFS
            self.g = param["graph"]
            # self.draw_manager = param["dm"]
            current_room = param["current_room"]
            target_room = self.g.get_room_by_coord(*self.coord_store.room_coords)
            path = self.g.bfs_find_path(current_room, target_room)
            if path is None:
                print("No path.")
            else:
                for r in path:
                    print(r.id)
                param["current_room"] = target_room
                self.draw_manager.draw_path(path)
                cv.imshow("image", self.img._img)
                print("current_room: ",param["current_room"].id)
                
    

                    
                    
    