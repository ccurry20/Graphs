"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
    #make a que
        q = Queue()
    # enqueue our start node
        q.enqueue(starting_vertex)

    #make a set to track visited nodes
        visited - set()

    #while queue stilll has things in it         
        while q.size() > 0
    ##dq from front of the line, this is our current node 
        current_node = d.dequeue()
    ## check if we've visited, if not:
        if current_node not in visited:
    ## mark it as visited 
        visited.add(current_node)
        print(current_node)
    ## get its neighbors 
        neighbors = self.get_neighbors(current_node)
    ## iterate over neighbors
        for neighbor in neighbors:
    ## add to queue             
        q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #make a stack        
        s = Stack()        
        #push our starting node onto the stack         
        s.push(starting_vertex)        
        #make a set to track the nodes we've vistited       
        visited = set()
        #as long as our stack isn't empty         
        while s.size() > 0        
        #pop off the top, this is our current node             
            current_node = s.pop()                
        #check if we have visited this before, and if not:             
        if current_node not in visited:         
            #mark it as visited             
            visited.add(current_node)        
        #print it (in this case)            
            print(current_node)        
        #get its neighbors             
        neighbors = self.get_neighbors(current_node)        
        #iterate over neighbors           
        for neighbor in neighbors:        
        #and add them to our stack             
            s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #check if we have been visited (get neighbors or return)        
        if vertex not in visited:             
            visited.add(vertex)        
        #base case: if no neighbors             
        neighbors = self.get_neighbors(vertex)            
            if len(neighbors) == 0:                
                return         
        #if we do have neighbors, iterate over them and recurse for each one            
            for neighbor in neighbors:                
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        # make a set to track visited 
        visited = set()
        # enqueue a PATH to the starting vertex
        path = [starting_vertex]
        q.enqueue(path)
        # as long as our queue isn't empty 
        while q.size() > 0:
        # dequeue from the front of the line, this is our current path: []
        q([1,2])
            current_path = q.dequeue()
            [1,2]
        # current_node is the last thing in the path 
            current_node = path[-1]
        # check if this is the target node 
            if current_node = destination_vertex:
        # if so return 
                return current_path
        # check if we've visted yet, if not: 
            if current_node not in visited:
        # mark as visited 
                visited.add(current_node)
        #get the current node's neighbors
                neighbors = self.get_neighbors(current_node)
        # iterate over the neighbors 
                for neighbor in neighbor:
        # add the neighbor to the path 
                    neighbor_path = copy(current_path)
                    neighbor_path.append(neighbor)
        # enqueue the neighbor's path 
                    q.enqueue(neighbor_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        path = [starting_vertex]
        s.push(path)

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the first PATH
            v = s.pop()

            # Grab the last vertex from the PATH
            last = v[-1]

            if last is destination_vertex:
                # IF SO, RETURN PATH
                return v

            # If that vertex has not been visited...
            if last not in visited:
                # CHECK IF IT'S THE TARGET

                # Mark it as visited...
                visited.add(last)

                # Then add A PATH TO its neighbors to the back of the queue
                for next_vert in self.get_neighbors(last):
                    copy = v[:]
                    copy.append(next_vert)
                    s.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None: 
            visited = set()
        
        if starting_vertex not in visited: 
            visited.add(starting_vertex)
        
        if starting_vertex == destination_vertex:
            return path 
        
        neighbors = self.get_neighbors(starting_vertex)

        for neighbor in neighbors: 
            if neighbor not in visited: 
                #recurse
                result = self.dfs_recursive(neighbor, path + [neighbor], destination_vertex, visited)
                if result is not None: 
                    return result
        
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
