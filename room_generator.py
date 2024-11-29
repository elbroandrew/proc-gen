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
        coord = random.choice(['x', 'y'])
        adj_list = self.g.get_rooms
        if coord == 'x':
            _x = random.choice([-1, 1])
            # check if there are no walls right and left of the selected room
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

            # can create only to the RIGHT (left wall)
            elif selected_room.x - 1 < 0 and selected_room.x + 1 <= selected_room.boundary_max:
                _x = 1
                rx = selected_room.x + _x   # place room to the right
                coords_list = []
                for room in adj_list[selected_room]:
                    coords_list.append((room.x, room.y))
                if not (rx, selected_room.y) in coords_list:
                    # I can place a room to the right
                    new_room = Room(self.img, rx, selected_room.y, self.cell_size)
                    self.g.add_vertex(new_room)
                    self.g.add_edge(selected_room, new_room)
            # can place room only to the LEFT (right wall)
            elif selected_room.x - 1 >= 0 and selected_room.x + 1 > selected_room.boundary_max:
                _x = -1
                rx = selected_room.x + _x   # place room to the left
                coords_list = []
                for room in adj_list[selected_room]:
                    coords_list.append((room.x, room.y))
                if not (rx, selected_room.y) in coords_list:
                    # I can place a room to the left
                    new_room = Room(self.img, rx, selected_room.y, self.cell_size)
                    self.g.add_vertex(new_room)
                    self.g.add_edge(selected_room, new_room)
                   
        elif coord == 'y':
            if selected_room.y - 1 >= 0 or selected_room.y + 1 <= selected_room.boundary_max:
                _y = random.choice([-1, 1])
                # check if there are no walls top and bottom of the selected room
                if selected_room.y - 1 >= 0 and selected_room.y + 1 <= selected_room.boundary_max:
                    ry = selected_room.y + _y   # place room to the top or bottom
                    coords_list = []
                    for room in adj_list[selected_room]:
                        coords_list.append((room.x, room.y))
                    if not (selected_room.x, ry) in coords_list:
                        # I can place a room to the top or bottom
                        new_room = Room(self.img, selected_room.x, ry, self.cell_size)
                        self.g.add_vertex(new_room)
                        self.g.add_edge(selected_room, new_room)


    def choose_random_room(self):
        # base case
        
        room = random.choice(list(self.g.get_rooms.keys()))
        if len(self.g._adjacency_list[room]) >= room.max_edges:
            return self.choose_random_room()
                    
        return room
