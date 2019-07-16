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
    for i in range(len(all_connections)):
        print(all_connections[i].connected_edges)

    # Second column will contain the count of each node.
    for i in range(0, edge_count):
        all_edges_from_one_node[edges[i][0]][1] = all_edges_from_one_node[edges[i][0]][1] + 1
        all_edges_from_one_node[edges[i][1]][1] = all_edges_from_one_node[edges[i][1]][1] + 1

    # Sort the originating nodes based on the increasing complexity. We use fail-first.
    # Assign the color to the node which has largest edges originating from itself.
    all_edges_from_one_node.sort(key=operator.itemgetter(1), reverse=True)

    print(all_edges_from_one_node)

    # Contains the colors from 0 to node_count
    all_colors = [[0]*2 for _ in range(node_count)]

    # print(all_colors)

    # Start assigning the colors to nodes.
    all_colors_filled=0
    while all_colors_filled==0:
        for i in range(len(all_edges_from_one_node)):
            if all_edges_from_one_node[i][2] == -1:
                all_edges_from_one_node[i][2] = get_color(all_colors)

            all_colors_filled = 1

    solution = 0
    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
    # output_data += ' '.join(map(str, solution))

    return output_data

def check_feasible(all_edges_from_one_node):
    return 0

def get_color(all_colors):
    for i in range(len(all_colors)):

        return 0




if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')
