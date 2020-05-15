from room import Room
from player import Player
from world import World
from utils import Stack, Queue, Graph

from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)
graph = Graph()
graph2 = Graph()
# print('#######################################')
bfs_rooms = graph2.bfs_rooms(player.current_room, None)
dfs_rooms = graph.dfs(player.current_room)
# print(dfs_rooms)


# print(bfs_rooms)
rooms = [room for room in dfs_rooms]

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# print(rooms)
visited = set()

while(len(visited) < len(room_graph) -1):
    current_room = rooms[0]
    # print(current_room)
    next_room = rooms[1]
    #find shortest path
    shortest_path = graph.bfs(current_room, next_room)
    # print(shortest_path)
    # loop over shortest path until empty
    while len(shortest_path) > 1:
        #get neighbors using dfs
        current_room_neighbors = dfs_rooms[shortest_path[0]]
        # print(current_room_neighbors)
        next_room = shortest_path[1]
        if next_room in current_room_neighbors:
            traversal_path.append(current_room_neighbors[next_room])
        shortest_path.remove(shortest_path[0])
    rooms.remove(current_room)
    visited.add(current_room)

# print(traversal_path)


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")