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
    
    
    def create_start_room(self) -> None:
        x,y = tuple(random.randint(self.x, self.y) for _ in range(2))
        start_room = Room(self.img, x, y, self.cell_size)
        start_room.hidden = False
        self.g.add_vertex(start_room)
        return start_room

    def allow_to_place(self):
        
        max_limit_edges = 0  # max edges limit for existing rooms
        current_edges_number = 0  # current edges number for existing rooms
        existing_rooms = list(self.g.get_rooms.keys())
        for room in existing_rooms:
            max_limit_edges += room.max_edges
        
        for list_of_edges in self.g.get_rooms.values():
            current_edges_number += len(list_of_edges)
                      
        if current_edges_number == max_limit_edges:
            print("Cannot create new room because the number of rooms equals to overall rooms.")
            return False
        return True
        
    def place_next_room(self):
        if self.allow_to_place() is False:
            return
        selected_room = self.choose_random_room()
        while True:
            if len(list(self.g.get_rooms[selected_room])) >= selected_room.max_edges:
                selected_room = self.choose_random_room()
            else:
                break
        walls_coords = self.get_walls_coords(selected_room)
        new_room_x, new_room_y = self.new_room_coords(selected_room)
        
        while True:
            if (new_room_x, new_room_y) in walls_coords:
                new_room_x, new_room_y = self.new_room_coords(selected_room)
            else:
                break
            
        room_exists = self.g.get_room_by_coord(new_room_x, new_room_y)
        if room_exists:
            self.place_random_edge(room_exists, selected_room)
            self.place_next_room()
        else:
            new_room = Room(self.img, new_room_x, new_room_y, self.cell_size)
            self.g.add_vertex(new_room)
            self.g.add_edge(selected_room, new_room)
    
    def place_random_edge(self, room1, room2):
        # check for EDGE:
        if self.g.check_edge(room1, room2) is False:
            # create an edge randomly
            edge = random.choice([True, False])
            if edge:
                self.g.add_edge(room1, room2)
        
    
    def new_room_coords(self, room):
        x,y = random.choice([(-1, 0),(1, 0), (0, 1), (0, -1)])
        return room.x+x, room.y+y
                    
    def get_walls_coords(self, room):
        walls_coords = []
        
        if room.x - 1 < 0:
            walls_coords.append((room.x - 1, room.y))
        if room.x + 1 > room.boundary_max:
            walls_coords.append((room.x + 1, room.y))
        if room.y - 1 < 0:
            walls_coords.append((room.x, room.y - 1))
        if room.y + 1 > room.boundary_max:
            walls_coords.append((room.x, room.y + 1))
        return walls_coords
            
        

    def choose_random_room(self):
        
        room = random.choice(list(self.g.get_rooms.keys()))
        if len(self.g._adjacency_list[room]) >= room.max_edges:
            return self.choose_random_room()
                    
        return room


    def create_rooms(self):
        for _ in range(1, self.rooms_number):  # 10-1 + start room = 10
            self.place_next_room()