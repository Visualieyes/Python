# Find Hamiltonian Paths


# Problem:
 Represent a random graph of n vertices of at least degree one (n is at least 100). 
 This graph might be undirected or directed. It could have cycles or no cycles. 
 Randomly select two vertices (x,y) from the graph, and find all of the possible hamiltonian paths in the graph.
 

# Approach:
1. Classical Brute-Force
3. Quantum Search

# Notes
- Hamiltonian Path: A path which visits every vertex in a graph exactly once.
- This problem is NP Complete.
- A cycle could lead to infinite searches in the graph. Nodes visited must be stored.
- Using Classical Computing algorithms this problem can, at best, be solved in polynomial time.
- Recursive algs will only scale to so many nodes until an iterable solution must be used, but it makes for cleaner to read code, in my opinion at least. 
- Worst-case, every node is redudantly interconnected and N! paths will be stored. * Example: Consider a graph of the human population where N is 7 billion. Say we want to simulate the ways a virus could traverse through each person in the population individually (not expontially). The number of different 'paths' would be (7billion)!, which is a very large number. Too large for a classical computer. As a result a more efficient method is needed in order to solve the problem. *
- Quantum search algorithms could provide quadratic or even exponential speed up the time of the search. 
- *Important* Depending on the goal of the search, a quantum approach might not necessarily always be optimal, especially considering the learning curve for unversed and inexperienced developers. 
- Due to quantum noise, any theoretical improvement risks being lost due to the current state of hardware. 
- If we want to find *all* possible paths, then they will still *all* need to be stored or displayed somehow. The worst-case  complexity would still be (N-1)!. *(n-1) since we start from a given vertex*. 
- A quantum search, such as grovers search, might provide a quick speed up to search and find a particular path thats hamiltonian in a large set of paths that would otherwise not be. Moreoeover, if quantum circuits can optimize storage or memory access then the potential improvement of quantum algorithms would surely supersede that of classical computing algorithms. *Example: While only 1 bit of information can be extracted from measuring a qubit, it can still hold much more information until that point. Consider a states which represent all perumtations of vertices from a given graph. We can optimize memory usage by only measuring for paths that are hamiltonian. But, again, worst-case every possible state measured returns a path that is hamiltonian. Considering these cases, a hybrid solution would make the most sense. By considering N and the total degree of the graph, we can predict whether we should optimize our approach in order to sift through superfluous information, or whether we'll need to go through each path regardless.* 
- This research 'path' is certainly something I'm interested in pursuing. 
- Networkx doesn't contain any function for generating random graphs that provides parameters to specify both degree and directed/undirected. The closest paramter it provides for degree is a probality value for edge creation. Specified at 1, to prevent the chance that any vertice would have 0 edges, the total degree often leads to a hyper-redundant graph, which is essentially just generating worst case graphs for my algorithm. 
- Be mindful that you're applying to a quantum computing company. While it may look proactive to conduct and provide research on competitors, like IBM or D-wave, avoid actually giving them a solution which requires them to use their competitors services unless some kind of consent from the company is given/ advised.

# Solutions + Implementation
  1. Depth-First Search (DFS): From a given vertex, traverse the graph for all it's adjacencies. As you traverse, store path and visited nodes. If the given path is hamiltonian, output it. Since the problem is NP complete and specifies at least a 100 nodes, this is perfectly sufficient because at worst case you'll need to check every permutation anyways. Worst-Case: O(n!) but really like 2 * O((n-1)!) because we dont check every vertex, we start with one, n-1) and check the rest. Then we do this for another given vertex. Recursive implementation is clean and elegant but leads to stackoverflow passed 990 nodes. 
 
  2. Grover's Search (*pseudo code only*): Use Grovers algorithm to quantum mechanically search and find all hamiltonian paths in a graph. Idea: Store vertices and connections as a matrix table. Cells are 1 or 0 depending on whether there is an edge connecting the vertices. This matrix structure of 0/1 states makes it convenient for linear algebra and quantum computing algorithms, such as grovers search. Groves search algorithm allows us to be in a superposition of states or paths and return true the states that are marked hamiltonian.  We can leverage this functionality in two ways. 1. Analyze matrix for all possible paths or states, return the index for those that are marked as hamiltonian. 2. Superposition of states, return true if path is a hamiltonian path. Theoretically, this solution promises to provide a quadratic speed up to that of a classical computing algorithm.


# Languages + Modules
- Python Programming Lanugage (3.7): Python is widely used, well supported, and extremely readable. When solving with complex problems that involve multiple chunks of information, a highly-readable programming language will increase the cognitive resources available to focus solving the problem rather than on syntax and code. 
- Networkx: Objects and Methods for constructing, initalizing, and accessing a random graph.
- MatPlotLib: Methods to display a visual representation of the graph.
- Pyquil: A well supported, open-source framework for quantum computing that allows you to leverage a QVM (quantum virtual machine) in order to run quantum code on a classical computer. It's recommended to pip install this module into a virtual environment.



# Sources
- https://networkx.github.io/documentation/networkx-1.9/overview.html
- https://awesomeopensource.com/project/rigetti/pyquil
- http://docs.rigetti.com/en/stable/start.html
- https://quantum-computing.ibm.com/docs/
