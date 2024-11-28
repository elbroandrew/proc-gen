import random
from room import Room
from undirected_graph import UndirectedGraph
from image import NewImage


class RoomGenerator:
    
    
    def __init__(self, rooms_number: int, img: NewImage, graph: UndirectedGraph):
        self.rn = rooms_number
        self.g = graph
        self.img = img
        self.x = 0
        self.y = 15
        self.rooms = []
        self.edges = {}
    
    
    def create_first_room(self) -> None:
        x,y = tuple(random.randint(self.x, self.y) for _ in range(2))
        start_room = Room(self.img, x, y, self.img._cell_size)
        self.g.add_vertex(start_room)

        
        
    def create_next_room(self, room):
        random.seed()
        coord = random.choice(['x', 'y'])
        if coord == 'x':
            
        else:
            print(coord)

g = RoomGenerator(7)
g.create_next_room()
        
