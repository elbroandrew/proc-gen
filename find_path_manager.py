import cv2 as cv
from coord_store import CoordinateStore


class PathManager:
    
    def __init__(self, img, rowscols):
        self.coord_store = CoordinateStore(img, rowscols)
        self.g = None
    
    def find_path(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.coord_store.click_event(x, y)
            # find path with BFS
            self.g = param["graph"]
            current_room = param["current_room"]
            target_room = self.g.get_room_by_coord(*self.coord_store.room_coords)
            path = self.g.bfs_find_path(current_room, target_room)
            if path is None:
                print("No path.")
            else:
                for r in path:
                    print(r.id)
                param["current_room"] = target_room
                print("current_room: ",param["current_room"].id)

                    
                    
    