#!/usr/bin/python
# -*- coding: utf-8 -*-

import operator


class NodeCollection:
    def __init__(self, node_id):
        self.node_id = node_id
        self.connected_edges = []


def solve_it(input_data):

    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    # Create a matrix to count the number of edges to each node.
    # Then we will delete the nodes that are not connected.
    all_edges_from_one_node = [[0]*3 for _ in range(node_count)]
    all_connections = []

    # First column is the node number, third column indicates the color selected. -1 if no color is assigned.
    for i in range(node_count):
        all_edges_from_one_node[i][0] = i
        all_edges_from_one_node[i][2] = -1
        temp = NodeCollection(i)
        all_connections.append(temp)

    # Assign the node to node_id and update the list with all the nodes that this node is connected
    for i in range(node_count):
        for j in range(edge_count):
            if edges[j][0] == i:
                all_connections[i].connected_edges.append(edges[j][1])
            if edges[j][1] == i:
                all_connections[i].connected_edges.append(edges[j][0])

    # Print to see if the nodes are properly assigned
    # for i in range(len(all_connections)):
    #    print(all_connections[i].connected_edges)

    # Second column will contain the count of each node.
    for i in range(0, edge_count):
        all_edges_from_one_node[edges[i][0]][1] = all_edges_from_one_node[edges[i][0]][1] + 1
        all_edges_from_one_node[edges[i][1]][1] = all_edges_from_one_node[edges[i][1]][1] + 1

    # print(all_edges_from_one_node)
    # Sort the originating nodes based on the increasing complexity. We use fail-first.
    # Assign the color to the node which has largest edges originating from itself.
    all_edges_from_one_node_sorted = sorted(all_edges_from_one_node, key=operator.itemgetter(1), reverse=True)
    all_edges_from_one_node_sorted = sorted(all_edges_from_one_node, key=operator.itemgetter(0), reverse=True)

    print(all_edges_from_one_node_sorted)
    print("not sorted")
    print(all_edges_from_one_node)

    # Contains the colors from 0 to node_count. Already assigned colors
    # all_colors = [[0]*2 for _ in range(node_count)]
    all_colors = [0]*node_count

    for i in range(len(all_colors)):
        all_colors[i] = i

    # print(all_colors)

    # Start assigning the colors to nodes.
    all_colors_filled = 0
    i = 0
    while all_colors_filled == 0:
        if i <= len(all_edges_from_one_node_sorted):
            if i == len(all_edges_from_one_node_sorted):
                feasibility = check_feasible(all_edges_from_one_node, all_connections)
                if feasibility:
                    all_colors_filled = 1
                else:
                    i = 0
            else:
                if all_edges_from_one_node_sorted[i][2] == -1:
                    #all_colors = get_all_colors_for_this_node(all_colors, all_edges_from_one_node_sorted, all_connections)
                    for m in range(len(all_colors)):
                        # if all_colors[m][1] == 0:
                        all_edges_from_one_node_sorted[i][2] = all_colors[m]
                        feasibility = check_feasible(all_edges_from_one_node, all_connections)
                        if feasibility:
                            i = i + 1
                            break
        #print(all_edges_from_one_node_sorted)

    print(all_edges_from_one_node)
    solution = []
    for i in range(len(all_edges_from_one_node)):
        solution.append(all_edges_from_one_node[i][2])

    objective_value = max(solution) + 1

    #while all_colors_filled == 0:


    # prepare the solution in the specified output format
    output_data = str(objective_value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


def check_feasible(all_edges_from_one_node, all_connections):
    feasible = True
    for i in range(len(all_edges_from_one_node)):
        if feasible:
            # Take the current node to compare the colors of its color and all its connected nodes.
            current_node = all_edges_from_one_node[i]
            connected_edges_to_this_node = all_connections[current_node[0]].connected_edges
            # Iterate through the connected lists and compare the color. Not feasible if connections have same color.
            for c in range(len(connected_edges_to_this_node)):
                if current_node[2] == all_edges_from_one_node[connected_edges_to_this_node[c]][2] and current_node[2] \
                        != -1:
                    feasible = False
                    break
        else:
            break

    #print(feasible)
    return feasible


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')
