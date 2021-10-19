# Lab-4


## Task
Build directed and weighted graph from input and implement Dijkstra algorithm to find average distance from vertex **S** 
to all available vertexes
---

##Input
  + First row contain two numbers **N**, **S**: **N** - amount of edges, 0 < N <= 10000; **S** - start vertex
  + The next N rows contain 3 numbers - start of edge, end of edge and weight of edge, weight >= 0
---

##Output
Output contains only one number - average distance from vertex **S** to all available vertexes

---

##Algorithm
1. Add start vertex to min priority queue, prioritized by distance
2. For every `cur_vertex` in queue do the following:
    + For every vertex with edge from `cur_vertex` to it:
        + Add to queue if not visited
        + Update distance with min value
    + Remove from queue

<b>Complexity = O(V + E*logV)</b>
 
---

## How to run
  + `cd` into folder where you want to store this repository
  + Clone this repository with command `git clone https://github.com/max-dmytryshyn/Algorithms-Labs.git`
  + Choose branch lab_3 with command `git checkout lab_4`
  + Go into folder with files with command `cd Algorithms-Labs`
  + run command `python3 dijkstra_algorithm.py` on Mac/Linux *or* `py dijkstra_algorithm.py` on Windows 