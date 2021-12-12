# Lab-5


## Task
    Impelement Prim's algortithm for finding the Minimum Spanning Tree
---

## Input
    Undirected and connected graph
---

## Output
    Single number - minimum edges weight to build spanning tree of given graph
---

## Algorithm
1. Maintain two disjoint sets of vertices. One containing vertices that are in the growing spanning tree and other that 
are not in the growing spanning tree.
2. Select the cheapest vertex that is connected to the growing spanning tree and is not in the growing spanning tree and
 add it into the growing spanning tree. This can be done using Priority Queues. Insert the vertices, that are connected to growing spanning tree, into the Priority Queue.
3. Check for cycles. To do that, mark the nodes which have been already selected and insert only those nodes in the 
Priority Queue that are not marked.

<b>Complexity = O(E*logV)</b>
 
---

## How to run
  + `cd` into folder where you want to store this repository
  + Clone this repository with command `git clone https://github.com/max-dmytryshyn/Algorithms-Labs.git`
  + Choose branch lab_5 with command `git checkout lab_5`
  + Go into folder with files with command `cd Algorithms-Labs/Lab_5`
  + run command `python3 -m unittest test.py` on Mac/Linux *or* `py -m unittest test.py` on Windows 
