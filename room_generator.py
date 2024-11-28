import random
from room import Room
from undirected_graph import UndirectedGraph
from image import NewImage


class RoomGenerator:
    
    
    def __init__(self, rooms_number: int, img: NewImage, graph: UndirectedGraph, cell_size):
        self.rn = rooms_number
        self.g = graph
        self.img = img
        self.cell_size = cell_size
        self.x = 0
        self.y = 15
        self.rooms = []
        self.edges = {}
    
    
    def create_first_room(self) -> None:
        x,y = tuple(random.randint(self.x, self.y) for _ in range(2))
        start_room = Room(self.img, x, y, self.cell_size)
        self.g.add_vertex(start_room)

        
        
    def create_next_room(self, room):
        random.seed()
        random_room = self.get_random_room()
        coord = random.choice(['x', 'y'])
        if coord == 'x':
            pass
            
        else:
            print(coord)

    def get_random_room(self):
        
        while True:
            r = random.choice(list(self.g.get_rooms.keys()))
            if len(self.g._adjacency_list[r]) < 4:
                break
                    
        print("random room ID: " + str(r.id))
        return r
