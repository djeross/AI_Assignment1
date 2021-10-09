class PriorityQueue:
    
    def __init__(self):
        self.queue = []
    

    # ** FINISH THIS FUNCTION **
    # Should take minmum element from priority queue and return element       
    def dequeue(self):
        pass

        
    # ** FINISH THIS FUNCTION **
    # Should add element to priority queue
    def enqueue(self, el):
        pass

class Node:
    
    def __init__(self, label, parent):
        self.label = label
        self.parent = parent # parent node
        self.g = 0 # total path cost from start node
        self.f = 0 # final cost
        self.h = 0 # heuristic distance
    
    # allows you to compare two nodes using <
    def __lt__(self, other):
         return self.f < other.f
        
    def __str__(self):
        return str((self.label, self.f))

# Returns the children/negihbours of a node in the graph including path cost
# e.g. [('A', 20), ('B', 30), ('D', 50)]
# graph - dictionary of nodes and edges
# node - label of node
def get_children(graph, node):
    children = []
    if node in graph.keys():
        children = list(graph[node].items())
    return children


# ** FINISH THIS FUNCTION **
# Should return a list representing the path from start to goal
# e.g ['A', 'B', 'G'] would be a possible solution starting from start node A to goal node G
# If there is no path from start to goal, the function should return empty list
# path_graph - dictionary of nodes and edges
# heurist_dist - dictionary of heuristic distance to goal
# start - label for start node e.g. 'A'
# goal - label for goal node e.g. 'G'
# search_type - can be one of UCS, Greedy, A-Star
# fringe_type - data structure used for fring can be one of p_queue, heap
def path_find(path_graph, heurist_dist, start, goal, search_type='UCS'):

    if search_type=='UCS':
        
        return UCS(path_graph, heurist_dist, start, goal)
    
    elif search_type=='A-Star':
        
        return A_star(path_graph, heurist_dist, start, goal)
    
    elif search_type=='Greedy':

        return Greedy(path_graph, heurist_dist, start, goal)

def UCS(path_graph, heurist_dist, start, goal):
    fringe = PriorityQueue();

    start_node = Node(start, None)
    goal_node = Node(goal, None)
    
    visited = []
    goal_found = False
    fringe.enqueue(start_node) # add the start node to fringe

def Greedy(path_graph, heurist_dist, start, goal):
    fringe = PriorityQueue();

    start_node = Node(start, None)
    goal_node = Node(goal, None)
    
    visited = []
    goal_found = False
    fringe.enqueue(start_node) # add the start node to fringe

def A_Star(path_graph, heurist_dist, start, goal):
    fringe = PriorityQueue();
    
    start_node = Node(start, None)
    goal_node = Node(goal, None)
    
    visited = []
    goal_found = False
    fringe.enqueue(start_node) # add the start node to fringe



    
    
