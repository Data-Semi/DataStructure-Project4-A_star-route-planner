# DataStructure-Project4-A_star-route-planner  

This is a route-planning algorithm like the one used in Google Maps to calculate the shortest path between two points on a map.  
I used the A* algorithm to find a path.  
A* algorithm has a base function to calculate the total estimated cost of a path, which helps us to avoid "greed search" on the map.  
total estimated cost f = g + h  
g: the path cost, the sum of distances between every node in the path.  
h: the heuristic estimation, estimation of the cost from the frontier to the goal.  
I chose the heuristic estimation h the distance between the frontier to the goal. This can keep the h is the smallest cost from the frontier to the goal.  
Because of this, we do not need to consider a path with a bigger total estimated cost, because there is no hope to get a smaller total estimated cost after searching on that path.  
This means we can only focus on the path which has the smallest total estimated cost.  
Therefore, we will run in a loop that always extends a path that has the smallest total estimated cost until the frontier of the chosen path reaches the goal.  

# Challenges of the program  

## 1. All neighbors of a frontier should be included in a new path.  
The first version I built is to extend a path with only one neighbor.  
How did I do is, find the only one neighbor node which has the shortest estimated path cost and continue the searching until reach the goal. 
This algorithm returns me a path with low cost so far, but not the shortest path.  
For example, When there is the shortest path to the goal but it includes a node that not chosen by a frontier during the searching, and the reason was its estimated path cost was higher than the other one which has been chosen.  

So I changed the algorithm to extend a path with all neighbors of the frontier.  
Every time the program will go and look at the dictionary `sol_list` which saves all paths that have been explored and choose the path with the lowest estimated path cost for the next explore.  
The frontier, the last node of the chosen path will search its neighbors and add new paths to the path list.  

## 2. Edge case of the goal is unreachable  
I decided to use a list `nodes_has_been_explored` to keep explored nodes for the case the goal is in an unreachable place.  
Every time the frontier has been processed, the program will append it to the list `nodes_has_been_explored`, and the next frontier will not consider its neighbor that included in the list `nodes_has_been_explored`.  
This list also shortens our searching time, because the shortest path from the start node to the node in `nodes_has_been_explored` has been found and included in the path list already, any other paths to the node should be ignored.  
If a frontier has no neighbors or its neighbors all included in `nodes_has_been_explored`, this means, this path we are considering has been reached its end, it will impossible to reach the goal. The program will delete the path from the path list.  
Finally, if there is no path in the path list to continue searching, we can say we have no path to the goal. The program will return -1 in this case.  

# Files description 
The progam code is included in project_notebook.ipynb and student_code.py

# Running environment
There is an error related to the networkX package when I try to run locally.  
I can run my program on the workspace Udacity provide to us.  
I included the data of Map in the final cell of the jupyter notebook:project_notebook.ipynb, you can use the data instead of these pickle files to avoid the error.  

Udacity says it uses the package below.  
plotly - 2.0.15
networkx - 1.11



