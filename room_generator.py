import random
from room import Room
from undirected_graph import UndirectedGraph
from image import NewImage


class RoomGenerator:
    
    
    def __init__(self, rooms_number: int, img: NewImage, graph: UndirectedGraph, cell_size):
        self.rooms_number = rooms_number
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
        selected_room = self.choose_random_room()   
        walls_coords = self.get_walls_coords(selected_room)
        new_room_x, new_room_y = self.new_room_coords(selected_room)
        
        while True:
            if (new_room_x, new_room_y) in walls_coords:
                new_room_x, new_room_y = self.new_room_coords(selected_room)
            else:
                break
            
        
        coord = random.choice(['x', 'y'])
        if coord == 'x':
            _x = random.choice([-1, 1])
            # check if there are no walls right and left of the selected room
            if selected_room.x - 1 >= 0 and selected_room.x + 1 <= selected_room.boundary_max:
                # place room to the right or left
                rx = selected_room.x + _x  
                room_exists = self.g.get_room_by_coord(rx, selected_room.y)
                if room_exists: # check if no room (connected or not) to the left or right
                    # check for EDGE:
                    if self.g.check_edge(room_exists, selected_room) is False:
                        # create an edge randomly
                        edge = random.choice([True, False])
                        if edge:
                            self.g.add_edge(selected_room, room_exists)
                else:
                    new_room = Room(self.img, rx, selected_room.y, self.cell_size)
                    self.g.add_vertex(new_room)
                    self.g.add_edge(selected_room, new_room)
                        
            # can create only to the RIGHT (left wall)
            elif selected_room.x - 1 < 0 and selected_room.x + 1 <= selected_room.boundary_max:
                _x = 1
                rx = selected_room.x + _x   # place room to the right
                room_exists = self.g.get_room_by_coord(rx, selected_room.y)
                if room_exists: # check if no room (connected or not) to the left or right
                    # check for EDGE:
                    if self.g.check_edge(room_exists, selected_room) is False:
                        # create an edge randomly
                        edge = random.choice([True, False])
                        if edge:
                            self.g.add_edge(selected_room, room_exists)
                else:
                    new_room = Room(self.img, rx, selected_room.y, self.cell_size)
                    self.g.add_vertex(new_room)
                    self.g.add_edge(selected_room, new_room)
                    
            # can place room only to the LEFT (right wall)
            elif selected_room.x - 1 >= 0 and selected_room.x + 1 > selected_room.boundary_max:
                _x = -1
                rx = selected_room.x + _x   # place room to the right
                room_exists = self.g.get_room_by_coord(rx, selected_room.y)
                if room_exists: # check if no room (connected or not) to the left or right
                    # check for EDGE:
                    if self.g.check_edge(room_exists, selected_room) is False:
                        # create an edge randomly
                        edge = random.choice([True, False])
                        if edge:
                            self.g.add_edge(selected_room, room_exists)
                else:
                    new_room = Room(self.img, rx, selected_room.y, self.cell_size)
                    self.g.add_vertex(new_room)
                    self.g.add_edge(selected_room, new_room)
                   
        elif coord == 'y':
            _y = random.choice([-1, 1])
            if selected_room.y - 1 >= 0 and selected_room.y + 1 <= selected_room.boundary_max:
                ry = selected_room.y + _y   # place room to the top or bottom
                room_exists = self.g.get_room_by_coord(selected_room.x, ry)
                if room_exists:
                    # check for EDGE:
                    if self.g.check_edge(room_exists, selected_room) is False:
                        # create an edge randomly
                        edge = random.choice([True, False])
                        if edge:
                            self.g.add_edge(selected_room, room_exists)
                else:
                    new_room = Room(self.img, selected_room.x, ry, self.cell_size)
                    self.g.add_vertex(new_room)
                    self.g.add_edge(selected_room, new_room)
                    
            elif selected_room.y - 1 < 0 and selected_room.y + 1 <= selected_room.boundary_max:
                _y = 1
                ry = selected_room.y + _y 
                room_exists = self.g.get_room_by_coord(selected_room.x, ry)
                if room_exists:
                    # check for EDGE:
                    if self.g.check_edge(room_exists, selected_room) is False:
                        edge = random.choice([True, False])
                        if edge:
                            self.g.add_edge(selected_room, room_exists)
                else:
                    new_room = Room(self.img, selected_room.x, ry, self.cell_size)
                    self.g.add_vertex(new_room)
                    self.g.add_edge(selected_room, new_room)
                    
            elif selected_room.y - 1 >= 0 and selected_room.y + 1 > selected_room.boundary_max:
                _y = -1
                ry = selected_room.y + _y
                room_exists = self.g.get_room_by_coord(selected_room.x, ry)
                if room_exists:
                    # check for EDGE:
                    if self.g.check_edge(room_exists, selected_room) is False:
                        # create an edge randomly
                        edge = random.choice([True, False])
                        if edge:
                            self.g.add_edge(selected_room, room_exists)
                else:
                    new_room = Room(self.img, selected_room.x, ry, self.cell_size)
                    self.g.add_vertex(new_room)
                    self.g.add_edge(selected_room, new_room)
                   
                   
    def new_room_coords(self, room):
        x,y = random.choice([(-1, 0),(1, 0), (0, 1), (0, -1)])
        return room.x+x, room.y+y
                    
    def get_walls_coords(self, room):
        _keys = ['left','right','top', 'bottom']
        walls_coords = dict.fromkeys(_keys, None)
        
        if room.x - 1 < 0:
            walls_coords['left'] = (room.x - 1, room.y)
        if room.x + 1 > room.boundary_max:
            walls_coords['right'] = (room.x + 1, room.y)
        if room.y - 1 < 0:
            walls_coords['top'] = (room.x, room.y - 1)
        if room.y + 1 > room.boundary_max:
            walls_coords['bottom'] = (room.x, room.y + 1)
        return [x for x in walls_coords.values() if x is not None]
            
        

    def choose_random_room(self):
        rooms_overall = list(self.g.get_rooms.keys())
        if len(rooms_overall) == self.rooms_number:
            raise SystemExit("Cannot create new room because the number of rooms equals to overall rooms.")
        
        room = random.choice(rooms_overall)
        if len(self.g._adjacency_list[room]) >= room.max_edges:
            return self.choose_random_room()
                    
        return room


    def create_rooms(self):
        for n in range(self.rooms_number):  # 10-1 + start room = 10
            self.place_next_room()