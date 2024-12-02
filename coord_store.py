import cv2 as cv
from math import floor

class CoordinateStore:
    
    def __init__(self, img, rows_cols):
        self.img=img._img
        self.rc = rows_cols
        self.room_coords = (0, 0)
            

    def click_event(self, x, y, ):
        rx, ry = self.converted_coords(self.rc, self.rc, x, y)
        self.room_coords = rx, ry
        print(self.room_coords)
            
            
            
    def converted_coords(self, rows, cols, xx, yy):
        h, w, _ = self.img.shape
        dy, dx = h/rows, w/cols
    
    
        return floor(xx/dx), floor(yy/dy)