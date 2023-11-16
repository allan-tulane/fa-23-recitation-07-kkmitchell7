# CMPS 2200 Recitation 10## Answers

**Name:** Kailen Mitchell
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** What is the work of reachable, assuming $n$ nodes and $m$ edges?

W(n) = O(n+m)

- **4)** What is the worst case number of times we need to call reachable to determine if a graph is connected?

Once because reachable determines all of the reachable nodes and if we're missing any nodes connected to any one node, the graph isn't fully connected.

- **5)** What is the work of connected, assuming $n$ nodes and $m$ edges?

W(n) = O(n+m+n)

- **7)** What if we switched the graph representation to an adjacency matrix? Would the work of reachable change? If so, what would it be? If not, why not?

Yes the work would change to be O(m^2) since now we have to traverse an entire 2D matrix rather than just using the list connections
