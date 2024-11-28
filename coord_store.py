import cv2 as cv
from math import floor

class CoordinateStore:
    
    def __init__(self, img, rows_cols):
        self.points=[]
        self.img=img
        self.rc = rows_cols
            

    def click_event(self, event, x, y, flags, params):
        if event == cv.EVENT_LBUTTONDOWN:
            dx, dy = self.converted_coords(self.rc, self.rc, x, y)
            print(dx, dy)
            
    def converted_coords(self, rows, cols, xx, yy):
        h, w, _ = self.img.shape
        dy, dx = h/rows, w/cols
    
    
        return floor(xx/dx), floor(yy/dy)