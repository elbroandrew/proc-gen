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

        
        
    def place_next_room(self):
        random.seed()
        selected_room = self.choose_random_room()
        coord = random.choice(['x'])
        adj_list = self.g.get_rooms
        if coord == 'x':
            _x = random.choice([-1, 1])
            # check if there are no walls right or left of the selected room
            if selected_room.x - 1 >= 0 and selected_room.x + 1 <= selected_room.boundary_max:
                rx = selected_room.x + _x   # place room to the right or left
                coords_list = []
                for room in adj_list[selected_room]:
                    coords_list.append((room.x, room.y))
                if not (rx, selected_room.y) in coords_list:
                    # I can place a room to the right or left
                    new_room = Room(self.img, rx, selected_room.y, self.cell_size)
                    self.g.add_vertex(new_room)
                    self.g.add_edge(selected_room, new_room)
                    
                        
                        
            
            elif selected_room.x - 1 < 0:
                # I cannot do -1, only +1
                pass
                
            
            
        elif coord == 'y' and (selected_room.y - 1 >= 0 or selected_room.y + 1 <= selected_room.boundary_max ):
            _y = random.choice([-1, 1])

            print(coord)

    def choose_random_room(self):
        
        running = True
        while running:
            room = random.choice(list(self.g.get_rooms.keys()))
            if len(self.g._adjacency_list[room]) < room.max_edges:
                # print(f"max edges from WHILE LOOP: {room.max_edges}")
                # print("random room ID: " + str(room.id))
                return room
            else:
                running = False
                    
        # print("random room ID: " + str(room.id))
        # print(f"max edges OUTSIDE LOOP: {room.max_edges}")
        return None
