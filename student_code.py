def dist(pointA, pointB):  #pointA == [0.7798606835438107, 0.6922727646627362], pointB == [0.7647837074641568, 0.3252670836724646]
    return np.sqrt((pointA[0]-pointB[0])*(pointA[0]-pointB[0]) + (pointA[1]-pointB[1])*(pointA[1]-pointB[1]))

#case1: if the goal is unreachable, return -1
#case2: when a path has no unexplored new neighbor but not reach the goal,delete the path. 
        #definition of explored node: a node was a frontier and has been searched it's neighbors
#case3: after reach the goal with a path, do not stop, continue search if there is shorther total estimated distance in the path list

def shortest_path(M,start,goal):
    print("shortest path called")
    nodes = M.intersections  # sorten the name for convinience, nodes includes (x, y) coordinates set. e.g. {0:[x0,y0],1:[x1,y1]}
    if start == goal: # edge case: the start is already the goal
        return [goal]
    
    sol_list = {"path":[[start]], "path_cost":[0], "total_est_cost":[0]}  # save pathes list
                #This list will be refreshed by every newly explored neighbor of a frontier.
                # a frontier: The nearest node to the goal in a path
                # e.g. path: [[1,2,3],[1,5,6],[1,3,7]], path_cost:[400,500,600], total_est_cost:[450, 560, 670]
                # We will find path with smallest total_est_cost
    min_total_index = 0  # keep track of the index of of the min value of total_est_cost
    frontier = start  # The nearest node to the goal in a path
    nodes_has_been_explored = [] # a node has been explored, should not to concidered for another path.
                                 # This is because the shortest path from the start node to this node has been included to the path list already.
    # continue searching next frontier untill the shortest path's(the path with minimum total_est_cost) frontier reach the goal.
    while frontier != goal:  
        
        count_neighbors = 0  # count explored neighbors
        for node_next in M.roads[frontier]: # search neighbours
            if node_next in nodes_has_been_explored:  
                count_neighbors +=1
                if count_neighbors == len(M.roads[frontier]):
                    #edge case: 
                    #if a path with frontier has all neighbors has been explored but not reach to the goal, we delete this path.
                    del sol_list["path"][min_total_index]
                    del sol_list["path_cost"][min_total_index]
                    del sol_list["total_est_cost"][min_total_index]
                continue
            else:
                # add a new path with every neighbor
                dist_frontier_next = dist(nodes[frontier], nodes[node_next])  # distance between the frontier node to the next neighbour
                current_path_cost = sol_list["path_cost"][min_total_index]  # path_cost from the start node to the frontier node.
                est_next =  dist(nodes[node_next], nodes[goal])

                # put the neighbor after the frontier
                new_path = sol_list["path"][min_total_index] + [node_next]
                sol_list["path"].append(new_path)
                sol_list["path_cost"].append(current_path_cost + dist_frontier_next)
                sol_list["total_est_cost"].append(current_path_cost + dist_frontier_next + est_next)
        # there is no reachable path found
        if len(sol_list["path"]) == 0:
            return -1
        if count_neighbors < len(M.roads[frontier]):  # new pathes added.
            # delete the original path before extend. because it is already included in new pathes
            nodes_has_been_explored.append(frontier)  # mark the frontier node as has been explored node.
            del sol_list["path"][min_total_index]
            del sol_list["path_cost"][min_total_index]
            del sol_list["total_est_cost"][min_total_index]
            
        #find the mimimum_total in the sol_list, refresh the frontier node.whatever any path reaches the goal
        min_total_index = sol_list["total_est_cost"].index(min(sol_list["total_est_cost"]))
        frontier = sol_list["path"][min_total_index][-1]
        
    #shortest path's(the path with minimum total_est_cost) frontier reach the goal.
    # we found the sortest path
    return sol_list["path"][min_total_index]