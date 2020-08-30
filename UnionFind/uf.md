<pre><code>
    class DisjointSetUnion(object):

        def __init__(self, size):
            # initially, each node is an independent component
            self.parent = [i for i in range(size+1)]
            # keep the size of each component
            self.size = [1] * (size+1)
        
        def find(self, x):
            """ return the component id that the element x belongs to. """
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            """ merge the two components that x, y belongs to respectively,
                and return the merged component id as the result.
            """
            px, py = self.find(x), self.find(y)
            
            # the two nodes share the same set
            if px == py:
                return px
            
            # otherwise, connect the two sets (components)
            if self.size[px] > self.size[py]:
                # add the node to the union with less members
                # keeping px as the index of the smaller component
                px, py = py, px
            # add the smaller component to the larger one
            self.parent[px] = py
            self.size[py] += self.size[px]
            # return the final (merged) group
            return py
</code></pre>


Since we applied the Union-Find data structure in our algorithm, we would like to start with a statement on the time complexity of the data structure, as follows:

Statement: If MM operations, either Union or Find, are applied to NN elements, the total run time is <img src="https://render.githubusercontent.com/render/math?math={O}(M \cdot \log^{*}{N})">, where log∗ is the iterated logarithm.

