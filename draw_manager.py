import cv2 as cv

class DrawManager:
     
    def draw_rooms(self, rooms):
        
        for room in rooms:
            room.draw()
        
        
    def draw_corridors(self, img, adj_list: dict, size, length=8):
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