from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

#determine all the reachable nodes of a graph from the starting node
def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set(start_node)
    frontier = set(start_node)
    while len(frontier) != 0:
        #get item from frontier and remove
        item = frontier.pop()
        
        #add frontier to result
        if item not in result:
            result.add(item)

        #get all connections from graph to add to the new frontier
        connection = graph[item]
        for letter in connection:
            if letter not in result:
                frontier.add(letter)
    return result




#Check if a graph is fully connected

def connected(graph):
    connectednodes = reachable(graph,list(graph.keys())[0])
    for item in graph:
        if item not in connectednodes:
            return False
    return True


"""6 Next, we'll use reachable to determine the number of connected 
components in a graph. Complete n_components and test with test_n_components.
 Again, think about how to minimize the number of calles to reachable you 
must make."""

def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    num_components = 0
    curr_node = list(graph.keys())[0]
    tobe_visited = set(graph.keys())
    while len(tobe_visited) != 0:
        num_components +=1
        connectednodes = list(reachable(graph,curr_node))
        for node in connectednodes:
            tobe_visited.discard(node)
        
        print(tobe_visited)
        if len(tobe_visited) != 0:
            curr_node = tobe_visited.pop()
        
    
    return num_components


