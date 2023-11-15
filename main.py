from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        for item in frontier:
            connection = graph[item]
            result.add(item)
            frontier.remove(item)
            frontier.add(connection)
    return result





def connected(graph):
    connectednodes = reachable(graph,graph[0])
    for item in connectednodes:
        if item not in graph:
            return false
    return true




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    pass

