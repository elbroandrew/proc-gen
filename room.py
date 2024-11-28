import cv2 as cv


class Room:
    
    _count = -1
    
    @classmethod
    def _increment_id(self):
        self._count += 1
        return self._count
        
        
    def __init__(self, img, x, y, cell_size, offset=6):
        self.img = img._img
        self.id = self._increment_id()
        self.x = x
        self.y = y
        self.boundary_min = 0
        self.boundary_max = img._rows_cols-1
        self.max_edges = self.get_max_edges()
        self.offset = offset
        self.s=int(cell_size)
        self.xx = self.x * self.s
        self.yy = self.y * self.s
        cv.rectangle(self.img, 
                     (self.xx+self.offset, self.yy+self.offset), 
                     (self.xx+self.s-self.offset, self.yy+self.s-self.offset), 
                     (70, 150, 150), -1)
        
        # draw ID
        cv.putText(self.img, 
                   str(self.id), 
                   (self.xx+12, self.yy+20), 
                   cv.FONT_HERSHEY_PLAIN, 
                   0.8, 
                   (255, 255, 255), 
                   1, 
                   cv.LINE_AA)
        
    
    def get_max_edges(self):
        if (self.x == self.boundary_min or self.x == self.boundary_max) and (self.y == self.boundary_min or self.y == self.boundary_max):
            return 2
        elif not( self.x == self.boundary_min or self.x == self.boundary_max) and not( self.y == self.boundary_min or  self.y == self.boundary_max):
            return 4
        else:
            return 3
            
            