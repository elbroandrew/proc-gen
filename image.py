import numpy as np
import cv2 as cv
from PIL import Image


class NewImage:
    
    def __init__(self, img_size=512, rows_cols=16):
        self.img_size=img_size
        self.img1 = Image.new('RGB', (self.img_size, self.img_size), (0, 0, 0))
        self.img = cv.cvtColor(np.array(self.img1), cv.COLOR_BGR2RGB)
        self.rows_cols=rows_cols
        self.h, self.w, _ = self.img.shape
        self.cell_size = self.h/self.rows_cols
        
    @property
    def _img(self):
        return self.img
    
    @property
    def _cell_size(self):
        return self.cell_size
    
    @property
    def _rows_cols(self):
        return self.rows_cols
    
    @property
    def _h(self):
        return self.h
    
    @property
    def _w(self):
        return self.w