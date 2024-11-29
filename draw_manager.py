

class DrawManager:
     
    def __init__(self, rooms):
        
        for room in rooms:
            room.draw()
        